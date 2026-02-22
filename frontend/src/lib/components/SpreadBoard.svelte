<script lang="ts">
  /**
   * SpreadBoard.svelte
   * Displays a spread of Tarot cards with staggered reveal animation.
   * Mobile-first responsive layout.
   */

  import Card from './Card.svelte';
  import { fade } from 'svelte/transition';

  interface CardData {
    id: string;
    name_jp: string;
    name_pt: string;
    name_en?: string;
    image_url: string;
    is_reversed: boolean;
    position?: string;
  }

  interface Props {
    cards: CardData[];
    onRevealComplete?: () => void;
  }

  let { cards = [], onRevealComplete }: Props = $props();

  let isRevealing = $state(false);
  let showTapPrompt = $state(true);
  let flippedIndices = $state<number[]>([]);

  async function startReveal() {
    if (isRevealing || cards.length === 0) return;
    
    isRevealing = true;
    showTapPrompt = false;
    flippedIndices = [];

    for (let i = 0; i < cards.length; i++) {
      await new Promise(resolve => setTimeout(resolve, 400));
      flippedIndices = [...flippedIndices, i];
      
      if (i === cards.length - 1) {
        setTimeout(() => {
          if (onRevealComplete) {
            onRevealComplete();
          }
        }, 800);
      }
    }
  }

  function isFlipped(index: number): boolean {
    return flippedIndices.includes(index);
  }
</script>

<div class="w-full min-h-[60vh] flex flex-col items-center justify-center py-8">
  {#if showTapPrompt && !isRevealing}
    <button
      onclick={startReveal}
      class="px-8 py-4 bg-gradient-to-r from-[#D4AF37] to-[#B8963C] text-white font-serif text-lg rounded-full shadow-lg hover:shadow-xl transform hover:scale-105 transition-all duration-300"
      in:fade={{ duration: 300 }}
    >
      カードを引く
    </button>
  {/if}

  <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-7 gap-3 sm:gap-4 md:gap-6 mt-8 px-4">
    {#each cards as card, index (card.id)}
      <div class="flex flex-col items-center">
        {#if card.position}
          <span class="text-xs sm:text-sm text-[#8B7355] font-serif mb-2 text-center">
            {card.position}
          </span>
        {/if}
        <Card
          id={card.id}
          name_jp={card.name_jp}
          name_pt={card.name_pt}
          name_en={card.name_en || ''}
          image_url={card.image_url}
          isFlipped={isFlipped(index)}
          index={index}
          is_reversed={card.is_reversed}
        />
      </div>
    {/each}
  </div>
</div>
