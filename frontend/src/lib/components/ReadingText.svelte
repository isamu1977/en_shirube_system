<script lang="ts">
  /**
   * ReadingText.svelte
   * Renders the AI interpretation as beautiful Markdown with soft styling.
   */

  import { fade } from 'svelte/transition';

  interface Props {
    text: string;
    visible?: boolean;
  }

  let { text = '', visible = false }: Props = $props();

  function parseMarkdown(content: string): string {
    let html = content;
    
    html = html.replace(/^### (.+)$/gm, '<h3 class="text-lg font-serif text-[#D4AF37] mt-6 mb-3">$1</h3>');
    html = html.replace(/^## (.+)$/gm, '<h2 class="text-xl font-serif text-[#D4AF37] mt-8 mb-4">$1</h2>');
    html = html.replace(/^# (.+)$/gm, '<h1 class="text-2xl font-serif text-[#D4AF37] mt-8 mb-4">$1</h1>');
    
    html = html.replace(/\*\*(.+?)\*\*/g, '<strong class="font-bold text-[#4A4A4A]">$1</strong>');
    html = html.replace(/\*(.+?)\*/g, '<em class="italic">$1</em>');
    
    html = html.replace(/^- (.+)$/gm, '<li class="ml-4 mb-1 text-[#5A5A5A]">$1</li>');
    html = html.replace(/^(\d+)\. (.+)$/gm, '<li class="ml-4 mb-1 text-[#5A5A5A]">$2</li>');
    
    html = html.replace(/\n\n/g, '</p><p class="mb-4 text-[#5A5A5A] leading-relaxed">');
    html = '<p class="mb-4 text-[#5A5A5A] leading-relaxed">' + html + '</p>';
    
    html = html.replace(/<p class="mb-4 text-\[#5A5A5A\] leading-relaxed"><\/p>/g, '');
    
    return html;
  }

  let parsedHtml = $derived(parseMarkdown(text));
</script>

{#if visible}
  <div 
    class="max-w-2xl mx-auto px-4 py-8"
    in:fade={{ duration: 800, delay: 200 }}
  >
    <div class="bg-white/80 backdrop-blur-sm rounded-2xl shadow-lg p-6 sm:p-8 border border-[#D4AF37]/20">
      <div class="prose prose-sm sm:prose max-w-none">
        {@html parsedHtml}
      </div>
    </div>
  </div>
{/if}
