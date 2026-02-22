<script lang="ts">
  import Card from "$lib/components/Card.svelte";

  // Test Data
  let cards = [
    {
      id: "major_00",
      name_jp: "愚者",
      name_pt: "O Louco",
      image_url: "/images/cards/major_00.png",
      flipped: false,
    },
    {
      id: "cups_ace",
      name_jp: "カップのエース",
      name_pt: "Ás de Copas",
      image_url: "/images/cards/cups_ace.png",
      flipped: false, // Start face down
    },
    {
      id: "wands_king",
      name_jp: "ワンドのキング",
      name_pt: "Rei de Paus",
      image_url: "/images/cards/wands_king.png",
      flipped: true, // Start face up
    },
  ];

  function toggle(index: number) {
    cards[index].flipped = !cards[index].flipped;
  }
</script>

<div
  class="min-h-screen bg-slate-950 flex flex-col items-center justify-center space-y-8 p-8"
>
  <h1
    class="text-3xl text-[#D4AF37] font-serif uppercase tracking-widest border-b border-[#D4AF37]/50 pb-2"
  >
    Card Component Design Test
  </h1>

  <p class="text-gray-400 max-w-md text-center">
    Tap a card to flip it. Demonstrates 3D transform, masking, and trilingual
    overlay.
  </p>

  <div class="flex flex-wrap gap-8 justify-center items-center">
    {#each cards as card, i}
      <div class="flex flex-col items-center space-y-4">
        <!-- Card Instance -->
        <Card
          id={card.id}
          name_jp={card.name_jp}
          name_pt={card.name_pt}
          image_url={card.image_url}
          isFlipped={card.flipped}
          on:click={() => toggle(i)}
        />

        <div class="text-xs text-gray-500 font-mono">
          State: {card.flipped ? "Face Up" : "Face Down"}
        </div>
      </div>
    {/each}
  </div>
</div>
