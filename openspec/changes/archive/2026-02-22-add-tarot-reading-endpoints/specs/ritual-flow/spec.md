## MODIFIED Requirements
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
