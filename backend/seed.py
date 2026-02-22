"""
Seed script for En-Shirube System.

Reads the 78-card deck from seeds/cards_data.json and populates the
PostgreSQL `cards` table. Idempotent — uses upsert (INSERT ... ON CONFLICT
DO UPDATE) so it can be re-run safely.

Usage:
    cd backend
    source .venv/bin/activate
    python seed.py
"""

import json
import sys
from pathlib import Path

from sqlalchemy.dialects.postgresql import insert as pg_insert

# seed.py lives at backend/ root; app/ is a sibling directory
BACKEND_ROOT = Path(__file__).resolve().parent
if str(BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(BACKEND_ROOT))

from app.database import Base, sync_engine, SyncSessionLocal
from app.models import Card  # noqa: F401 — registers model with Base


SEED_FILE = BACKEND_ROOT / "seeds" / "cards_data.json"


def load_cards_json() -> list[dict]:
    """Load card data from the JSON seed file."""
    if not SEED_FILE.exists():
        print(f"ERROR: Seed file not found at {SEED_FILE}")
        sys.exit(1)

    with open(SEED_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    print(f"Loaded {len(data)} cards from {SEED_FILE.name}")
    return data


def create_tables() -> None:
    """Create all tables defined in the ORM models (if they don't exist)."""
    Base.metadata.create_all(bind=sync_engine)
    print("Database tables created (or already exist).")


def seed_cards(cards_data: list[dict]) -> None:
    """
    Upsert all cards into the database.

    Uses PostgreSQL's INSERT ... ON CONFLICT DO UPDATE to make the script
    idempotent — safe to re-run without duplicating data.
    """
    with SyncSessionLocal() as session:
        inserted = 0
        updated = 0

        for card in cards_data:
            stmt = pg_insert(Card).values(
                id=card["id"],
                name_pt=card["name_pt"],
                name_jp=card["name_jp"],
                name_en=card["name_en"],
                arcana_type=card["arcana_type"],
                suit=card.get("suit"),
                card_number=card["card_number"],
                image_url=card.get("image_url", ""),
                keywords_json=card.get("keywords_json", {}),
                description_pt=card.get("description_pt", ""),
                description_jp=card.get("description_jp", ""),
                description_en=card.get("description_en", ""),
                element=card.get("element"),
            )

            # On conflict (same slug), update all mutable fields
            stmt = stmt.on_conflict_do_update(
                index_elements=["id"],
                set_={
                    "name_pt": stmt.excluded.name_pt,
                    "name_jp": stmt.excluded.name_jp,
                    "name_en": stmt.excluded.name_en,
                    "arcana_type": stmt.excluded.arcana_type,
                    "suit": stmt.excluded.suit,
                    "card_number": stmt.excluded.card_number,
                    "image_url": stmt.excluded.image_url,
                    "keywords_json": stmt.excluded.keywords_json,
                    "description_pt": stmt.excluded.description_pt,
                    "description_jp": stmt.excluded.description_jp,
                    "description_en": stmt.excluded.description_en,
                    "element": stmt.excluded.element,
                },
            )

            result = session.execute(stmt)
            if result.rowcount == 1:
                inserted += 1
            else:
                updated += 1

        session.commit()
        print(f"Seed complete: {inserted} inserted, {updated} updated.")


def verify_seed() -> None:
    """Quick verification that the seed was successful."""
    with SyncSessionLocal() as session:
        total = session.query(Card).count()
        major = session.query(Card).filter(Card.arcana_type == "major").count()
        minor = session.query(Card).filter(Card.arcana_type == "minor").count()

        print(f"\nVerification:")
        print(f"  Total cards: {total}")
        print(f"  Major Arcana: {major}")
        print(f"  Minor Arcana: {minor}")

        if total != 78:
            print(f"  WARNING: Expected 78 cards, found {total}")
        elif major != 22:
            print(f"  WARNING: Expected 22 major arcana, found {major}")
        elif minor != 56:
            print(f"  WARNING: Expected 56 minor arcana, found {minor}")
        else:
            print("  ✓ All 78 cards seeded correctly!")


def main() -> None:
    """Main entry point for the seed script."""
    print("=" * 50)
    print("Tarô de Raízes — Database Seed Script")
    print("=" * 50)
    print()

    # Step 1: Create tables
    create_tables()

    # Step 2: Load seed data
    cards_data = load_cards_json()

    # Step 3: Upsert cards
    seed_cards(cards_data)

    # Step 4: Verify
    verify_seed()

    print()
    print("Done!")


if __name__ == "__main__":
    main()
