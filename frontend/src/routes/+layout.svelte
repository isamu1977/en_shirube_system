<script lang="ts">
  import "../app.css";
  import favicon from '$lib/assets/favicon.svg';
  import { locale } from '$lib/stores/locale';
  import { t } from '$lib/i18n';
  import { browser } from '$app/environment';
  import Footer from '$lib/components/Footer.svelte';

  let { children } = $props();

  // Init locale from localStorage on mount (client only)
  if (browser) {
    const saved = localStorage.getItem('enshirube_locale');
    if (saved === 'en' || saved === 'ja') locale.set(saved);
  }
</script>

<svelte:head>
  <link rel="icon" href="{favicon}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous" />
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700&family=Noto+Serif+JP:wght@400;500;600;700&display=swap" rel="stylesheet" />
</svelte:head>

<div class="min-h-screen flex flex-col bg-[#252321]">
  <!-- Floating Header -->
  <header class="sticky top-0 z-50 w-full py-4 bg-[#252321]/90 backdrop-blur-md border-b border-[#EAE5DF]/5">
    <div class="max-w-6xl mx-auto px-4 flex items-center justify-between">
      <a href="/" class="text-2xl md:text-3xl font-serif text-[#EAE5DF] hover:text-[#C5A880] transition-colors duration-200 cursor-pointer tracking-wider" aria-label="縁しるべ ホームページ">
        {$t('nav.brand')}
      </a>
      <nav>
        <a href="/library" class="text-sm font-sans text-[#A9A39C] hover:text-[#C5A880] transition-colors duration-200">
          {$locale === 'ja' ? 'ライブラリ' : 'Library'}
        </a>
      </nav>
    </div>
  </header>

  <main class="flex-grow w-full">
    {@render children()}
  </main>

  <Footer />
</div>
