# Change: Add Tarot Seed Data Payload Structure

## Why
The backend seed script (`scripts/seed_cards.py`) relies on a structured JSON payload to populate the `cards` table with 78 Tarot cards. This JSON structure must conform identically to the newly established relationship context schema, guaranteeing data consistency between Japanese interpretations, suit mapping, and emotional context orientations.

## What Changes
- Formalize the JSON payload format for `data/tarot_cards.json` to include 78 records.
- Enforce strictly typed fields: `id`, `name_jp`, `name_en`, `arcana_type`, `suit`, `number`, `meaning_upright`, `meaning_reversed`, `love_context_upright`, `love_context_reversed`.
- Establish the data source contract in the `card-management` specification.

## Impact
- Affected specs: `card-management`
- Affected code: `backend/data/tarot_cards.json` (the generation of this file is deferred to the application phase).
