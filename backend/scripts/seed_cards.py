import asyncio
import json
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
import sys
import os

# Adjust import according to the project structure
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.models import Card

# Ideally this should be imported from app.database, but using the user provided structure
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://postgres:postgres@localhost:5432/en_shirube_system",
)
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def seed_data():
    try:
        # Adjusted path based on typical execution from backend root
        file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'tarot_cards.json')
        with open(file_path, 'r', encoding='utf-8') as f:
            cards_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return

    async with AsyncSessionLocal() as session:
        # Check if cards exist
        result = await session.execute(text("SELECT COUNT(*) FROM cards"))
        count = result.scalar()
        
        if count > 0:
            print(f"Database already has {count} cards. Seed aborted.")
            return

        print("Starting insertion of 78 cards...")
        for card_data in cards_data:
            new_card = Card(
                # ID and required fields for the new schema
                id=card_data.get('id', f"{card_data.get('arcana_type')}_{card_data.get('number')}"),
                name_pt=card_data.get('name_pt', card_data.get('name_en', '')),
                name_en=card_data.get('name_en', ''),
                name_jp=card_data.get('name_jp', ''),
                arcana_type=card_data['arcana_type'],
                suit=card_data.get('suit'),
                card_number=card_data['number'],
                # Assuming empty defaults for image_url if not provided
                image_url=card_data.get('image_url', ''),
                meaning_upright=card_data.get('meaning_upright'),
                meaning_reversed=card_data.get('meaning_reversed'),
                love_context_upright=card_data.get('love_context_upright'),
                love_context_reversed=card_data.get('love_context_reversed')
            )
            session.add(new_card)
        
        await session.commit()
        print("Seed completed successfully! 78 cards inserted.")

if __name__ == "__main__":
    asyncio.run(seed_data())
