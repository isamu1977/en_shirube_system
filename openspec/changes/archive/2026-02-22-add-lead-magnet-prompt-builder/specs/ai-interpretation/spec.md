## MODIFIED Requirements
### Requirement: Free Tier Gap Technique
The system SHALL implement the "gap technique" for the Lead Magnet spread, providing a compelling but incomplete insight tailored to romantic context ("His true feelings") that motivates the user to seek a full analysis.

#### Scenario: Lead Magnet prompt enforces strict rules
- **WHEN** a lead_magnet-tier interpretation is generated
- **THEN** the prompt instructs the AI to adopt the persona of an exclusive AI guide ("縁しるべ"の専属AI案内人) avoiding cheap occultism
- **AND** the prompt enforces a strict strict 200-300 character limit
- **AND** the prompt mandates an opening that points out the target's explicit psychological state
- **AND** the prompt forbids any final conclusions about the relationship
- **AND** the prompt mandates a cliffhanger ending hinting at hidden feelings or unrevealed obstacles
- **AND** the prompt provides the structured `love_context` data to the LLM
