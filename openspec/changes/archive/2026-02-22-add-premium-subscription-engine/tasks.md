## 1. Database Schema
- [x] 1.1 Create `users` table with subscription fields (stripe_customer_id, subscription_status, sos_credits, emotional_profile)
- [x] 1.2 Add summary_for_memory field to `readings` table
- [x] 1.3 Write database migration script

## 2. Memory Engine
- [x] 2.1 Create `services/memory_service.py` with `get_contextual_memory()` function
- [x] 2.2 Implement query to fetch last reading's summary_for_memory
- [x] 2.3 Write unit tests for memory service

## 3. Subscription Service
- [x] 3.1 Create `services/subscription_service.py`
- [x] 3.2 Implement Stripe customer creation/retrieval
- [x] 3.3 Implement subscription status checking
- [x] 3.4 Implement SOS credit management
- [x] 3.5 Write unit tests for subscription service

## 4. SOS Feature
- [x] 4.1 Create `services/sos_service.py`
- [x] 4.2 Implement SOS credit validation
- [x] 4.3 Create panic intervention prompt builder
- [x] 4.4 Create SOS API endpoint (Note: Backend API not yet set up - service ready for integration)
- [x] 4.5 Write integration tests for SOS flow

## 5. Prompt Integration
- [x] 5.1 Update prompt_builder.py to inject contextual memory for subscribers
- [x] 5.2 Add emotional_profile to system prompts
- [x] 5.3 Add "evolution" logic for premium subscribers

## 6. Integration & Testing
- [x] 6.1 End-to-end test for premium reading flow
- [x] 6.2 End-to-end test for SOS flow
- [x] 6.3 Run lint and typecheck
