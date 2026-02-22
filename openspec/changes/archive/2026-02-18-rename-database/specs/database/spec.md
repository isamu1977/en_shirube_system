# Database Configuration

## ADDED Requirements

### Requirement: Database Name

The application MUST use `en_shirube_system` as the default database name.

#### Scenario: Default Connection

Given the application is started without a specific `POSTGRES_DB` environment variable
When the database connection is initialized
Then it should connect to a database named `en_shirube_system`
