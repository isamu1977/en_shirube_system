# card-management Specification

## Purpose
TBD - created by archiving change add-taro-de-raizes-platform. Update Purpose after archive.
## Requirements
### Requirement: 78-Card Deck Data
The system SHALL store 78 cards with standard Rider-Waite meanings, trilingual metadata, and explicit orientation contexts for upright/reversed meanings and love-specific scenarios. The ID format SHALL be `major_XX` for Major Arcana (00-21) and `[suit]_[rank]` for Minor Arcana (where rank is `01`-`10`, `page`, `knight`, `queen`, `king`).

#### Scenario: Image URL format
- **WHEN** a card is retrieved
- **THEN** its `image_url` field follows the pattern `/images/cards/[id].png`
- **AND** the ID component matches the card's primary key

#### Scenario: Standardized IDs
- **WHEN** the "The Fool" card is retrieved
- **THEN** its ID is `major_00`
- **WHEN** the "King of Cups" card is retrieved
- **THEN** its ID is `cups_king`

#### Scenario: Trilingual Rider-Waite Meanings
- **WHEN** a card is retrieved
- **THEN** `description_pt`, `description_jp`, and `description_en` contain standard Rider-Waite interpretations
- **AND** `keywords_json` contains accurate keywords in all three languages

#### Scenario: Orientation and Love Contexts
- **WHEN** a card is retrieved
- **THEN** the record includes `meaning_upright`, `meaning_reversed`, `love_context_upright`, and `love_context_reversed` fields detailing specific granular meanings

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

### Requirement: JSON Seed Data Structure
The system SHALL ingest initial card definitions from a strictly formatted JSON array located at `data/tarot_cards.json`. Each of the 78 objects MUST contain explicit fields defining its identity and psychological reading contexts.

#### Scenario: Seed object constraints
- **WHEN** the seed script reads the JSON manifest
- **THEN** it demands `id`, `name_jp`, `name_en`, `arcana_type`, `suit`, `number`, `meaning_upright`, `meaning_reversed`, `love_context_upright`, and `love_context_reversed`
- **AND** `suit` must be null for `major` arcana types

