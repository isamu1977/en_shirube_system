import random
from dataclasses import dataclass
from typing import List

from app.models import Card

HARD_CARDS: set[int] = {13, 15, 16}
MAX_CHALLENGE_SCORE = 3
MAX_ITERATIONS = 100


@dataclass
class CardDraw:
    card_id: int
    is_reversed: bool


SPREAD_7_POSITIONS = [
    {"jp": "現在の状況", "en": "Current State", "weight": "Neutral. Report the facts of the energy without heavy judgment."},
    {"jp": "彼女の感情", "en": "Her Emotion", "weight": "Empathetic/Validating. Focus on validating her anxiety or hope."},
    {"jp": "彼の感情", "en": "His Emotion", "weight": "Neutral/Analytical. Explain his distance or confusion logically."},
    {"jp": "障害・ブロック", "en": "The Obstacle", "weight": "Challenging. Highlight the hard truth or the subconscious block preventing them from being together right now."},
    {"jp": "ターニングポイント", "en": "Turning Point", "weight": "Neutral/Positive. Show where the energy can shift."},
    {"jp": "次のアクション", "en": "Next Action", "weight": "Positive/Actionable. Give her one highly specific, safe action to take."},
    {"jp": "最終結果・未来", "en": "Probable Outcome", "weight": "Lightly Positive + Open-ended. Give hope, but state that energies are fluid."},
]

RETENTION_TRIGGER_TEXT = (
    "『タロットが示すエネルギーは絶対ではありません。特に行動を起こした場合、約14日間で状況や彼の心理は変化し始めます。"
    "焦らず、まずはこの2週間、今回のアドバイスを意識してみてください。』"
)


def calculate_challenge_score(draws: List[CardDraw], db_cards: List[Card]) -> int:
    score = 0
    card_map = {c.card_number: c for c in db_cards}
    
    for draw in draws:
        if draw.is_reversed:
            score += 1
        card = card_map.get(draw.card_id)
        if card and card.arcana_type == "major" and card.card_number in HARD_CARDS:
            score += 1
    
    return score


def draw_balanced_spread_7(db_cards: List[Card]) -> List[CardDraw]:
    available_card_numbers = [c.card_number for c in db_cards]
    
    for _ in range(MAX_ITERATIONS):
        selected_numbers = random.sample(available_card_numbers, 7)
        draws = [
            CardDraw(card_id=num, is_reversed=random.choice([True, False]))
            for num in selected_numbers
        ]
        
        challenge_score = calculate_challenge_score(draws, db_cards)
        
        if challenge_score > MAX_CHALLENGE_SCORE:
            continue
        
        if challenge_score == 0:
            draws[3].is_reversed = True
        
        return draws
    
    raise RuntimeError(f"Failed to generate balanced spread after {MAX_ITERATIONS} iterations")


def get_emotional_weight(position_index: int) -> str:
    if 0 <= position_index < len(SPREAD_7_POSITIONS):
        return SPREAD_7_POSITIONS[position_index]["weight"]
    return "Neutral."
