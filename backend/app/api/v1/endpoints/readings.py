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

@router.get("/{id}/pdf")
async def get_reading_pdf(id: str, db: AsyncSession = Depends(get_db)):
    """
    Generate and return a styled PDF document containing the reading results.
    """
    from fastapi import HTTPException
    from fastapi.responses import Response
    from app.services.pdf_service import generate_reading_pdf
    
    # 1. Fetch reading data
    reading = await reading_service.get_reading(id, db)
    if not reading:
         raise HTTPException(status_code=404, detail="Reading not found")
         
    # 2. Prepare data for Jinja2 template
    reading_data = {
        "date": reading.created_at.strftime("%Y年%m月%d日") if reading.created_at else "",
        "cards": [
            {
                "position_name": step.get("position_name", ""),
                "name_jp": step.get("card", {}).get("name_jp", ""),
                "is_reversed": step.get("reversed", False)
            } for step in reading.cards
        ] if reading.cards else [],
        "reading_html": reading.interpretation_text or ""
    }
    
    # 3. Generate PDF byte stream
    try:
        pdf_bytes = await generate_reading_pdf(reading_data)
        return Response(content=pdf_bytes, media_type="application/pdf")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to generate PDF")
