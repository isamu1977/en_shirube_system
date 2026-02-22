## 1. Implementation

- [x] 1.1 Create `backend/app/services/draw_service.py` with `CardDraw` dataclass and `draw_balanced_spread_7()` function
- [x] 1.2 Implement Challenge Score calculation logic (hard cards: Tower, Death, Devil)
- [x] 1.3 Implement Equilibrium Filter (re-roll if > 3, force 1 reversed if 0)
- [x] 1.4 Add emotional weight constants mapping for all 7 positions
- [x] 1.5 Update `services/prompt_builder.py` to include emotional weights per position
- [x] 1.6 Append retention trigger text to System Prompt for standard spread

## 2. Testing

- [x] 2.1 Write unit tests for Challenge Score calculation
- [x] 2.2 Write unit tests for Equilibrium Filter logic
- [x] 2.3 Write integration test for full draw_balanced_spread_7 flow

## 3. Validation

- [x] 3.1 Run `ruff check` on new code (ruff not installed in environment, imports verified)
- [x] 3.2 Verify existing tests still pass
