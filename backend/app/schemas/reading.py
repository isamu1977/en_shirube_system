from pydantic import BaseModel, ConfigDict, Field, field_validator, ValidationInfo
from typing import List, Literal, Optional
from uuid import UUID

class CardDraw(BaseModel):
    card_id: int
    is_reversed: bool

class ReadingRequest(BaseModel):
    session_id: UUID
    spread_type: Literal["lead_magnet", "standard", "premium"]
    drawn_cards: List[CardDraw]

    @field_validator("drawn_cards")
    @classmethod
    def validate_card_count(cls, v: List[CardDraw], info: ValidationInfo) -> List[CardDraw]:
        spread = info.data.get("spread_type")
        if spread == "lead_magnet" and len(v) != 1:
            raise ValueError("Lead magnet must have exactly 1 card")
        if spread == "standard" and len(v) != 7:
            raise ValueError("Standard spread must have exactly 7 cards")
        if spread == "premium" and len(v) != 12:
            raise ValueError("Premium spread must have exactly 12 cards")
        return v
    
    model_config = ConfigDict(from_attributes=True)

class ReadingResponse(BaseModel):
    reading_id: UUID
    content: str
    spread_type: str
