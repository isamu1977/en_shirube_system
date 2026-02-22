# api-gateway Specification

## Purpose
TBD - created by archiving change add-taro-de-raizes-platform. Update Purpose after archive.
## Requirements
### Requirement: Health Check Endpoint

The system SHALL expose a `GET /api/v1/health` endpoint that returns the health status of the application, including database connectivity and LLM API reachability.

#### Scenario: All systems healthy

- **WHEN** a `GET /api/v1/health` request is made
- **AND** the database is reachable and the LLM API responds
- **THEN** the response status is 200
- **AND** the body contains `{"status": "healthy", "db": "ok", "llm": "ok"}`

#### Scenario: Database unreachable

- **WHEN** a `GET /api/v1/health` request is made
- **AND** the database connection fails
- **THEN** the response status is 503
- **AND** the body contains `{"status": "degraded", "db": "error", "llm": "ok"}`

### Requirement: Versioned API Path

All API endpoints SHALL be served under the `/api/v1/` path prefix, enabling future API version coexistence.

#### Scenario: API version prefix

- **WHEN** any API request is made
- **THEN** the URL path begins with `/api/v1/`

### Requirement: CORS Configuration

The system SHALL configure Cross-Origin Resource Sharing (CORS) to allow requests from the SvelteKit frontend origin.

#### Scenario: CORS headers present

- **WHEN** a preflight `OPTIONS` request is sent from the frontend origin
- **THEN** the response includes `Access-Control-Allow-Origin` matching the frontend domain
- **AND** `Access-Control-Allow-Methods` includes `GET, POST, OPTIONS`

### Requirement: Request Validation

The system SHALL validate all incoming request bodies using Pydantic models and return structured error responses for invalid input.

#### Scenario: Invalid reading init request

- **WHEN** a `POST /api/v1/reading/init` request is made with `focus_area` = `invalid_value`
- **THEN** the response status is 422
- **AND** the body contains a structured error with field-level details

### Requirement: Rate Limiting

The system SHALL enforce rate limiting on the interpretation endpoint to prevent abuse, with configurable limits per IP address.

#### Scenario: Rate limit enforced

- **WHEN** a single IP address sends more than the configured limit of `POST /api/v1/reading/interpret` requests within the rate window
- **THEN** subsequent requests receive a 429 status code
- **AND** the response includes a `Retry-After` header

### Requirement: Structured Error Responses

The system SHALL return error responses in a consistent JSON format containing `error_code`, `message`, and optional `details` fields, with messages localized to the request's language where applicable.

#### Scenario: Consistent error format

- **WHEN** any API error occurs
- **THEN** the response body follows the structure: `{"error_code": "...", "message": "...", "details": [...]}`

#### Scenario: Localized error message

- **WHEN** an error occurs for a request with `language` = `ja`
- **THEN** the `message` field is in Japanese

