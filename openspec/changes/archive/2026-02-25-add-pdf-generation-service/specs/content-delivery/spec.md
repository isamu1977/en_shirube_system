## MODIFIED Requirements
### Requirement: PDF Download

The system SHALL provide a `GET /api/v1/reading/{id}/pdf` endpoint that generates and returns a highly styled, premium PDF document containing the reading results.

#### Scenario: PDF generation aesthetic and structure

- **WHEN** a `GET /api/v1/reading/{id}/pdf` request is made for a completed reading
- **THEN** the response is a minimum 4-page PDF file (`application/pdf`)
- **AND** Page 1 contains the Cover with the title and date
- **AND** Page 2 contains a Spread Overview of the drawn cards
- **AND** Page 3 contains the AI Reading Content formatted for readability
- **AND** Page 4 contains the "14-Day Anchor" retention message
- **AND** the PDF utilizes a premium, editorial aesthetic with elegant typography (e.g., Noto Serif JP).
