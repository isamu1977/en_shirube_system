## ADDED Requirements
### Requirement: Stripe Customer Integration

The system SHALL create and manage Stripe customer records to link payments with user accounts.

#### Scenario: New customer creation

- **WHEN** a user initiates their first paid reading without an existing Stripe customer ID
- **THEN** the system creates a Stripe customer record
- **AND** stores the returned stripe_customer_id in the users table

#### Scenario: Retrieve existing customer

- **WHEN** a user with an existing stripe_customer_id initiates a reading
- **THEN** the system retrieves the customer from Stripe to validate status

### Requirement: Subscription Status Management

The system SHALL track subscription status ("active", "canceled", "none") to control access to premium features.

#### Scenario: Check active subscription

- **WHEN** a user requests a premium reading
- **THEN** the system verifies subscription_status = "active"
- **AND** grants access if true, returns error if false

#### Scenario: Subscription status sync

- **WHEN** Stripe webhook is received for subscription events
- **THEN** the system updates the user's subscription_status accordingly

### Requirement: SOS Credits Initialization

Premium subscribers SHALL receive SOS credits upon subscription activation.

#### Scenario: Initial credit allocation

- **WHEN** a subscription transitions to "active" status
- **THEN** sos_credits is set to the configured monthly allowance (default: 3)
