# ritual-flow Specification

## Purpose
TBD - created by archiving change add-taro-de-raizes-platform. Update Purpose after archive.
## Requirements
### Requirement: Reading Input Collection

The system SHALL present a form to collect the user's name, focus area (Love, Career, or General), and preferred language before starting a reading.

#### Scenario: User submits reading input

- **WHEN** the user enters their name "Yui", selects focus area "Love", and language "ja"
- **AND** submits the form
- **THEN** a `POST /api/v1/reading/init` request is sent with the provided data

#### Scenario: Input validation

- **WHEN** the user submits the form with an empty name field
- **THEN** the system displays a validation error in the user's selected language
- **AND** the form is not submitted

### Requirement: Shuffle Animation

The system SHALL display a mystic "shuffling" animation after the user submits their reading input, using Svelte transitions to simulate card shuffling.

#### Scenario: Shuffle state is shown

- **WHEN** the reading input is submitted
- **THEN** the UI transitions to a shuffle animation state
- **AND** the animation runs for a minimum of 3 seconds (to build anticipation)
- **AND** the animation uses Svelte's native `transition:` directives

### Requirement: Card Draw
The system SHALL select cards from the 78-card deck based on the targeted spread type: 1 card for Lead Magnet, 7 cards for Standard, and 12 cards for Premium readings.

#### Scenario: Lead magnet reading draws 1 card
- **WHEN** a reading requests `spread_type` = `lead_magnet`
- **THEN** the exactly 1 card is drawn

#### Scenario: Standard reading draws 7 cards
- **WHEN** a reading requests `spread_type` = `standard`
- **THEN** exactly 7 cards are drawn

#### Scenario: Premium reading draws 12 cards
- **WHEN** a reading requests `spread_type` = `premium`
- **THEN** exactly 12 cards are drawn

#### Scenario: Cards are unique per reading
- **WHEN** a reading draws multiple cards
- **THEN** no card slug appears more than once in the drawn collection

#### Scenario: Random selection uses cryptographic randomness
- **WHEN** cards are selected for a reading
- **THEN** the selection uses `secrets.SystemRandom` or equivalent CSPRNG

### Requirement: Card Reveal Animation

The system SHALL display each drawn card with a 3D flip reveal animation using CSS `rotateY` transform, transitioning from the card's back face to its front face with the Brazilian Roots artwork.

#### Scenario: Single card reveal (free)

- **WHEN** the shuffle animation completes for a free reading
- **THEN** a single card is revealed with a 3D flip animation
- **AND** the card back is shown first, then rotates to reveal the card front

#### Scenario: Sequential card reveal (paid)

- **WHEN** the shuffle animation completes for a paid reading
- **THEN** three cards are revealed sequentially (Past → Present → Future)
- **AND** each card flip animation is staggered by at least 500ms

### Requirement: Reading Session Persistence

The system SHALL persist each reading session to the `readings` table with all relevant metadata including drawn cards, user info, language, and timestamps.

#### Scenario: Reading is persisted

- **WHEN** a reading session is initialized via `POST /api/v1/reading/init`
- **THEN** a new record is created in the `readings` table
- **AND** the record contains `user_name`, `focus_area`, `cards_drawn`, `language`, `reading_type`, and `created_at`

