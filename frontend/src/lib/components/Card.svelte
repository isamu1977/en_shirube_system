<script lang="ts">
  /**
   * Card.svelte
   * Displays a Tarot card with a 3D flip animation, "Mystic Minimalist" styling,
   * and trilingual text support (JP primary, PT secondary).
   */

  export let id: string;
  export let name_jp: string;
  export let name_pt: string;
  export let name_en: string = ""; // Optional, for accessibility/alt text
  export let image_url: string;
  export let isFlipped: boolean = false;

  function handleKeydown(e: KeyboardEvent) {
    if (e.key === "Enter" || e.key === " ") {
      e.preventDefault();
      // Trigger the click event so parent handles it regardless of input method
      (e.currentTarget as HTMLElement).click();
    }
  }
</script>

<!-- Scene Container -->
<div
  class="group perspective-1000 w-64 h-96 cursor-pointer focus:outline-none"
  on:click
  on:keydown={handleKeydown}
  role="button"
  tabindex="0"
  data-testid={id}
>
  <!-- Card Inner (The moving part) -->
  <div
    class="relative w-full h-full transition-all duration-700 ease-in-out transform-style-3d shadow-2xl rounded-2xl"
    class:rotate-y-180={isFlipped}
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
  .rotate-y-180 {
    transform: rotateY(180deg);
  }
</style>
