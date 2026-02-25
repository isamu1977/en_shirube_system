import logging
import os
from jinja2 import Environment, FileSystemLoader
from playwright.async_api import async_playwright

logger = logging.getLogger(__name__)

# Setup Jinja2 Environment
templates_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates")
env = Environment(loader=FileSystemLoader(templates_dir))

async def generate_reading_pdf(reading_data: dict) -> bytes:
    """
    Generates a PDF from reading_data dict.
    reading_data should contain:
    - date: string (e.g. "2026年2月24日")
    - cards: list of dicts with (position_name, name_jp, is_reversed)
    - reading_html: string of rendered markdown for the reading
    """
    try:
        # 1. Render HTML Template
        template = env.get_template("reading_report.html")
        rendered_html = template.render(
            date=reading_data.get("date", ""),
            cards=reading_data.get("cards", []),
            reading_html=reading_data.get("reading_html", "")
        )

        # 2. Convert to PDF using Playwright
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            
            # Load the HTML content
            await page.set_content(rendered_html)
            
            # Ensure fonts are loaded before generating PDF
            await page.evaluate("document.fonts.ready")
            
            # Generate the PDF
            pdf_bytes = await page.pdf(
                format="A4",
                print_background=True,
                margin={"top": "0", "right": "0", "bottom": "0", "left": "0"} 
                # Margins are handled by CSS @page in the template, so we set browser margins to 0.
            )
            
            await browser.close()
            return pdf_bytes

    except Exception as e:
        logger.error(f"Failed to generate PDF: {e}")
        raise e
