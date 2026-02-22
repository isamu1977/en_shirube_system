# frontend Specification

## Purpose
TBD - created by archiving change add-reading-result-ui. Update Purpose after archive.
## Requirements
### Requirement: Reading Result Page

The system SHALL provide a dedicated page for displaying reading results at /reading/[session_id].

#### Scenario: Page loads with valid session

- **WHEN** a user navigates to /reading/{session_id} with a valid session ID
- **THEN** the page fetches reading data from the API
- **AND** displays the SpreadBoard component

#### Scenario: Page loads with invalid session

- **WHEN** a user navigates to /reading/{invalid_session_id}
- **THEN** an error message is displayed
- **AND** a link back to home is provided

### Requirement: ReadingText Markdown Rendering

The system SHALL render the LLM interpretation text as beautifully formatted Markdown.

#### Scenario: Markdown sections rendered

- **WHEN** interpretation text is provided
- **THEN** the component renders Markdown with proper headings, paragraphs, lists
- **AND** each major section has a soft background card for readability

#### Scenario: Text fades in after cards

- **WHEN** the last card flip animation completes
- **THEN** the ReadingText component fades in with a smooth transition
- **AND** uses Svelte's transition:fade directive

### Requirement: Minimalist Aesthetic

The UI SHALL follow a minimalist, elegant design suitable for the target audience (Japanese women 20-45).

#### Scenario: Design follows guidelines

- **WHEN** the reading result page is rendered
- **THEN** plenty of whitespace is used
- **AND** refined typography (Mincho fonts for Japanese) is applied
- **AND** soft transitions are used throughout

#### Scenario: No dark/heavy styling

- **WHEN** the design is rendered
- **THEN** dark, heavy, or overly occult aesthetics are avoided
- **AND** colors are soft and calming

