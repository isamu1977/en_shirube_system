<script lang="ts">
  /**
   * Card.svelte
   * Displays a Tarot card with a 3D flip animation, "Mystic Minimalist" styling,
   * and trilingual text support (JP primary, PT secondary).
   * 
   * Props:
   * - id: Card identifier
   * - name_jp: Japanese card name
   * - name_pt: Portuguese card name
   * - name_en: English card name (optional)
   * - image_url: Card image URL
   * - isFlipped: Controls flip state
   * - index: Card position for staggered delay
   * - is_reversed: Whether card is drawn reversed
   */

  interface Props {
    id: string;
    name_jp: string;
    name_pt: string;
    name_en?: string;
    image_url: string;
    isFlipped?: boolean;
    index?: number;
    is_reversed?: boolean;
  }

  let { 
    id, 
    name_jp, 
    name_pt, 
    name_en = "", 
    image_url, 
    isFlipped = false,
    index = 0,
    is_reversed = false
  }: Props = $props();

  function handleKeydown(e: KeyboardEvent) {
    if (e.key === "Enter" || e.key === " ") {
      e.preventDefault();
      (e.currentTarget as HTMLElement).click();
    }
  }

  let flipDelay = $derived(index * 400);

  let cardTransform = $derived.by(() => {
    if (isFlipped) {
      return is_reversed ? 'rotateY(180deg) rotateZ(180deg)' : 'rotateY(180deg)';
    }
    return 'rotateY(0deg)';
  });
</script>

<!-- Scene Container -->
<div
  class="group perspective-1000 w-40 h-60 sm:w-48 sm:h-72 md:w-56 md:h-80 lg:w-64 lg:h-96 cursor-pointer focus:outline-none"
  style="transition-delay: {flipDelay}ms"
  role="button"
  tabindex="0"
  data-testid={id}
>
  <!-- Card Inner (The moving part) -->
  <div
    class="relative w-full h-full transition-all duration-700 transform-style-3d shadow-2xl rounded-2xl"
    style="transform: {cardTransform}; transition-timing-function: cubic-bezier(0.4, 0.0, 0.2, 1)"
  >
    <!-- FRONT FACE (The Tarot Art) -->
    <!-- Rotated 180deg so it's "behind" the back initially -->
    <div
      class="absolute w-full h-full inset-0 backface-hidden rotate-y-180 rounded-2xl overflow-hidden border-2 border-[#D4AF37] bg-slate-900"
    >
      <!-- Image with Masking -->
      <div class="relative w-full h-full">
        <img
          src={image_url}
          alt="{name_en || name_pt} - {name_jp}"
          class="w-full h-full object-cover"
        />

        <!-- Gradient Overlay for Text Readability -->
        <div
          class="absolute bottom-0 left-0 right-0 h-1/3 bg-gradient-to-t from-black/90 to-transparent pointer-events-none"
        ></div>

        <!-- Trilingual Label -->
        <div class="absolute bottom-4 left-0 right-0 text-center px-2">
          <h2
            class="text-white text-xl font-bold font-serif tracking-widest drop-shadow-md mb-0.5"
          >
            {name_jp}
          </h2>
          <p
            class="text-[#D4AF37] text-xs font-serif uppercase tracking-widest opacity-90"
          >
            {name_pt}
          </p>
        </div>
      </div>
    </div>

    <!-- BACK FACE (The Pattern) -->
    <div
      class="absolute w-full h-full inset-0 backface-hidden rounded-2xl overflow-hidden border-2 border-[#D4AF37]/50 bg-[#0a0f1c]"
    >
      <img
        src="/images/back_cover.png"
        alt="Card Back"
        class="w-full h-full object-cover opacity-90"
      />
      <!-- Center Symbol -->
      <div
        class="absolute inset-0 flex items-center justify-center pointer-events-none"
      >
        <div
          class="w-12 h-12 border border-[#D4AF37]/30 rounded-full flex items-center justify-center"
        >
          <div class="w-8 h-8 border border-[#D4AF37]/60 rotate-45"></div>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
  .perspective-1000 {
    perspective: 1000px;
  }
  .transform-style-3d {
    transform-style: preserve-3d;
  }
  .backface-hidden {
    backface-visibility: hidden;
  }
</style>
