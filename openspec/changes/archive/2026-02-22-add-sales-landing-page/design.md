## Context
The Sales Landing Page is the primary revenue driver connecting the free LINE Bot lead magnet to paid Stripe checkouts. It targets Japanese women in their 30s-40s experiencing relationship anxieties (e.g., breakups, unresponsiveness).

## Goals / Non-Goals
- **Goals**: 
  - Deliver a production-grade, highly empathetic UI that mirrors user anxieties and provides a structured solution.
  - Implement a 6-section layout with clear pricing cards and CTAs linked to Stripe.
  - Strictly adhere to a soft, calming design system (off-white backgrounds, soft charcoal text, muted gold accents) avoiding harsh blacks or cheap occultism.
- **Non-Goals**: 
  - Actually implementing the Stripe webhook handling here (assumed already existing or handled in a separate change).
  - Building a complex CMS for reviews (hardcoded MVP reviews are acceptable).

## Decisions
- **Design System**: SvelteKit with TailwindCSS (or existing global styles). Colors will use Hex codes mapped to "soft charcoal", "muted gold", and "dusty rose" to ensure the high-end, empathetic vibe.
- **Animations**: Use Svelte's `IntersectionObserver` actions or simple CSS `transition: opacity` with Tailwind's `duration-1000` to create the requested fade-ins on scroll, adding to the premium feel.
- **Typography**: Utilize Noto Serif JP or Yu Mincho via Google Fonts or system font stacks for headings to ensure elegance.

## Risks / Trade-offs
- **Mobile Responsiveness**: Given the target audience, mobile traffic will likely be >90%.
  - **Mitigation**: The design must be mobile-first. The 3-column "Method" section and Pricing cards will stack cleanly on mobile.
- **Load Time**: High-quality fonts and animations can slow down the initial render.
  - **Mitigation**: Keep animations lightweight (CSS opacity/transform) and use font-display: swap.
