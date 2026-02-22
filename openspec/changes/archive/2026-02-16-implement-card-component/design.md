# Design: Card Component

## Aesthetic Direction (Frontend Design Skill)

- **Style**: Mystic Minimalism / Luxury.
- **Palette**: Deep background, Gold (`#D4AF37`) accents.
- **Motion**: Physical, weighted flip animation (not instant).

## Component Interface

```svelte
<script lang="ts">
  export let card: {
    id: string;
    name_jp: string;
    name_pt: string;
    image_url: string; // e.g. /images/cards/major_00.png
  };
  export let isFlipped: boolean = false;
</script>
```

## Visual Specification

1.  **Dimensions**: `aspect-[2/3]` strictly maintained.
2.  **Masking**: `rounded-2xl` with `overflow-hidden` to crop the rectangular AI images into the card shape.
3.  **Border**: Solid 1px-2px `border-[#D4AF37]` (Gold) on the container, _outside_ the image masking if possible, or consistent with it.
4.  **Shadow**: `shadow-xl` to lift it from the background.
5.  **Back Cover**: A standard pattern (to be sourced/generated).
6.  **Typography**:
    - Primary: Japanese name (Kanji/Kana), larger font, prominent.
    - Secondary: Portuguese name, smaller, elegant serif (e.g., _Outfit_ or _Cinzel_).

## Interaction Logic

- **State**: `isFlipped` prop controls the rotation.
- **Transition**: `transform-style: preserve-3d`, `transition: transform 0.6s cubic-bezier(0.4, 0.0, 0.2, 1)`.
- **Faces**: Front (Image + Text overlay?), Back (Pattern). Backface visibility hidden.

## Directory Structure

- `frontend/src/lib/components/Card.svelte`
- `frontend/static/images/cards/[id].png`
- `frontend/static/images/back_cover.png`
