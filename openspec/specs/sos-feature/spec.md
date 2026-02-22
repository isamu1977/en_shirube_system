# sos-feature Specification

## Purpose
TBD - created by archiving change add-premium-subscription-engine. Update Purpose after archive.
## Requirements
### Requirement: SOS Credit Validation

The system SHALL validate that users have available SOS credits before allowing emergency readings.

#### Scenario: Sufficient credits

- **WHEN** a user requests an SOS reading with sos_credits > 0
- **THEN** the request proceeds
- **AND** credits are deducted after completion

#### Scenario: Insufficient credits

- **WHEN** a user requests an SOS reading with sos_credits = 0
- **THEN** the request is rejected with error code "SOS_CREDITS_EXHAUSTED"
- **AND** the user is directed to upgrade or wait for monthly reset

### Requirement: SOS Single Card Reading

The SOS feature SHALL provide a fast, single-card reading focused on immediate grounding.

#### Scenario: SOS card draw

- **WHEN** an SOS reading is initiated
- **THEN** exactly 1 card is drawn
- **AND** the reading_type is set to "sos"

### Requirement: Panic Intervention Prompt

The system SHALL use a specialized prompt for SOS readings focused on immediate emotional grounding.

#### Scenario: SOS prompt injection

- **WHEN** an SOS reading interpretation is generated
- **THEN** the prompt instructs the LLM to provide immediate grounding
- **AND** offer a logical perspective on the situation
- **AND** suggest a specific micro-action to prevent impulsive communication

### Requirement: SOS Credit Deduction

The system SHALL deduct 1 SOS credit after each SOS reading is completed.

#### Scenario: Credit deducted after reading

- **WHEN** an SOS reading is successfully completed
- **THEN** sos_credits is decremented by 1
- **AND** the updated value is persisted to the database

