# content-delivery Specification

## Purpose
TBD - created by archiving change add-taro-de-raizes-platform. Update Purpose after archive.
## Requirements
### Requirement: Web Reading Display

The system SHALL display the completed reading on a dedicated results page, showing the drawn card(s) with artwork, the AI-generated interpretation text, and the user's reading metadata (name, focus area, date).

#### Scenario: Reading results page renders

- **WHEN** an interpretation is completed
- **THEN** the UI displays the card image(s), card name(s) in the user's language, and the full interpretation text
- **AND** the reading metadata (user name, focus area, date) is visible

#### Scenario: Streaming text display

- **WHEN** the interpretation is streamed via SSE
- **THEN** the interpretation text appears progressively on the page (typewriter effect)
- **AND** the user can see the text being generated in real-time

### Requirement: PDF Download

The system SHALL provide a `GET /api/v1/reading/{id}/pdf` endpoint that generates and returns a styled PDF document containing the reading results.

#### Scenario: PDF generation

- **WHEN** a `GET /api/v1/reading/{id}/pdf` request is made for a completed reading
- **THEN** the response is a PDF file (`application/pdf` content type)
- **AND** the PDF contains the card artwork, card name, interpretation text, and reading metadata
- **AND** the PDF uses the same "mystic minimalism" visual style as the web UI

#### Scenario: PDF in user's language

- **WHEN** a PDF is generated for a reading in Japanese
- **THEN** all text in the PDF (card names, interpretation, headers) is in Japanese
- **AND** the PDF uses a font that supports Japanese characters

#### Scenario: PDF for nonexistent reading

- **WHEN** a `GET /api/v1/reading/{id}/pdf` request is made with an invalid UUID
- **THEN** the response status is 404

### Requirement: Social Sharing

The system SHALL provide a shareable URL for each completed reading that includes Open Graph meta tags for rich preview on social media and messaging apps (including LINE).

#### Scenario: Shareable URL

- **WHEN** a reading is completed
- **THEN** a unique shareable URL is generated (e.g., `/reading/{id}`)
- **AND** the page at that URL is accessible without authentication

#### Scenario: OG meta tags

- **WHEN** the shareable reading URL is crawled by a social media bot
- **THEN** the page contains `og:title`, `og:description`, `og:image`, and `og:url` meta tags
- **AND** `og:title` includes the card name(s) in the reading's language
- **AND** `og:image` is the card artwork image

### Requirement: Past Reading Retrieval

The system SHALL expose a `GET /api/v1/reading/{id}` endpoint that returns the full details of a previously completed reading.

#### Scenario: Retrieve completed reading

- **WHEN** a `GET /api/v1/reading/{id}` request is made with a valid reading UUID
- **THEN** the response contains the complete reading data: cards drawn, interpretation text, language, focus area, timestamps

#### Scenario: Retrieve incomplete reading

- **WHEN** a `GET /api/v1/reading/{id}` request is made for a reading that has not yet been interpreted
- **THEN** the response includes `interpretation_text: null` and `status: awaiting_interpretation`

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

