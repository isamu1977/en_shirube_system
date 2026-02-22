## 1. Data Generation

- [x] 1.1 Create `scripts/generate_rider_waite_json.py` to generate the new 78-card JSON with standardized IDs and meanings
- [x] 1.2 Run the generator to overwrite `backend/seeds/cards_data.json`
- [x] 1.3 Update `backend/seed.py` to handle the new schema if necessary (schema is same, just content/IDs change)

## 2. Verification

- [x] 2.1 Verify new ID format (`major_00`, `cups_king`) in generated JSON
- [x] 2.2 Verify image URL format matches `/images/cards/[id].png`
- [x] 2.3 Verify trilingual descriptions are present and non-empty
- [x] 2.4 Re-seed database and verify strict count (78 cards)
