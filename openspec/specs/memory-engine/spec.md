# memory-engine Specification

## Purpose
TBD - created by archiving change add-premium-subscription-engine. Update Purpose after archive.
## Requirements
### Requirement: Contextual Memory Retrieval

The system SHALL provide contextual memory from previous readings to maintain continuity for premium subscribers.

#### Scenario: Memory exists for user

- **WHEN** get_contextual_memory is called for a user with prior readings
- **THEN** the function returns the summary_for_memory from the most recent reading
- **AND** includes the time elapsed since that reading

#### Scenario: No prior memory

- **WHEN** get_contextual_memory is called for a user with no prior readings
- **THEN** the function returns an empty string

### Requirement: Contextual Memory Injection

The system SHALL inject contextual memory into AI prompts for premium subscribers.

#### Scenario: Premium reading with prior context

- **WHEN** a premium user requests a reading
- **THEN** the system prompt includes the contextual memory
- **AND** instructs the LLM to acknowledge the passage of time

#### Scenario: Memory drives evolution narrative

- **WHEN** contextual memory is present
- **THEN** the prompt instructs the LLM to compare new cards with past situation
- **AND** point out what energy has shifted
- **AND** end with a reflective question about personal growth

