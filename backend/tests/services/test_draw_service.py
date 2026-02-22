import sys
import os
from dataclasses import dataclass
from typing import List

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app.services.draw_service import (
    CardDraw,
    calculate_challenge_score,
    draw_balanced_spread_7,
    get_emotional_weight,
    HARD_CARDS,
    SPREAD_7_POSITIONS,
    RETENTION_TRIGGER_TEXT,
)


@dataclass
class MockCard:
    card_number: int
    arcana_type: str
    name_jp: str


def test_hard_cards_constants():
    assert HARD_CARDS == {13, 15, 16}
    assert 13 in HARD_CARDS
    assert 15 in HARD_CARDS
    assert 16 in HARD_CARDS


def test_challenge_score_reversed_card():
    db_cards = [
        MockCard(card_number=1, arcana_type="minor", name_jp="テスト"),
    ]
    draws = [CardDraw(card_id=1, is_reversed=True)]
    
    score = calculate_challenge_score(draws, db_cards)
    
    assert score == 1


def test_challenge_score_hard_major_card():
    db_cards = [
        MockCard(card_number=13, arcana_type="major", name_jp="死神"),
    ]
    draws = [CardDraw(card_id=13, is_reversed=False)]
    
    score = calculate_challenge_score(draws, db_cards)
    
    assert score == 1


def test_challenge_score_hard_major_reversed():
    db_cards = [
        MockCard(card_number=16, arcana_type="major", name_jp="塔"),
    ]
    draws = [CardDraw(card_id=16, is_reversed=True)]
    
    score = calculate_challenge_score(draws, db_cards)
    
    assert score == 2


def test_challenge_score_multiple_cards():
    db_cards = [
        MockCard(card_number=1, arcana_type="minor", name_jp="カード1"),
        MockCard(card_number=13, arcana_type="major", name_jp="死神"),
        MockCard(card_number=16, arcana_type="major", name_jp="塔"),
    ]
    draws = [
        CardDraw(card_id=1, is_reversed=True),
        CardDraw(card_id=13, is_reversed=False),
        CardDraw(card_id=16, is_reversed=True),
    ]
    
    score = calculate_challenge_score(draws, db_cards)
    
    assert score == 4


def test_spread_7_returns_7_cards():
    db_cards = [
        MockCard(card_number=i, arcana_type="major" if i < 22 else "minor", name_jp=f"カード{i}")
        for i in range(1, 79)
    ]
    
    draws = draw_balanced_spread_7(db_cards)
    
    assert len(draws) == 7


def test_spread_7_unique_cards():
    db_cards = [
        MockCard(card_number=i, arcana_type="major" if i < 22 else "minor", name_jp=f"カード{i}")
        for i in range(1, 79)
    ]
    
    draws = draw_balanced_spread_7(db_cards)
    card_ids = [d.card_id for d in draws]
    
    assert len(set(card_ids)) == 7


def test_spread_7_challenge_score_within_limit():
    db_cards = [
        MockCard(card_number=i, arcana_type="major" if i < 22 else "minor", name_jp=f"カード{i}")
        for i in range(1, 79)
    ]
    
    for _ in range(10):
        draws = draw_balanced_spread_7(db_cards)
        score = calculate_challenge_score(draws, db_cards)
        assert score <= 3


def test_spread_7_no_zero_score():
    db_cards = [
        MockCard(card_number=i, arcana_type="major" if i < 22 else "minor", name_jp=f"カード{i}")
        for i in range(1, 79)
    ]
    
    for _ in range(10):
        draws = draw_balanced_spread_7(db_cards)
        score = calculate_challenge_score(draws, db_cards)
        if score == 0:
            assert draws[3].is_reversed == True


def test_emotional_weight_mapping():
    assert len(SPREAD_7_POSITIONS) == 7
    
    assert SPREAD_7_POSITIONS[0]["jp"] == "現在の状況"
    assert "Neutral" in SPREAD_7_POSITIONS[0]["weight"]
    
    assert SPREAD_7_POSITIONS[1]["jp"] == "彼女の感情"
    assert "Empathetic" in SPREAD_7_POSITIONS[1]["weight"]
    
    assert SPREAD_7_POSITIONS[3]["jp"] == "障害・ブロック"
    assert "Challenging" in SPREAD_7_POSITIONS[3]["weight"]
    
    assert SPREAD_7_POSITIONS[6]["jp"] == "最終結果・未来"
    assert "Lightly Positive" in SPREAD_7_POSITIONS[6]["weight"]


def test_get_emotional_weight():
    weight = get_emotional_weight(0)
    assert "Neutral" in weight
    
    weight = get_emotional_weight(6)
    assert "Lightly Positive" in weight
    
    weight = get_emotional_weight(99)
    assert weight == "Neutral."


def test_retention_trigger_text():
    assert "14日間" in RETENTION_TRIGGER_TEXT
    assert "タロットが示すエネルギー" in RETENTION_TRIGGER_TEXT


if __name__ == "__main__":
    test_hard_cards_constants()
    test_challenge_score_reversed_card()
    test_challenge_score_hard_major_card()
    test_challenge_score_hard_major_reversed()
    test_challenge_score_multiple_cards()
    test_spread_7_returns_7_cards()
    test_spread_7_unique_cards()
    test_spread_7_challenge_score_within_limit()
    test_spread_7_no_zero_score()
    test_emotional_weight_mapping()
    test_get_emotional_weight()
    test_retention_trigger_text()
    print("All tests passed!")
