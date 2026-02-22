<script lang="ts">
  /**
   * Reading Result Page
   * Displays the result of a tarot reading with card reveal animation and interpretation.
   */

  import SpreadBoard from '$lib/components/SpreadBoard.svelte';
  import ReadingText from '$lib/components/ReadingText.svelte';
  import { page } from '$app/stores';
  import { onMount } from 'svelte';

  interface CardData {
    id: string;
    name_jp: string;
    name_pt: string;
    name_en: string;
    image_url: string;
    is_reversed: boolean;
    position?: string;
  }

  interface ReadingData {
    id: string;
    user_name: string;
    focus_area: string;
    cards_drawn: string[];
    interpretation_text: string;
    language: string;
    created_at: string;
  }

  let sessionId = $derived($page.params.session_id);
  
  let loading = $state(true);
  let error = $state<string | null>(null);
  let reading = $state<ReadingData | null>(null);
  let cards = $state<CardData[]>([]);
  let showText = $state(false);

  const POSITIONS = [
    '現在の状況',
    'あなたの心境',
    '相手の心境',
    '障害',
    '転換期',
    '次のアクション',
    '結果'
  ];

  onMount(async () => {
    await fetchReading();
  });

  async function fetchReading() {
    try {
      loading = true;
      error = null;

      const response = await fetch(`/api/v1/reading/${sessionId}`);
      
      if (!response.ok) {
        if (response.status === 404) {
          error = 'この鑑定が見つかりません';
        } else {
          error = '鑑定の読み込みに失敗しました';
        }
        return;
      }

      const data = await response.json();
      reading = data;

      if (data.cards && data.cards.length > 0) {
        cards = data.cards.map((card: any, index: number) => ({
          id: card.id || card.card_id,
          name_jp: card.name_jp || card.nameJp || 'カード',
          name_pt: card.name_pt || card.namePt || 'Carta',
          name_en: card.name_en || card.nameEn || 'Card',
          image_url: card.image_url || card.imageUrl || '/images/cards/default.jpg',
          is_reversed: card.is_reversed || card.isReversed || false,
          position: POSITIONS[index] || undefined
        }));
      }
    } catch (e) {
      error = 'ネットワークエラーが発生しました';
      console.error('Failed to fetch reading:', e);
    } finally {
      loading = false;
    }
  }

  function handleRevealComplete() {
    showText = true;
  }
</script>

<svelte:head>
  <title>鑑定結果 | 縁しるべ</title>
</svelte:head>

<main class="min-h-screen bg-gradient-to-b from-[#F5F0E8] to-[#E8E0D0]">
  {#if loading}
    <div class="flex items-center justify-center min-h-screen">
      <div class="text-center">
        <div class="w-12 h-12 border-4 border-[#D4AF37] border-t-transparent rounded-full animate-spin mx-auto mb-4"></div>
        <p class="text-[#8B7355] font-serif">鑑定を読み込み中...</p>
      </div>
    </div>
  {:else if error}
    <div class="flex items-center justify-center min-h-screen">
      <div class="text-center px-4">
        <p class="text-[#8B7355] font-serif text-lg mb-4">{error}</p>
        <a 
          href="/" 
          class="inline-block px-6 py-3 bg-[#D4AF37] text-white rounded-full font-serif hover:bg-[#B8963C] transition-colors"
        >
          トップに戻る
        </a>
      </div>
    </div>
  {:else}
    <div class="py-8">
      <h1 class="text-2xl sm:text-3xl font-serif text-center text-[#4A4A4A] mb-2">
        鑑定結果
      </h1>
      {#if reading?.user_name}
        <p class="text-center text-[#8B7355] font-serif mb-8">
          {reading.user_name}様
        </p>
      {/if}

      <SpreadBoard {cards} onRevealComplete={handleRevealComplete} />

      {#if reading?.interpretation_text}
        <ReadingText text={reading.interpretation_text} visible={showText} />
      {/if}

      <div class="text-center mt-8 pb-8">
        <a 
          href="/" 
          class="inline-block px-6 py-3 border-2 border-[#D4AF37] text-[#D4AF37] rounded-full font-serif hover:bg-[#D4AF37] hover:text-white transition-colors"
        >
          もう一度占う
        </a>
      </div>
    </div>
  {/if}
</main>
