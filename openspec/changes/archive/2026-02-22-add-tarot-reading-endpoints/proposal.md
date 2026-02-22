# Change: Add Tarot Reading Endpoints for Romantic Relationships

## Why
We need to implement the core business logic and API endpoints for a specialized Tarot reading service targeted at romantic relationships (恋愛/復縁). This service will handle three specific spread types—Lead Magnet (1 card), Standard (7 cards), and Premium (12 cards)—catering to different user engagement and conversion tiers.

## What Changes
- **Schemas**: Add Pydantic models for `CardDraw`, `ReadingRequest`, and `ReadingResponse`.
- **Services**: Implement `ReadingService.generate_reading` to handle DB fetching for card context, specialized LLM prompting per spread type, mock LLM generation execution, and session metadata persistence.
- **Endpoints**: Create a new `/readings/generate` POST endpoint integrating the `ReadingService`.
- **Specs**: Modify `ai-interpretation` to align with the new gap technique (Lead Magnet) and structured deep-dives (Standard, Premium). Modify `ritual-flow` to define the 1, 7, and 12 card mappings for the respective spread types.

## Impact
- Affected specs: `ai-interpretation`, `ritual-flow`
- Affected code: `schemas/reading.py`, `services/reading_service.py`, `api/v1/endpoints/readings.py`
