# Change: Add Tarô de Raízes Platform

## Why

Users in Japan and Brazil need a culturally-rich, AI-powered tarot reading platform that
bridges Brazilian spiritual traditions with modern technology. No existing solution offers
trilingual (PT-BR, JP, EN) tarot interpretations grounded in Brazilian cultural symbolism
with a premium, ritualistic UX.

## What Changes

- **NEW** Trilingual engine for UI text and AI interpretation language routing
- **NEW** 78-card "Brazilian Roots" deck data model with trilingual metadata
- **NEW** Ritualistic reading flow: input → shuffle → draw → reveal → interpret
- **NEW** AI interpretation pipeline using GPT-4o/Claude 3.5 Sonnet with prompt engineering
- **NEW** Content delivery system with web display and PDF share/download
- **NEW** RESTful API gateway (`/api/v1/`) for all client-server interactions
- **NEW** PostgreSQL schema for cards, readings, and user session data
- **NEW** SvelteKit frontend with Tailwind CSS and mystic minimalism design system

## Impact

- Affected specs: `trilingual-engine`, `card-management`, `ritual-flow`, `ai-interpretation`, `content-delivery`, `api-gateway`
- Affected code: Entire codebase (greenfield)
- Breaking changes: None (new project)
- Dependencies: OpenAI/Anthropic API keys, PostgreSQL instance, CDN for card images
