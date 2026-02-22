## ADDED Requirements

### Requirement: 78-Card Deck Data

The system SHALL store all 78 cards of the "Brazilian Roots" tarot deck in a PostgreSQL `cards` table with the following structure: `id` (slug), `name_pt`, `name_jp`, `name_en`, `arcana_type`, `suit`, `card_number`, `image_url`, `keywords_json`, `description_pt`, `description_jp`, `description_en`, `element`, and `created_at`.

#### Scenario: Complete deck is seeded

- **WHEN** the database is initialized
- **THEN** the `cards` table contains exactly 78 records
- **AND** 22 records have `arcana_type` = `major`
- **AND** 56 records have `arcana_type` = `minor`

#### Scenario: Minor arcana suit distribution

- **WHEN** the database is queried for minor arcana cards
- **THEN** there are exactly 14 cards per suit (Wands, Cups, Swords, Pentacles)

### Requirement: Trilingual Card Metadata

Each card record SHALL contain name, keywords, and description fields in all three supported languages (PT-BR, JP, EN).

#### Scenario: Card has trilingual names

- **WHEN** the card "the-fool" is fetched
- **THEN** `name_pt`, `name_jp`, and `name_en` are all non-empty strings

#### Scenario: Keywords JSON structure

- **WHEN** the card "the-fool" is fetched
- **THEN** `keywords_json` contains keys `pt`, `jp`, and `en`
- **AND** each key maps to an array of at least 3 keyword strings

### Requirement: Card Retrieval API

The system SHALL expose a `GET /api/v1/cards` endpoint that returns all card metadata, optionally filtered by `arcana_type` or `suit`, with card names returned in the requested language.

#### Scenario: List all cards

- **WHEN** a `GET /api/v1/cards` request is made
- **THEN** the response contains 78 card objects

#### Scenario: Filter by arcana type

- **WHEN** a `GET /api/v1/cards?arcana_type=major` request is made
- **THEN** the response contains exactly 22 card objects

### Requirement: Single Card Detail API

The system SHALL expose a `GET /api/v1/cards/{slug}` endpoint that returns full card details including description and keywords in the requested language.

#### Scenario: Fetch card by slug

- **WHEN** a `GET /api/v1/cards/the-fool` request is made
- **THEN** the response contains the complete card object for "The Fool"
- **AND** the response includes `description_pt`, `description_jp`, `description_en`, and `keywords_json`

#### Scenario: Card not found

- **WHEN** a `GET /api/v1/cards/nonexistent-card` request is made
- **THEN** the response status is 404
- **AND** the response body contains an error message
