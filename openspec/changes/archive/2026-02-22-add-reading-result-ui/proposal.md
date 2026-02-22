# Change: Frontend UI & Card Reveal Animation

## Why
The application lacks a complete frontend implementation for displaying reading results. The current Card.svelte exists but lacks the staggered reveal logic, reversed card handling, and integration with the SpreadBoard and ReadingText components. This is essential for delivering the ritualistic experience to users.

## What Changes

- **SpreadBoard Component**: New `src/lib/components/SpreadBoard.svelte` for 7-card layout with horseshoe/grid arrangement
- **ReadingText Component**: New `src/lib/components/ReadingText.svelte` for rendering Markdown interpretations
- **Reading Result Page**: New `src/routes/reading/[session_id]/+page.svelte` as main presentation view
- **Card Component Updates**: Enhance existing Card.svelte with reversed card support and staggered delay prop
- **Staggered Reveal Logic**: Implement wave-like card reveal sequence (400ms delay between cards)
- **Markdown Rendering**: Beautiful rendering of LLM response with soft background cards

## Impact
- Affected specs: ritual-flow (card reveal animation)
- New specs: frontend, card-animation
- Key files: `frontend/src/lib/components/Card.svelte`, `frontend/src/lib/components/SpreadBoard.svelte`, `frontend/src/lib/components/ReadingText.svelte`, `frontend/src/routes/reading/[session_id]/+page.svelte`
