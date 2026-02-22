## Context
The application needs to integrate a new seed script (e.g., `tarot_cards.json`) that provides highly specific data for each card: basic meanings (upright/reversed) and love-specific contexts (upright/reversed). The current `Card` schema only supports generic trilingual descriptions and keywords.

## Goals / Non-Goals
- **Goals**: Extend the database schema to support orientation-based meanings (upright and reversed) and relationship-specific contexts. Ensure the `Card` SQLAlchemy model reflects these changes.
- **Non-Goals**: Altering the trilingual requirement for existing names or breaking the core 78-card logic. The new fields might be stored in a primary language first (e.g. Japanese or English) based on the seed data, but the schema should afford storing them as text.

## Decisions
- **Decision**: Add four explicit `Text` fields to the `Card` model: `meaning_upright`, `meaning_reversed`, `love_context_upright`, `love_context_reversed`.
- **Alternatives considered**: Storing the new contextual meanings inside a JSONB field (like `keywords_json`). However, since these fields are explicitly queried and used for prompt generation in specific API endpoints, having them as discrete text columns makes the model more robust and self-documenting.

## Risks / Trade-offs
- **Migration**: If the database is already populated, a schema migration (via Alembic) is required. Since the project might be in early development, we may just need to update `models.py` and run the new seed script.
