# Change: Responsive Editorial Footer Redesign

## Why
The current footer is a minimal single-row design that doesn't reflect the premium brand experience. A 3-column editorial footer will improve navigation, provide better user experience, and reinforce brand identity with clear visual hierarchy.

## What Changes
- Replace inline footer with a 3-column responsive grid layout
- Column 1: Brand logo, tagline, and social icons (Threads, LINE)
- Column 2: Navigation menu links
- Column 3: Support and legal links
- Bottom bar with language toggle and copyright
- Darker background (#1A1918) with increased vertical padding
- Gold accent hover states for links

## Impact
- Affected specs: `frontend` (new footer component)
- Key files: `frontend/src/routes/+layout.svelte` (inline → component)
