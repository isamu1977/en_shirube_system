## Context
This change introduces premium subscription features including Stripe integration, user continuity via memory injection, and an SOS panic-button feature. The system currently has no user accounts or subscription management.

## Goals / Non-Goals
- Goals: Enable premium subscriptions via Stripe, provide continuity across readings, add SOS crisis intervention feature
- Non-Goals: Full payment processing beyond Stripe checkout, user authentication system, push notifications

## Decisions

### Decision: Use Stripe Customer ID as Primary User Identifier
We will create a `users` table with Stripe customer ID as the primary link. Users are identified by their Stripe customer, enabling seamless subscription management.
- Alternative considered: Separate auth system with email/password
- Rationale: Simpler initial implementation, Stripe handles payment security

### Decision: Store Memory Summary in Readings Table
Instead of a separate memory table, we store `summary_for_memory` directly in the `readings` table. This keeps related data together and simplifies queries.
- Alternative considered: Separate memory table with user_id foreign key
- Rationale: Simpler schema, each reading naturally contains its own summary

### Decision: SOS Credits Reset Monthly
SOS credits will reset on the 1st of each month. This requires tracking the last reset date per user.
- Alternative considered: Calendar-based reset, rolling 30-day window
- Rationale: Simple implementation, predictable user experience

### Decision: Emotional Profile Updated Periodically by LLM
The user's emotional profile ("anxious", "logical", "hopeful") will be inferred by the LLM from reading content and stored in the users table.
- Alternative considered: User-selected profile, questionnaire
- Rationale: More accurate, less friction for users

## Risks / Trade-offs
- **Risk**: LLM inference of emotional profile may be inaccurate → Mitigation: Allow manual override via user settings (future)
- **Risk**: Stripe integration complexity → Mitigation: Start with basic customer creation, add webhook handling later
- **Risk**: Contextual memory could become stale → Mitigation: Include time elapsed in prompt injection

## Migration Plan
1. Create new tables/columns via Alembic migration
2. Deploy new services alongside existing code
3. Stripe integration goes live with new subscription product
4. Existing readings continue to work without memory context

## Open Questions
- How do free users transition to premium? (Stripe checkout flow TBD)
- Should emotional_profile be editable by users? (Future feature)
- What happens to SOS credits on subscription cancellation? (Retain but disable)
