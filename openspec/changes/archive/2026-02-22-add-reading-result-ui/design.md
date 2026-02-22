## Context
This change implements the frontend presentation layer for reading results. The existing Card.svelte needs enhancement, and new SpreadBoard and ReadingText components are needed. The aesthetic must be minimalist, elegant, and calming for Japanese women 20-45.

## Goals / Non-Goals
- Goals: Complete reading result page with 3D card reveal, staggered animation, Markdown rendering
- Non-Goals: Backend API changes, database updates, user authentication flow

## Decisions

### Decision: Use CSS-based 3D Transforms
We will continue using CSS transforms for the 3D flip effect (already implemented in Card.svelte) rather than JavaScript-based animations.
- Alternative considered: JavaScript-driven 3D with Three.js
- Rationale: Simpler, better performance, sufficient for the effect

### Decision: 400ms Stagger Delay
Each card will flip with a 400ms delay between reveals.
- Alternative considered: 500ms (existing spec), 300ms (faster)
- Rationale: 400ms provides good psychological anticipation without being too slow

### Decision: Mobile-First Grid Layout
The SpreadBoard will use CSS Grid with a responsive approach that works on mobile first.
- Alternative considered: Fixed horseshoe layout
- Rationale: Better mobile experience, Japanese users primarily access via mobile

### Decision: "Tap to Reveal" Pattern
Instead of auto-playing the reveal, users will tap to start the card reveal sequence.
- Alternative considered: Auto-reveal on page load
- Rationale: Gives user control, builds anticipation, aligns with ritualistic feel

## Risks / Trade-offs
- **Risk**: Markdown rendering could be slow for long interpretations → Mitigation: Use lightweight parser (marked)
- **Risk**: Reversed card rotation might look awkward → Mitigation: Apply 180deg rotation on both Y and Z axes
- **Risk**: Animation might not work on older browsers → Mitigation: CSS fallback, progressive enhancement

## Migration Plan
1. Update existing Card.svelte with new props
2. Create new SpreadBoard component
3. Create new ReadingText component
4. Create the reading result page route
5. Test on various screen sizes

## Open Questions
- Should we support a "replay" button to flip cards back? (Future feature)
- Should we allow sharing the reading result? (Future feature)
- How to handle loading state while fetching interpretation? (Skeleton UI)
