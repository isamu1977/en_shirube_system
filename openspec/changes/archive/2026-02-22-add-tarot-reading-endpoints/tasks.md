## 1. Sub-tasks
- [x] 1.1 Create `schemas/reading.py` containing `CardDraw`, `ReadingRequest` (with dynamic validator for card counts), and `ReadingResponse`.
- [x] 1.2 Create `services/reading_service.py` to instantiate `ReadingService`.
- [x] 1.3 Implement `generate_reading` logic mapping specific card data to specific prompt instructions based on `spread_type` (Lead Magnet, Standard, Premium).
- [x] 1.4 Mock an internal `llm_client.generate_text(prompt)` method inside the service logic context.
- [x] 1.5 Implement database session persisting of generated text/session state.
- [x] 1.6 Add `api/v1/endpoints/readings.py` and mount the single POST `/readings/generate` endpoint.
