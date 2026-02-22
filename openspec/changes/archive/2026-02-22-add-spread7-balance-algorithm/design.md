## Context
This change introduces intelligent card selection for the Spread 7 (Standard Reading) to guarantee emotionally balanced readings in the love/reconciliation niche. The frontend currently sends drawn cards; this change adds server-side balance validation and emotional weight injection.

## Goals / Non-Goals
- Goals:
  - Implement Challenge Score algorithm to limit overly negative readings
  - Add emotional weight mapping for 7 positions to guide LLM tone
  - Add retention trigger text to encourage user action
- Non-Goals:
  - Modify existing card data model (reuse existing `Card` model)
  - Add new API endpoints (existing `/readings` endpoint reuses this logic)
  - Implement for other spreads (lead_magnet, premium) - only standard spread)

## Decisions
- **Decision**: Store hard cards as constant set in `draw_service.py`
  - Rationale: Simple, maintainable list that can be adjusted without database changes
  - Alternative: Could store in database, but list is stable and small

- **Decision**: Re-roll entire hand if Challenge Score > 3
  - Rationale: Prevents 4+ challenge cards (too negative) in single reading
  - Alternative: Could re-roll individual cards, but whole-hand reroll is simpler and faster

- **Decision**: Force reversal on Position 4 (Obstacle) if Challenge Score = 0
  - Rationale: Ensures some realism; obstacle should have tension
  - Alternative: Could pick random position, but Position 4 is semantically appropriate

## Risks / Trade-offs
- **Risk**: Infinite re-roll loop if deck composition is problematic
  - Mitigation: Add max iterations (e.g., 100) to prevent infinite loop
- **Risk**: Hard-coded emotional weights may not suit all contexts
  - Mitigation: Weights are injected as prompt guidance; LLM can interpret flexibly

## Open Questions
- Should the hard cards list (Tower, Death, Devil) be configurable via environment variable?
- Should the Challenge Score threshold (3) be configurable?
