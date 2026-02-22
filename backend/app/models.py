"""
SQLAlchemy ORM models for Tarô de Raízes.

Defines two tables as specified in the OpenSpec design:
  - cards:    78-card "Brazilian Roots" tarot deck with trilingual metadata
  - readings: User reading sessions with AI interpretation results
"""

import uuid
from datetime import datetime, timezone

from sqlalchemy import (
    ARRAY,
    DateTime,
    Integer,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Card(Base):
    """
    A single tarot card from the 78-card "Brazilian Roots" deck.

    The primary key is a human-readable slug (e.g. 'the-fool', 'ace-of-wands')
    to allow stable references across seed data, prompts, and URLs.
    """

    __tablename__ = "cards"

    # Primary key — slug identifier
    id: Mapped[str] = mapped_column(String(50), primary_key=True)

    # Trilingual card names
    name_pt: Mapped[str] = mapped_column(String(100), nullable=False)
    name_jp: Mapped[str] = mapped_column(String(100), nullable=False)
    name_en: Mapped[str] = mapped_column(String(100), nullable=False)

    # Classification
    arcana_type: Mapped[str] = mapped_column(
        String(10), nullable=False
    )  # 'major' | 'minor'
    suit: Mapped[str | None] = mapped_column(
        String(20), nullable=True
    )  # NULL for major arcana
    card_number: Mapped[int] = mapped_column(Integer, nullable=False)

    # Visual
    image_url: Mapped[str] = mapped_column(Text, nullable=False, default="")

    # Content — structured trilingual keywords
    keywords_json: Mapped[dict] = mapped_column(
        JSONB, nullable=False, default=dict
    )  # {"pt": [...], "jp": [...], "en": [...]}

    # Content — trilingual Brazilian Roots descriptions
    description_pt: Mapped[str] = mapped_column(Text, nullable=False, default="")
    description_jp: Mapped[str] = mapped_column(Text, nullable=False, default="")
    description_en: Mapped[str] = mapped_column(Text, nullable=False, default="")

    # Orientation and Love Contexts
    meaning_upright: Mapped[str | None] = mapped_column(Text, nullable=True)
    meaning_reversed: Mapped[str | None] = mapped_column(Text, nullable=True)
    love_context_upright: Mapped[str | None] = mapped_column(Text, nullable=True)
    love_context_reversed: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Metadata
    element: Mapped[str | None] = mapped_column(
        String(20), nullable=True
    )  # Fire, Water, Earth, Air
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )

    def __repr__(self) -> str:
        return f"<Card(id='{self.id}', name_en='{self.name_en}', arcana='{self.arcana_type}')>"


class Reading(Base):
    """
    A tarot reading session.

    Captures the user's input, drawn cards, AI interpretation result,
    and LLM usage metadata.
    """

    __tablename__ = "readings"

    # Primary key — UUID
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )

    # User input
    user_name: Mapped[str] = mapped_column(String(100), nullable=False)
    focus_area: Mapped[str] = mapped_column(
        String(20), nullable=False
    )  # 'love' | 'career' | 'general'
    reading_type: Mapped[str] = mapped_column(
        String(10), nullable=False
    )  # 'free' | 'paid'

    # Drawn cards — array of card slugs
    cards_drawn: Mapped[list[str]] = mapped_column(
        ARRAY(String(50)), nullable=False
    )

    # AI interpretation result
    interpretation_text: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Language of the reading
    language: Mapped[str] = mapped_column(
        String(5), nullable=False
    )  # 'pt-br' | 'ja' | 'en'

    # LLM usage metadata
    llm_provider: Mapped[str | None] = mapped_column(
        String(20), nullable=True
    )  # 'openai' | 'anthropic'
    llm_model: Mapped[str | None] = mapped_column(String(50), nullable=True)
    prompt_tokens: Mapped[int | None] = mapped_column(Integer, nullable=True)
    completion_tokens: Mapped[int | None] = mapped_column(Integer, nullable=True)

    # Timestamps
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )

    def __repr__(self) -> str:
        return (
            f"<Reading(id='{self.id}', user='{self.user_name}', "
            f"type='{self.reading_type}', lang='{self.language}')>"
        )
