# Change: Implement Card Component

## Why

Users need a visual and interactive way to view Tarot cards that aligns with the "mystic minimalism" aesthetic. The current system has backend data but no frontend visualization. We need a high-quality Svelte component to render the cards with specific styling (gold border, masking) and behaviors (3D flip).

## What Changes

- **NEW** SvelteKit project initialization (if missing) at `frontend/`
- **NEW** `Card.svelte` component with:
  - 3D Flip animation
  - Visual masking (rounded corners, aspect ratio 2/3)
  - Trilingual display priority (JP primary, PT secondary)
- **NEW** Asset structure in `frontend/static/images/cards/`
- **MODIFIED** `content-delivery` spec to include specific UI rendering requirements

## Impact

- **Affected Specs**: `content-delivery`
- **New Tech**: SvelteKit, Tailwind CSS
- **Visuals**: Establishes the core aesthetic of the digital card.
