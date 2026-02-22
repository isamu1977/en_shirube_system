## Context
The lead magnet is the most critical conversion point in the application. The prompt governing the 1-card AI reading needs strict guardrails so the LLM does not over-explain or provide false closures, which would ruin the upsell potential.

## Goals / Non-Goals
- **Goals**: Create an isolated function dedicated to constructing the LLM prompt for the Lead Magnet. Enforce character limits, tone restrictions, and the cliffhanger requirement.
- **Non-Goals**: Altering the actual LLM client interface or modifying how the 7-card or 12-card prompts work (for now).

## Decisions
- **Decision**: The prompt template will be hardcoded in Japanese within `services/prompt_builder.py` to ensure exact nuance and formatting.
- **Decision**: The `build_lead_magnet_prompt` function will accept `card_name_jp`, `is_reversed`, and `love_context` directly, keeping the builder decoupled from the database model itself but perfectly aligned with the seed data structure.

## Risks / Trade-offs
- **LLM Compliance**: LLMs sometimes ignore character limits or fail to leave cliffhangers if they try to be helpful. 
  - **Mitigation**: The system prompt rules are extremely strict and explicitly forbid conclusions. We use Anthropic/OpenAI's latest models which follow formatting instructions closely.
