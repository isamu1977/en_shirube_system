## MODIFIED Requirements

### Requirement: 78-Card Deck Data

The system SHALL store 78 cards with standard Rider-Waite meanings and trilingual metadata. The ID format SHALL be `major_XX` for Major Arcana (00-21) and `[suit]_[rank]` for Minor Arcana (where rank is `01`-`10`, `page`, `knight`, `queen`, `king`).

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
