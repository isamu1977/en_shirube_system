from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.reading import ReadingRequest, ReadingResponse
from app.services.reading_service import ReadingService
from app.database import get_db

router = APIRouter()
reading_service = ReadingService()

@router.post("/generate", response_model=ReadingResponse)
async def generate_reading(request: ReadingRequest, db: AsyncSession = Depends(get_db)):
    """
    Generate a Tarot reading interpretation.
    Supports 'lead_magnet' (1 card), 'standard' (7 cards), and 'premium' (12 cards).
    """
    return await reading_service.generate_reading(request, db)
