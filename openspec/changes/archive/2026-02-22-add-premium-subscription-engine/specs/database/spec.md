## MODIFIED Requirements
### Requirement: Database Name

The application MUST use `en_shirube_system` as the default database name.

#### Scenario: Default Connection

Given the application is started without a specific `POSTGRES_DB` environment variable
When the database connection is initialized
Then it should connect to a database named `en_shirube_system`

## ADDED Requirements
### Requirement: Users Table

The system SHALL store user information including subscription status and Stripe integration data in a `users` table.

#### Scenario: User record creation

- **WHEN** a new user initiates their first paid reading
- **THEN** a user record is created with stripe_customer_id, subscription_status = "none", sos_credits = 0, and emotional_profile = null

#### Scenario: Subscription activated

- **WHEN** Stripe webhook receives subscription.created event
- **THEN** the user's subscription_status is updated to "active"
- **AND** sos_credits is set to the configured monthly allowance (default: 3)

#### Scenario: Subscription canceled

- **WHEN** Stripe webhook receives subscription.deleted or subscription.canceled event
- **THEN** the user's subscription_status is updated to "canceled"
- **AND** existing sos_credits are retained but not replenished

### Requirement: Emotional Profile Tracking

The system SHALL store an emotional profile per user that reflects their psychological tendency, to be used in prompt injection for personalized readings.

#### Scenario: Emotional profile updated

- **WHEN** a reading interpretation is generated for a premium user
- **THEN** the LLM may suggest an emotional_profile update based on the reading content
- **AND** if suggested, the profile is stored in the users table

### Requirement: SOS Credits Management

Premium subscribers SHALL receive monthly SOS credits that can be used for emergency readings.

#### Scenario: Monthly credit reset

- **WHEN** a subscriber's subscription has been active for 30 days
- **THEN** sos_credits is reset to the monthly allowance

#### Scenario: SOS credit deducted

- **WHEN** an SOS reading is completed
- **THEN** sos_credits is decremented by 1
- **AND** if sos_credits reaches 0, subsequent SOS requests are rejected

### Requirement: Reading Summary for Memory

The system SHALL store a 2-sentence LLM-generated summary of each reading to provide context for future readings.

#### Scenario: Summary stored

- **WHEN** a reading interpretation is completed
- **THEN** a summary_for_memory field is populated with a concise 2-sentence summary
- **AND** this summary is stored in the same reading record
