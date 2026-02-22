# Project Context

## Purpose

**Tarô de Raízes** ("Tarot of Roots") is a high-end, trilingual (PT-BR, JP, EN) tarot reading web application.
It uses a custom 78-card "Brazilian Roots" deck and delivers automated, AI-powered interpretations
through a ritualistic, immersive user interface. The platform is designed to serve users in Japan and Brazil
seeking spiritual and emotional guidance.

## Tech Stack

- **Frontend:** SvelteKit + Tailwind CSS (native Svelte transitions for ritualistic animations)
- **Backend:** FastAPI (Python 3.11+) — async-first, high-performance API
- **Database:** PostgreSQL (relational: cards, users, reading logs)
- **AI Integration:** OpenAI API (GPT-4o) or Anthropic API (Claude 3.5 Sonnet) for interpretations
- **PDF Generation:** Server-side PDF library (e.g., WeasyPrint or ReportLab)
- **Deployment:** Docker-based, targeting cloud-native environments

## Project Conventions

### Code Style

- **Python:** PEP 8, type hints required, `ruff` for linting/formatting
- **Svelte/JS:** ESLint + Prettier, `.svelte` single-file components
- **Naming:** kebab-case for files, snake_case for Python, camelCase for JS/TS

### Architecture Patterns

- RESTful API with versioned endpoints (`/api/v1/`)
- Service-layer pattern in FastAPI (routers → services → repositories)
- Component-driven frontend with Svelte stores for state
- Prompt templates stored as structured data, not hardcoded strings

### Testing Strategy

- Backend: `pytest` with `httpx.AsyncClient` for integration tests
- Frontend: Vitest + Svelte Testing Library for unit tests
- E2E: Playwright for critical user flows

### Git Workflow

- Feature branches from `main`, PR-based merge
- Conventional commits (`feat:`, `fix:`, `docs:`, `chore:`)

## Domain Context

- **78-card deck:** 22 Major Arcana + 56 Minor Arcana (Wands, Cups, Swords, Pentacles)
- **Brazilian Roots theme:** Each card is re-themed with Brazilian cultural symbols, folklore, and nature
- **Trilingual:** All card names, keywords, and AI interpretations in PT-BR, Japanese, and English
- **Ritual flow:** Name → Focus area → Shuffle animation → Card draw → Reveal → AI interpretation
- **Free vs Paid tiers:** Free = 1-card + short insight (gap technique); Paid = 3-card + deep analysis

## Important Constraints

- AI prompts MUST be grounded in the "Brazilian Roots" descriptions — no generic tarot
- The "voice" of the tarot must be wise, non-judgmental, and culturally rich
- Mobile-first design, optimized for LINE browser and mobile web
- LGPD / APPI / GDPR awareness for user data handling

## External Dependencies

- OpenAI API (GPT-4o) or Anthropic API (Claude 3.5 Sonnet) — LLM provider
- PostgreSQL — primary data store
- CDN — card art image delivery
