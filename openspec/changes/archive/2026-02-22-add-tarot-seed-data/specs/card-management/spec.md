## ADDED Requirements
### Requirement: JSON Seed Data Structure
The system SHALL ingest initial card definitions from a strictly formatted JSON array located at `data/tarot_cards.json`. Each of the 78 objects MUST contain explicit fields defining its identity and psychological reading contexts.

#### Scenario: Seed object constraints
- **WHEN** the seed script reads the JSON manifest
- **THEN** it demands `id`, `name_jp`, `name_en`, `arcana_type`, `suit`, `number`, `meaning_upright`, `meaning_reversed`, `love_context_upright`, and `love_context_reversed`
- **AND** `suit` must be null for `major` arcana types
