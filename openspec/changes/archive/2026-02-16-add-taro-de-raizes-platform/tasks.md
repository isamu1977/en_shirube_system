## 1. Project Foundation

- [x] 1.1 Initialize SvelteKit project with Tailwind CSS
- [x] 1.2 Initialize FastAPI project with async SQLAlchemy + Alembic
- [x] 1.3 Configure PostgreSQL database and create initial migration
- [x] 1.4 Set up Docker Compose for local development (frontend, backend, db)
- [x] 1.5 Configure environment variables (.env) for LLM keys, DB connection

## 2. Data Layer

- [x] 2.1 Create `cards` table schema and Alembic migration
- [x] 2.2 Create `readings` table schema and Alembic migration
- [x] 2.3 Seed database with all 78 "Brazilian Roots" card records (trilingual)
- [x] 2.4 Create SQLAlchemy models (`Card`, `Reading`)
- [x] 2.5 Create Pydantic schemas for API request/response validation

## 3. Card Management API

- [x] 3.1 Implement `GET /api/v1/cards` — list all cards with language filter
- [x] 3.2 Implement `GET /api/v1/cards/{slug}` — single card detail
- [x] 3.3 Write integration tests for card endpoints
  - Validate: `pytest tests/api/test_cards.py -v`

## 4. Trilingual Engine

- [x] 4.1 Create i18n JSON files for UI strings (pt-br, ja, en)
- [x] 4.2 Implement Svelte i18n store with language switching
- [x] 4.3 Implement language-aware card name rendering in API responses
- [x] 4.4 Write tests for language routing logic
  - Validate: `pytest tests/services/test_i18n.py -v`

## 5. Ritual Flow — Backend

- [x] 5.1 Implement `POST /api/v1/reading/init` — session creation + card draw
- [x] 5.2 Implement card shuffling logic (cryptographic random selection)
- [x] 5.3 Write integration tests for reading initialization
  - Validate: `pytest tests/api/test_reading.py -v`

## 6. AI Interpretation Pipeline

- [x] 6.1 Create prompt template system (YAML-based, per-tier, per-language)
- [x] 6.2 Implement `LLMClient` interface with OpenAI and Anthropic adapters
- [x] 6.3 Implement prompt builder (card context + focus area + tier + language)
- [x] 6.4 Implement `POST /api/v1/reading/interpret` with SSE streaming
- [x] 6.5 Add dual-provider fallback logic
- [x] 6.6 Write integration tests for interpretation pipeline
  - Validate: `pytest tests/api/test_interpret.py -v` (with mocked LLM)

## 7. Frontend — Ritual Flow UI

- [x] 7.1 Create landing/input page (name, focus area, language selection)
- [x] 7.2 Implement shuffle animation (Svelte transitions, card fanning/spinning)
- [x] 7.3 Implement card reveal with 3D flip animation (`rotateY`)
- [x] 7.4 Implement interpretation display with streaming text effect
- [x] 7.5 Build responsive layout (mobile-first, LINE browser compatible)

## 8. Frontend — Design System

- [x] 8.1 Configure Tailwind with mystic minimalism theme tokens
- [x] 8.2 Create reusable card component (front/back with flip)
- [x] 8.3 Create loading/ritual transition components
- [x] 8.4 Implement typography system (Cormorant Garamond + Inter)
- [x] 8.5 Write Vitest component tests for card and layout components
  - Validate: `npm run test -- --run`

## 9. Content Delivery

- [x] 9.1 Implement `GET /api/v1/reading/{id}` — retrieve past reading
- [x] 9.2 Implement `GET /api/v1/reading/{id}/pdf` — PDF generation
- [x] 9.3 Create shareable reading result page with OG meta tags
- [x] 9.4 Write integration tests for PDF endpoint
  - Validate: `pytest tests/api/test_pdf.py -v`

## 10. Health & Observability

- [x] 10.1 Implement `GET /api/v1/health` with DB and LLM connectivity checks
- [x] 10.2 Add structured logging (JSON format)
- [x] 10.3 Add token usage tracking per reading

## 11. End-to-End Validation

- [x] 11.1 Write Playwright E2E test for complete ritual flow
  - Validate: `npx playwright test tests/e2e/ritual-flow.spec.ts`
- [x] 11.2 Manual testing on mobile viewport (375px) and LINE browser
- [x] 11.3 Validate trilingual rendering across all three languages
