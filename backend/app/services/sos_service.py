"""
SOS Service - Emergency panic button for relationship anxiety.

Provides fast-track emergency readings with panic intervention prompts
for users experiencing acute relationship anxiety.
"""

import uuid
from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models import Card, Reading, User
from app.services.subscription_service import SubscriptionService


SOS_ERROR_CODES = {
    "SOS_CREDITS_EXHAUSTED": "SOS_CREDITS_EXHAUSTED",
    "NOT_SUBSCRIBER": "NOT_SUBSCRIBER",
    "INVALID_USER": "INVALID_USER",
}


class SOSService:
    """Service for handling emergency SOS readings."""

    def __init__(self):
        self.subscription_service = SubscriptionService()

    def build_panic_prompt(
        self, card_name: str, is_reversed: bool, emotional_profile: Optional[str] = None
    ) -> str:
        """
        Build a panic intervention prompt for SOS readings.
        
        Args:
            card_name: Name of the drawn card
            is_reversed: Whether the card is reversed
            emotional_profile: User's emotional profile
            
        Returns:
            Formatted prompt string
        """
        orientation = "逆位置" if is_reversed else "正位置"
        
        tone_guidance = ""
        if emotional_profile == "anxious":
            tone_guidance = "ユーザーは今パニック状態です。groundingな安心感を первую очередьを提供してください。"
        elif emotional_profile == "logical":
            tone_guidance = "ユーザーは論理的な説明を求めています。事実ベースで客観的な視点を提供してください。"
        elif emotional_profile == "hopeful":
            tone_guidance = "ユーザーは希望を持ちたいと感じています。温柔で励ますようなトーンしてください。"
        
        prompt = f"""あなたは今、ユーザーの緊急事態に対応しています。

状況: ユーザーは元恋人に感情的なメッセージを送りそうな非常に高い关系不安を感じています。
引くことになった: {card_name} ({orientation})

あなたのタスク:
1. まず、深呼吸するように伝えましょう（今すぐできる具体的なアクション）
2. このカードから今すぐ使える現実的な視点を提供してください
3. 「今すぐメッセージを送らないでください」と明確にアドバイスしてください
4. {min(200, 400)}文字以内で、具体的な止めるためのマイクロアクションを1つ提案してください

{tone_guidance}

結論には必ず「今送らなくてくれてありがとう」というagüardecimento（含めないでください、感じたことを形に）で終わるでください。"""
        
        return prompt

    async def validate_sos_request(
        self, user: User, db: AsyncSession
    ) -> tuple[bool, Optional[str]]:
        """
        Validate if user can make an SOS request.
        
        Args:
            user: The User object
            db: Database session
            
        Returns:
            Tuple of (is_valid, error_code)
        """
        if not user:
            return False, SOS_ERROR_CODES["INVALID_USER"]

        if user.subscription_status != "active":
            return False, SOS_ERROR_CODES["NOT_SUBSCRIBER"]

        user = await self.subscription_service.reset_sos_credits_if_needed(user, db)
        
        has_credits = await self.subscription_service.check_sos_credits(user)
        if not has_credits:
            return False, SOS_ERROR_CODES["SOS_CREDITS_EXHAUSTED"]

        return True, None

    async def process_sos_reading(
        self, user: User, db: AsyncSession, drawn_card: dict
    ) -> Reading:
        """
        Process an SOS reading request.
        
        Args:
            user: The User object
            db: Database session
            drawn_card: Dictionary with card data
            
        Returns:
            Created Reading object
        """
        is_valid, error_code = await self.validate_sos_request(user, db)
        if not is_valid:
            raise ValueError(f"SOS request validation failed: {error_code}")

        card_result = await db.execute(
            select(Card).where(Card.id == drawn_card["card_id"])
        )
        card = card_result.scalar_one_or_none()
        
        card_name = getattr(card, "name_jp", "Unknown") if card else "Unknown"
        is_reversed = drawn_card.get("is_reversed", False)
        
        prompt = self.build_panic_prompt(
            card_name, is_reversed, user.emotional_profile
        )

        from app.services.reading_service import MockLLMClient
        llm_client = MockLLMClient()
        interpretation = await llm_client.generate_text(prompt)

        reading = Reading(
            id=uuid.uuid4(),
            user_name="SOS User",
            focus_area="love",
            reading_type="sos",
            cards_drawn=[drawn_card["card_id"]],
            interpretation_text=interpretation,
            language="ja",
            llm_provider="mock",
            llm_model="mock-v1",
            summary_for_memory=f"SOS reading: {card_name}",
            user_id=user.id,
        )
        
        db.add(reading)
        
        await self.subscription_service.deduct_sos_credit(user, db)
        
        await db.commit()
        await db.refresh(reading)
        
        return reading
