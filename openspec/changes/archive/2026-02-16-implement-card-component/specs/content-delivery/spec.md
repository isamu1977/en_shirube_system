## ADDED Requirements

### Requirement: Card Visual Presentation

The system SHALL render Tarot cards using a specialized `Card` component that adheres to the "Mystic Minimalism" aesthetic.

#### Scenario: Visual Styling

- **WHEN** a card is displayed
- **THEN** it must have an aspect ratio of 2:3
- **AND** it must have rounded corners (`rounded-2xl`) masking the image
- **AND** it must feature a gold border (`#D4AF37`) and elevation shadow (`shadow-xl`)

#### Scenario: Trilingual Labels

- **WHEN** a card is revealed
- **THEN** it displays the Japanese name prominently
- **AND** the Portuguese name as a secondary, elegant label

### Requirement: Card Interaction

The system SHALL support interactive states for the card, specifically "Face Down" and "Face Up" with a transition animation.

#### Scenario: Shuffle and Reveal

- **WHEN** the user completes the "shuffle" interaction
- **THEN** the card transitions from face-down to face-up
- **AND** the transition uses a 3D flip animation (`rotateY`)
