## ADDED Requirements
### Requirement: Card Component with Reversed Support

The Card component SHALL support reversed card display with proper visual rotation.

#### Scenario: Reversed card displays upside down

- **WHEN** cardData.is_reversed is true
- **THEN** the final transform applies rotationY(180deg) rotateZ(180deg)
- **AND** the card appears upside down after flipping

#### Scenario: Staggered delay prop

- **WHEN** an index prop is provided to the Card component
- **THEN** the flip animation uses a calculated delay based on index * 400ms

### Requirement: SpreadBoard Layout

The system SHALL display drawn cards in a visually pleasing layout suitable for mobile-first design.

#### Scenario: 7-card spread layout

- **WHEN** a standard reading with 7 cards is displayed
- **THEN** cards are arranged in a responsive grid/flex layout
- **AND** the layout works well on mobile screens (320px+)

#### Scenario: Tap to reveal interaction

- **WHEN** the SpreadBoard is mounted
- **THEN** cards remain unflipped until user initiates reveal
- **AND** a "Tap to Reveal" prompt is displayed

### Requirement: Staggered Card Reveal

The system SHALL reveal cards one at a time with a wave-like sequence to build emotional tension.

#### Scenario: Sequential reveal with 400ms delay

- **WHEN** reveal is triggered
- **THEN** each card flips with index * 400ms delay
- **AND** the animation uses cubic-bezier(0.4, 0.0, 0.2, 1) easing

#### Scenario: Last card completion

- **WHEN** the final card finishes its flip animation
- **THEN** a completion event is emitted for ReadingText to fade in
