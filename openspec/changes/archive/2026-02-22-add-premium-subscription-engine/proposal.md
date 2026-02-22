# Change: Premium Subscription & Continuity Engine

## Why
The application currently lacks premium subscription management and user continuity features. Users cannot maintain context across readings, and there is no SOS panic-button feature for relationship anxiety intervention. This limits monetization opportunities and user retention.

## What Changes

- **Database Schema Updates**: Add subscription fields to `readings` table (renamed from reading_sessions), add new `users` table with Stripe integration fields, emotional profile, and SOS credits
- **Memory Engine**: New `services/memory_service.py` to fetch and inject contextual memory from previous readings into AI prompts
- **Subscription Service**: New `services/subscription_service.py` for Stripe customer management and subscription status
- **SOS Feature**: New `services/sos_service.py` for emergency 1-card readings with panic intervention prompts
- **Prompt Injection**: Modify prompt builder to include contextual memory and emotional profile for premium subscribers

## Impact
- Affected specs: database, ai-interpretation
- New specs: subscription-management, memory-engine, sos-feature
- Key files: `backend/app/models.py`, `backend/app/services/memory_service.py`, `backend/app/services/subscription_service.py`, `backend/app/services/sos_service.py`, `backend/app/services/prompt_builder.py`
