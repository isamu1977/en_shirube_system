# Change: Refactor Card Data Schema

## Why

The previous card data used generic "Brazilian Roots" descriptions and a placeholder image URL format.
We need to align the data with standard trilingual Rider-Waite meanings for accuracy and consistency,
and update the image URLs to a specific `/images/cards/[id].png` format as requested by the product team.
The ID format also needs standardization (e.g., `major_00`, `cups_king`).

## What Changes

- **MODIFIED** seed data structure in `open/seeds/cards_data.json`
- **MODIFIED** `Card` model ID format (to `major_XX` and `[suit]_[rank]`)
- **MODIFIED** image URL format to `/images/cards/[id].png`
- **MODIFIED** descriptions to be standard Rider-Waite interpretations in PT-BR, JP, and EN

## Impact

- Affected specs: `card-management`
- Affected code: `backend/seed.py`, `backend/seeds/cards_data.json`
- Breaking changes: Card IDs will change, requiring a database reset/reseeding.
