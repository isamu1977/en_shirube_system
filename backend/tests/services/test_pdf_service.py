import pytest
from app.services.pdf_service import generate_reading_pdf

@pytest.mark.asyncio
async def test_generate_reading_pdf():
    # Arrange: Mock reading data
    reading_data = {
        "date": "2026年2月24日",
        "cards": [
            {"position_name": "過去", "name_jp": "愚者", "is_reversed": False},
            {"position_name": "現在", "name_jp": "魔術師", "is_reversed": True},
            {"position_name": "未来", "name_jp": "女教皇", "is_reversed": False},
        ],
        "reading_html": "<h2>鑑定結果</h2><p>これはテストの鑑定結果です。</p><blockquote>重要なアドバイスです。</blockquote>",
    }

    # Act
    pdf_bytes = await generate_reading_pdf(reading_data)

    # Assert
    assert pdf_bytes is not None
    assert isinstance(pdf_bytes, bytes)
    # Check if the output is a valid PDF (starts with %PDF)
    assert pdf_bytes.startswith(b"%PDF")
