## Context
The platform is introducing highly tailored spreading techniques focused entirely on romantic relationships (恋愛/復縁) across 3 tiers:
- Lead Magnet (1 card)
- Standard (7 cards)
- Premium (12 cards)

## Goals / Non-Goals
- **Goals**: Create robust backend routing, schema validation, and specialized prompt architectures handling the various spread types.
- **Non-Goals**: Frontend integration, immediate live LLM provider connections (a mocked LLM invocation is sufficient for initial scaffolding).

## Decisions
- **Decision**: Encapsulate the spread selection and inputs cleanly into a single generic `/readings/generate` endpoint consuming a `ReadingRequest` model.
- **Alternatives considered**: Creating disparate endpoints per spread (e.g., `/readings/standard`), but standardizing it through `ReadingRequest.spread_type` prevents code repetition and keeps routing simple.

## Risks / Trade-offs
- **Complex LLM Prompts (12 cards)**: Large prompts might hit token limits or degrade generation speed.
  - **Mitigation**: Future implementations will offload this complexity via SSE streaming and careful prompt chunking. We start with rigorous mock testing for these scenarios.
