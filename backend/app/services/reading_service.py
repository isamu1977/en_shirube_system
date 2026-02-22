from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID

from app.schemas.reading import ReadingRequest, ReadingResponse
from app.models import Card, Reading

class MockLLMClient:
    async def generate_text(self, prompt: str) -> str:
        snippet = prompt[:150].replace('\n', ' ')
        return f"**Mocked AI Interpretation**\n\nGenerated for prompt:\n> {snippet}...\n\n*The full response would be generated here based on the instructions.*"

class ReadingService:
    def __init__(self):
        self.llm_client = MockLLMClient()

    async def generate_reading(self, request: ReadingRequest, db: AsyncSession) -> ReadingResponse:
        card_ids = [c.card_id for c in request.drawn_cards]
        result = await db.execute(select(Card).where(Card.card_number.in_(card_ids)))
        cards_db = result.scalars().all()
        cards = {c.card_number: c for c in cards_db}

        prompt = ""
        if request.spread_type == "lead_magnet":
            card = cards.get(request.drawn_cards[0].card_id)
            card_name = getattr(card, "name_en", f"Card {request.drawn_cards[0].card_id}") if card else "Unknown"
            
            prompt = (
                f"Position: His true feelings.\nCard: {card_name}\n\n"
                "Instruction: Generate a short, 2-paragraph emotional response. High empathy, creating curiosity. "
                "Do not give a final conclusion, leave a cliffhanger for the next step."
            )
        elif request.spread_type == "standard":
            positions = [
                "1: Current Situation", "2: Her Emotion", "3: His Emotion", 
                "4: The Obstacle", "5: Turning Point", "6: Next Action", "7: Probable Outcome"
            ]
            prompt = "Positions:\n"
            for i, draw in enumerate(request.drawn_cards):
                card = cards.get(draw.card_id)
                card_name = getattr(card, "name_en", f"Card {draw.card_id}") if card else "Unknown"
                prompt += f"- {positions[i]}: {card_name} {'(Reversed)' if draw.is_reversed else ''}\n"
            prompt += (
                "\nInstruction: Generate a structured, elegant reading. Use Markdown. Focus on actionable emotional clarity, "
                "avoiding cheap mysticism. Provide a concrete next step."
            )
        elif request.spread_type == "premium":
            positions = ["Past Karma", "Subconscious Blocks", "3-Phase Strategic Plan"]
            prompt = "Positions: Past Karma, Subconscious Blocks, 3-Phase Strategic Plan\n"
            for i, draw in enumerate(request.drawn_cards):
                card = cards.get(draw.card_id)
                card_name = getattr(card, "name_en", f"Card {draw.card_id}") if card else "Unknown"
                prompt += f"- Card {i+1}: {card_name} {'(Reversed)' if draw.is_reversed else ''}\n"
                
            prompt += (
                "\nInstruction: Generate an exhaustive, highly personalized psychological and strategic guide. "
                "Divide into clear sections. Tone must be of an expert emotional guide (案内人)."
            )

        content = await self.llm_client.generate_text(prompt)

        reading = Reading(
            id=request.session_id,
            user_name="Anonymous User", # Placeholder as it's not in the request
            focus_area="love", # Implicit based on the spec
            reading_type="paid" if request.spread_type in ["standard", "premium"] else "free",
            cards_drawn=[getattr(cards.get(c.card_id), "id", str(c.card_id)) for c in request.drawn_cards],
            interpretation_text=content,
            language="en",
            llm_provider="mock",
            llm_model="mock-v1"
        )
        db.add(reading)
        await db.commit()

        return ReadingResponse(
            reading_id=reading.id,
            content=content,
            spread_type=request.spread_type
        )
