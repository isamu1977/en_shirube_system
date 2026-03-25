# Change: Apply Signature Visual Strategy

## Why
The Enshirube brand needs consistent, visually striking card back designs across all touchpoints. Currently, different components use inconsistent placeholder designs (CSS gradients in library grid, broken image icons in detail pages). Using the existing `back_cover.png` as the standardized "Enshirube Standard Back" ensures brand consistency and reinforces the geometric mysticism identity.

## What Changes
- Update library index to use `back_cover.png` for unrevealed cards instead of CSS gradient placeholders
- Update card detail page to use `back_cover.png` as the fallback when images fail to load
- Add staggered wave animation to library grid when cards load
- Standardize all card components to reference the same back image

## Impact
- Affected specs: `library` (visual consistency)
- Key files: `frontend/src/routes/library/+page.svelte`, `frontend/src/routes/library/[slug]/+page.svelte`, `frontend/src/lib/components/Card.svelte`
