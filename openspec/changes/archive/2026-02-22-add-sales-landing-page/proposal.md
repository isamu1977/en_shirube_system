# Change: Add Sales Landing Page

## Why
The LINE Bot lead magnet flow requires a high-converting destination page for users who complete their free 1-card reading. This Sales Landing Page (`/sales` or `/reading/start`) is the core conversion point where users choose between a 7-card standard reading and a 12-card premium reading. It must be highly empathetic, addressing the user's anxieties while offering a clear, structured psychological method (AI tarot) to resolve them.

## What Changes
- Create a new SvelteKit page at `src/routes/sales/+page.svelte` (or `/reading/start`).
- Implement a 6-section vertical flow: Hero, Problem/Empathy, Method, Pricing, Social Proof, and FAQ/Footer.
- Apply a distinctive, production-grade frontend design with soft calming colors, refined serif typography, abundant whitespace, and subtle scroll animations.
- Integrate CTA buttons that trigger Stripe Checkout for the respective reading tiers.

## Impact
- Affected specs: `frontend`
- Affected code: New SvelteKit routes and UI components for the sales funnel. Connects to existing Stripe integration.
