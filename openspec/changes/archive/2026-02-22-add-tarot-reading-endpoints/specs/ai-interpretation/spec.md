## MODIFIED Requirements
### Requirement: Free Tier Gap Technique
The system SHALL implement the "gap technique" for the Lead Magnet spread, providing a compelling but incomplete insight tailored to romantic context ("His true feelings") that motivates the user to seek a full analysis.

#### Scenario: Lead Magnet interpretation includes gap
- **WHEN** a lead_magnet-tier interpretation is generated
- **THEN** the interpretation provides a short, 2-paragraph emotional response
- **AND** the interpretation leaves a cliffhanger for the next step, avoiding a final conclusion

### Requirement: Paid Tier Structured Analysis
The system SHALL instruct the AI to produce structured, psychologically deep interpretations for Standard and Premium spreads focused on romantic relationships, scaling complexity with the spread tier.

#### Scenario: Standard interpretation structure
- **WHEN** a standard 7-card interpretation is generated
- **THEN** the output uses Markdown and maps cards to 7 positions (Current Situation, Her Emotion, His Emotion, Obstacle, Turning Point, Next Action, Probable Outcome)
- **AND** the tone acts as an expert emotional guide, focused on actionable emotional clarity, avoiding cheap mysticism and offering a concrete next step

#### Scenario: Premium interpretation structure
- **WHEN** a premium 12-card interpretation is generated
- **THEN** the output generates an exhaustive, highly personalized psychological timeline
- **AND** divides the reading into clear sections (Past Karma, Subconscious Blocks, 3-Phase Strategic Plan)
- **AND** the tone acts as an expert emotional guide
