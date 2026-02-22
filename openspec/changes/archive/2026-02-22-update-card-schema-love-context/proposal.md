# Change: Update Card Schema for Orientation and Love Contexts

## Why
The backend `Card` model and the `card-management` specification currently lack explicit fields for upright/reversed meanings and specific contexts like love or relationships. To support the recently added Tarot Reading endpoints (which focus on romantic relationships) and the new seed script format, the schema must be updated to store this granular information.

## What Changes
- Add `meaning_upright` and `meaning_reversed` fields to the `cards` table.
- Add `love_context_upright` and `love_context_reversed` fields to the `cards` table.
- Update the `card-management` specification to reflect these new requirements for the 78-card deck data.

## Impact
- Affected specs: `card-management`
- Affected code: `app/models.py` (Card model), database schema (Alembic migration needed, or table recreation since it's early stage), and seed scripts (`scripts/seed_cards.py`).
