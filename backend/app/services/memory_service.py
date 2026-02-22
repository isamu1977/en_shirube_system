"""
Memory Service - Contextual memory retrieval for premium subscribers.

Provides functionality to fetch and format contextual memory from previous
readings to maintain continuity in AI-generated interpretations.
"""

import uuid
from datetime import datetime, timezone

from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Reading


class MemoryService:
    """Service for managing contextual memory across readings."""

    async def get_contextual_memory(
        self, user_id: uuid.UUID, db: AsyncSession
    ) -> str:
        """
        Fetch contextual memory from the user's most recent reading.
        
        Args:
            user_id: The UUID of the user
            db: Database session
            
        Returns:
            A formatted string containing the previous reading summary
            and time elapsed, or empty string if no prior reading exists
        """
        result = await db.execute(
            select(Reading)
            .where(Reading.user_id == user_id)
            .where(Reading.summary_for_memory.isnot(None))
            .order_by(desc(Reading.created_at))
            .limit(1)
        )
        last_reading = result.scalar_one_or_none()

        if not last_reading or not last_reading.summary_for_memory:
            return ""

        time_elapsed = self._calculate_time_elapsed(last_reading.created_at)
        
        return f"({time_elapsed}) {last_reading.summary_for_memory}"

    def _calculate_time_elapsed(self, past_datetime: datetime) -> str:
        """
        Calculate human-readable time since past datetime.
        
        Args:
            past_datetime: The datetime to compare against
            
        Returns:
            A Japanese-formatted time string (e.g., "2週間前")
        """
        now = datetime.now(timezone.utc)
        if past_datetime.tzinfo is None:
            past_datetime = past_datetime.replace(tzinfo=timezone.utc)
            
        delta = now - past_datetime
        days = delta.days

        if days == 0:
            return "今日"
        elif days == 1:
            return "昨日"
        elif days < 7:
            return f"{days}日前"
        elif days < 14:
            return "1週間前"
        elif days < 30:
            weeks = days // 7
            return f"{weeks}週間前"
        elif days < 60:
            return "1ヶ月前"
        elif days < 365:
            months = days // 30
            return f"{months}ヶ月前"
        else:
            years = days // 365
            return f"{years}年前"

    async def save_memory_summary(
        self, reading_id: uuid.UUID, summary: str, db: AsyncSession
    ) -> None:
        """
        Save a memory summary to an existing reading.
        
        Args:
            reading_id: The UUID of the reading
            summary: The LLM-generated summary for memory
            db: Database session
        """
        result = await db.execute(
            select(Reading).where(Reading.id == reading_id)
        )
        reading = result.scalar_one_or_none()
        
        if reading:
            reading.summary_for_memory = summary
            await db.commit()
