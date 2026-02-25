## 1. Scaffold & Template Design
- [ ] 1.1 Create `backend/app/templates/reading_report.html` with basic HTML5 boilerplate and Jinja2 variables.
- [ ] 1.2 Implement the CSS block including `@page` A4 formatting, Japanese web fonts, off-white background (`#FAF9F6`), and soft dark grey text (`#333333`).
- [ ] 1.3 Design Page 1 (Cover): Add the title, date, and welcome message.
- [ ] 1.4 Design Page 2 (Overview): Add the grid/list displaying drawn cards with position and orientation.
- [ ] 1.5 Design Page 3 (Reading): Render the Markdown-derived HTML with generous line height and blockquotes.
- [ ] 1.6 Design Page 4 (14-Day Anchor): Add the retention message and LINE/Subscription link.

## 2. Backend Service Logic
- [ ] 2.1 Install the chosen PDF generation library (`playwright` or `weasyprint`) and add it to `requirements.txt` / `pyproject.toml`.
- [ ] 2.2 Create `backend/app/services/pdf_service.py` with `generate_reading_pdf(reading_data: dict) -> bytes`.
- [ ] 2.3 Implement Jinja2 template rendering within `pdf_service.py`.
- [ ] 2.4 Implement the asynchronous HTML-to-PDF conversion logic.

## 3. Integration & Testing
- [ ] 3.1 Update the reading retrieval endpoint (e.g., `GET /api/v1/reading/{id}/pdf`) to utilize `generate_reading_pdf()`.
- [ ] 3.2 Add unit/integration tests for `pdf_service.py` verifying template rendering and PDF byte output.
- [ ] 3.3 Verify Japanese font rendering and layout integrity in a strictly A4 output format.
