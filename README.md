# En Shirube System (縁しるべ)

A high-end, trilingual (PT-BR, JP, EN) tarot reading web application featuring a custom 78-card "Brazilian Roots" deck with AI-powered interpretations.

## Purpose

**En Shirube** (縁しるべ) is a tarot reading platform designed for users in Japan and Brazil seeking spiritual and emotional guidance. The app delivers automated, AI-powered interpretations through a ritualistic, immersive user interface with a minimalist, elegant aesthetic targeting Japanese women aged 20-45.

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | SvelteKit + Tailwind CSS |
| Backend | FastAPI (Python 3.11+) |
| Database | PostgreSQL |
| AI | OpenAI API (GPT-4o) / Anthropic API (Claude 3.5 Sonnet) |
| PDF Generation | WeasyPrint / ReportLab |

## Project Structure

```
en-shirube-system/
├── backend/               # FastAPI backend
│   ├── app/
│   │   ├── models.py     # SQLAlchemy ORM models
│   │   ├── database.py    # Database configuration
│   │   └── services/      # Business logic
│   │       ├── draw_service.py
│   │       ├── memory_service.py
│   │       ├── prompt_builder.py
│   │       ├── reading_service.py
│   │       ├── sos_service.py
│   │       └── subscription_service.py
│   ├── scripts/           # Database scripts
│   └── tests/             # Backend tests
├── frontend/              # SvelteKit frontend
│   ├── src/
│   │   ├── lib/
│   │   │   └── components/  # UI components
│   │   │       ├── Card.svelte
│   │   │       ├── ReadingText.svelte
│   │   │       └── SpreadBoard.svelte
│   │   └── routes/       # SvelteKit routes
│   │       └── reading/[session_id]/
│   └── static/            # Static assets
├── openspec/              # Specification-driven development
│   ├── specs/            # Current specs
│   └── changes/          # Change proposals
└── images/               # Card art images
```

## Features

### Core Features

- **Trilingual Support**: PT-BR, Japanese, and English for all card names and interpretations
- **78-Card Brazilian Roots Deck**: Custom tarot deck themed with Brazilian cultural symbols
- **Ritual Flow**: Name → Focus area → Shuffle animation → Card draw → Reveal → AI interpretation
- **3D Card Reveal Animation**: Smooth CSS-based 3D flip with staggered reveal

### Reading Types

- **Lead Magnet (Free)**: 1-card reading using "Gap Technique" for lead generation
- **Standard (Paid)**: 7-card reading with deep psychological analysis
- **Premium (Paid)**: 12-card exhaustive reading with strategic guidance
- **SOS Emergency**: 1-card panic intervention for relationship anxiety

### Premium Features

- **Stripe Integration**: Subscription management for premium users
- **Contextual Memory**: Continuity across readings with LLM-generated summaries
- **Emotional Profile**: Personalized tone based on user's psychological tendency
- **SOS Credits**: Monthly emergency readings for crisis situations

## Getting Started

### Prerequisites

- Python 3.11+
- Node.js 18+
- PostgreSQL

### Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up database
python scripts/init_db.py

# Run migrations
python scripts/migrate_subscription_features.py

# Start development server
uvicorn app.main:app --reload
```

### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

### Environment Variables

Create `.env` files in both `backend/` and `frontend/` directories:

```bash
# backend/.env
DATABASE_URL=postgresql+asyncpg://user:pass@localhost:5432/en_shirube_system
STRIPE_SECRET_KEY=sk_test_...
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-...

# frontend/.env
PUBLIC_API_URL=http://localhost:8000
```

## Architecture

### Service Layer Pattern

The backend follows a service-layer pattern:

1. **Routers** (`/api/v1/`) - Handle HTTP requests
2. **Services** - Business logic
3. **Models** - Database entities

### Prompt Template System

AI prompts are built using structured templates that include:
- System role and voice directives
- Card-specific context from database
- Focus area and language settings
- Reading tier (free/paid)
- Contextual memory for premium subscribers

## Testing

```bash
# Backend tests
cd backend
python tests/services/test_memory_service.py
python tests/services/test_subscription_service.py
python tests/services/test_sos_service.py

# Frontend type checking
cd frontend
npm run check
```

## Development Workflow

1. Create a feature branch from `main`
2. Write a change proposal in `openspec/changes/`
3. Implement the changes
4. Run tests and linting
5. Create a PR for review
6. Archive the change after deployment

## Design Principles

- **Mobile-first**: Optimized for LINE browser and mobile web
- **Minimalist aesthetic**: Plenty of whitespace, refined typography (Mincho fonts)
- **Wise voice**: AI speaks as a wise, non-judgmental emotional guide
- **Cultural authenticity**: Grounded in "Brazilian Roots" tradition, not generic tarot

## License

Private - All rights reserved
