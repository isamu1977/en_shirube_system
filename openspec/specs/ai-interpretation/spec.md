# ai-interpretation Specification

## Purpose
TBD - created by archiving change add-taro-de-raizes-platform. Update Purpose after archive.
## Requirements
### Requirement: Prompt Template System

The system SHALL use structured prompt templates that assemble the AI instruction from: system role, voice directives, card-specific context (from the `cards` table), focus area, language, and reading tier (free/paid).

#### Scenario: Prompt includes card grounding data

- **WHEN** an interpretation is requested for the card "the-empress"
- **THEN** the prompt sent to the LLM includes the card's `description_{lang}` and `keywords_json[lang]` data specific to the "Brazilian Roots" deck

#### Scenario: Prompt differs by tier

- **WHEN** a free-tier interpretation is requested
- **THEN** the prompt instructs the LLM to provide a 150-250 word insight using the "Gap Technique"
- **WHEN** a paid-tier interpretation is requested
- **THEN** the prompt instructs the LLM to provide a 600-1000 word structured analysis

### Requirement: Brazilian Roots Grounding

All AI interpretations SHALL be grounded exclusively in the "Brazilian Roots" card descriptions and keywords stored in the database. The AI MUST NOT use generic tarot meanings or descriptions not in the provided context.

#### Scenario: AI uses grounded context

- **WHEN** an interpretation is generated
- **THEN** the system prompt includes explicit grounding instructions: "Base your interpretation ONLY on the following card descriptions and keywords from the Tarô de Raízes tradition."

#### Scenario: AI voice quality

- **WHEN** an interpretation is generated
- **THEN** the system prompt instructs the AI to speak with a voice that is "wise, non-judgmental, warm, and culturally rich, honoring Brazilian spiritual and folk traditions."

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

### Requirement: Dual LLM Provider Support

The system SHALL support both OpenAI (GPT-4o) and Anthropic (Claude 3.5 Sonnet) as interpretation providers, selectable via environment variable, with automatic fallback to the secondary provider on failure.

#### Scenario: Primary provider succeeds

- **WHEN** the primary LLM provider is configured as `openai`
- **AND** a reading interpretation is requested
- **THEN** the system sends the prompt to GPT-4o and returns the response

#### Scenario: Primary provider fails, fallback activates

- **WHEN** the primary LLM provider returns an error (timeout, rate limit, 5xx)
- **THEN** the system automatically retries with the secondary provider
- **AND** the `readings.llm_provider` field records which provider ultimately served the request

### Requirement: Streaming Interpretation Delivery

The system SHALL support Server-Sent Events (SSE) streaming for interpretation delivery, allowing the frontend to display text progressively as the LLM generates it.

#### Scenario: Streaming enabled

- **WHEN** a `POST /api/v1/reading/interpret` request is made with `stream: true`
- **THEN** the response uses `text/event-stream` content type
- **AND** each SSE event contains a `chunk` of interpretation text
- **AND** the final event includes `done: true` and token usage metadata

#### Scenario: Non-streaming fallback

- **WHEN** a `POST /api/v1/reading/interpret` request is made with `stream: false`
- **THEN** the response returns the complete interpretation as a single JSON object

### Requirement: Token Usage Tracking

The system SHALL record the prompt token count and completion token count for each interpretation in the `readings` table.

#### Scenario: Token counts are stored

- **WHEN** an interpretation is successfully generated
- **THEN** the `readings.prompt_tokens` and `readings.completion_tokens` fields are populated
- **AND** the values match the usage data returned by the LLM API

