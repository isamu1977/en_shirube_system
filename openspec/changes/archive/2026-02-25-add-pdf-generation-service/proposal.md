# Change: Add PDF Generation Service

## Why
The Tarot of Roots platform currently delivers AI-generated readings via the web UI. To enhance the premium feel of the service and provide users with a lasting, beautiful artifact of their reading, we need a service to generate highly styled, editorial-quality PDF reports. This will act as a valuable takeaway and encourage retention through the 14-day anchor approach.

## What Changes
- Create a new FastAPI service `services/pdf_service.py` to handle PDF generation.
- Design an elegant HTML template `templates/reading_report.html` using Jinja2 with an editorial, minimalist aesthetic.
- Implement a 4-page PDF layout including the Cover, Spread Overview, Reading Content, and 14-Day Anchor.
- Use Playwright (Async) or WeasyPrint for robust HTML+CSS to PDF conversion supporting Japanese fonts.
- Integrate the PDF generation with the existing `GET /api/v1/reading/{id}/pdf` endpoint conceptually defined in `content-delivery`.

## Impact
- Affected specs: `content-delivery`
- Affected code: `backend/app/services/pdf_service.py`, `backend/app/templates/reading_report.html`, and potentially PDF storage logic.
