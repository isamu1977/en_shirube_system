<script lang="ts">
  import { locale } from '$lib/stores/locale';
  import { t } from '$lib/i18n';
</script>

<footer class="w-full bg-[#1A1918] py-16 md:py-24">
  <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
    <!-- 3 Column Grid -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-12 md:gap-8 mb-12">
      <!-- Column 1: Brand & Identity -->
      <div class="text-center md:text-left">
        <a href="/" class="inline-block">
          <span class="text-3xl md:text-4xl font-serif text-[#EAE5DF] tracking-wider">
            {$t('nav.brand')}
          </span>
        </a>
        <p class="text-sm text-[#A9A39C]/70 mt-3 leading-relaxed">
          {$t('footer.tagline')}
        </p>
        
        <!-- Social Icons -->
        <div class="flex gap-4 mt-6 justify-center md:justify-start">
          <!-- Threads Icon -->
          <a 
            href="#" 
            class="w-8 h-8 rounded-full border border-[#C5A880]/30 flex items-center justify-center text-[#C5A880]/60 hover:text-[#C5A880] hover:border-[#C5A880]/60 transition-colors duration-200"
            aria-label="Threads"
          >
            <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12.186 24h-.007c-3.581-.024-6.334-1.2-8.473-3.606-2.514-2.826-3.652-6.507-3.238-10.429.279-2.647 1.372-4.832 3.082-6.168 1.459-1.14 3.128-1.704 4.873-1.704 1.519 0 2.976.46 4.17 1.346.903.67 1.54 1.5 1.903 2.472.15.402.244.836.303 1.281.147-.14.305-.263.468-.379.855-.608 1.835-.922 2.906-.922 1.32 0 2.582.498 3.535 1.354.946.853 1.475 2.028 1.419 3.302-.048 1.108-.514 2.054-1.314 2.675-.463.36-.994.558-1.569.558-.282 0-.556-.052-.823-.152-.19-.072-.37-.16-.53-.26-.151.36-.34.68-.576.963-.64.768-1.537 1.168-2.57 1.168a4.7 4.7 0 01-.478-.027c-.172.378-.37.741-.598 1.087-1.036 1.57-2.48 2.44-4.167 2.48l-.023.002z"/>
            </svg>
          </a>
          
          <!-- LINE Icon -->
          <a 
            href="#" 
            class="w-8 h-8 rounded-full border border-[#00B900]/30 flex items-center justify-center text-[#00B900]/60 hover:text-[#00B900] hover:border-[#00B900]/60 transition-colors duration-200"
            aria-label="LINE"
          >
            <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19.365 9.863c.349 0 .63.285.63.631 0 .345-.281.63-.63.63H17.61v1.125h1.755c.349 0 .63.283.63.63 0 .344-.281.628-.63.628h-2.386c-.345 0-.627-.284-.627-.628v-3.931c0-.345.282-.63.627-.63h2.386c.349 0 .63.285.63.63 0 .346-.281.631-.63.631h-1.755v1.125h1.755zm-3.855 3.016c0 .27-.174.51-.432.596-.064.021-.133.031-.199.031-.211 0-.391-.09-.51-.25l-2.443-3.317v2.94c0 .344-.279.629-.631.629-.346 0-.626-.285-.626-.629v-3.931c0-.27.173-.51.43-.595.06-.022.13-.031.199-.031.21 0 .394.09.51.25l2.462 3.33V9.779c0-.345.28-.63.63-.63.345 0 .63.285.63.63v3.1zm-2.487-2.725h-1.755v4.481c0 .345-.282.63-.63.63-.345 0-.63-.285-.63-.63v-4.481H10.57c-.345 0-.63-.285-.63-.63 0-.342.285-.627.63-.627h1.518V6.075c0-.345.282-.63.63-.63.345 0 .63.285.63.63v3.432h1.518c.346 0 .63.285.63.627 0 .345-.284.63-.63.63zm-1.013-3.462h-2.386c-.345 0-.63-.285-.63-.63 0-.342.285-.627.63-.627h2.386c.345 0 .63.285.63.63 0 .342-.285.627-.63.627zm-4.545 8.477v-3.931c0-.345.279-.63.63-.63.345 0 .63.285.63.63v3.931c0 .344-.285.628-.63.628-.351 0-.63-.284-.63-.628zm2.487-.596c-.064 0-.135-.01-.199-.031-.258-.085-.432-.326-.432-.595V6.075c0-.345.282-.63.63-.63.346 0 .63.285.63.63v6.096c0 .27-.173.51-.43.595-.06.022-.13.031-.199.031-.21 0-.394-.09-.51-.25L7.484 9.11v2.94c0 .344-.279.629-.63.629-.346 0-.63-.285-.63-.629v-3.931c0-.27.173-.51.43-.595.06-.022.13-.031.199-.031.21 0 .394.09.51.25l2.462 3.33v2.94c0 .345-.284.63-.63.63zm2.13 0v-3.317l2.443 3.316c.119.16.299.25.51.25.066 0 .135-.01.199-.03.258-.086.432-.327.432-.596v-3.931c0-.345-.281-.63-.63-.63-.352 0-.631.285-.631.63v3.1h-.016l-2.443-3.316c-.12-.16-.3-.25-.51-.25-.066 0-.135.01-.199.03-.258.086-.432.327-.432.596v3.931c0 .344.282.628.63.628.346 0 .63-.284.63-.628v-3.1h.017l2.443 3.316c.119.16.299.25.51.25.066 0 .135-.01.199-.03.258-.086.432-.327.432-.596v-3.931c0-.345-.281-.63-.63-.63-.352 0-.631.285-.631.63v3.931c0 .27.173.51.43.595.06.022.13.031.199.031.21 0 .394-.09.51-.25l2.462-3.33V9.779c0-.345-.279-.63-.63-.63-.346 0-.63.285-.63.63v3.1h.017l2.443-3.316c.119-.16.299-.25.51-.25.066 0 .135.01.199.03.258.086.432.327.432.596v3.931c0 .344-.285.628-.63.628-.346 0-.63-.284-.63-.628v-3.1h-.017l-2.443 3.316c-.12.16-.3.25-.51.25-.066 0-.135-.01-.199-.03-.258-.086-.432-.327-.432-.596v-3.931c0-.345.281-.63.63-.63.352 0 .631.285.631.63v3.931c0 .27-.173.51-.43.595-.06.022-.13.031-.199.031-.21 0-.394-.09-.51-.25l-2.462-3.33V9.779c0-.345.279-.63.63-.63.346 0 .63.285.63.63z"/>
            </svg>
          </a>
        </div>
      </div>

      <!-- Column 2: Navigation -->
      <div class="text-center">
        <h3 class="text-xs font-sans uppercase tracking-widest text-[#C5A880] mb-4">
          {$t('footer.menu')}
        </h3>
        <nav class="flex flex-col gap-3">
          <a href="/" class="text-sm text-[#A9A39C] hover:text-[#C5A880] transition-colors duration-200">
            {$t('footer.home')}
          </a>
          <a href="/library" class="text-sm text-[#A9A39C] hover:text-[#C5A880] transition-colors duration-200">
            {$t('footer.library')}
          </a>
          <a href="/about" class="text-sm text-[#A9A39C] hover:text-[#C5A880] transition-colors duration-200">
            {$t('footer.about')}
          </a>
        </nav>
      </div>

      <!-- Column 3: Support & Legal -->
      <div class="text-center md:text-right">
        <h3 class="text-xs font-sans uppercase tracking-widest text-[#C5A880] mb-4">
          {$t('footer.support')}
        </h3>
        <nav class="flex flex-col gap-3 items-center md:items-end">
          <a href="/contact" class="text-sm text-[#A9A39C] hover:text-[#C5A880] transition-colors duration-200">
            {$t('footer.contact')}
          </a>
          <a href="/tokushoho" class="text-sm text-[#A9A39C] hover:text-[#C5A880] transition-colors duration-200">
            {$t('footer.tokushoho')}
          </a>
          <a href="/privacy" class="text-sm text-[#A9A39C] hover:text-[#C5A880] transition-colors duration-200">
            {$t('footer.privacy')}
          </a>
          <a href="/terms" class="text-sm text-[#A9A39C] hover:text-[#C5A880] transition-colors duration-200">
            {$t('footer.terms')}
          </a>
        </nav>
      </div>
    </div>

    <!-- Bottom Bar -->
    <div class="pt-8 border-t border-[#EAE5DF]/5">
      <div class="flex flex-col sm:flex-row items-center justify-between gap-4">
        <!-- Language Toggle -->
        <div class="flex items-center gap-3" aria-label="言語を選択 / Select language">
          <button
            type="button"
            class="text-xs font-sans tracking-widest transition-colors duration-200 cursor-pointer focus-visible:outline-none {$locale === 'ja' ? 'text-[#C5A880] font-bold border-b border-[#C5A880]' : 'text-[#A9A39C]/50 hover:text-[#A9A39C]'}"
            onclick={() => locale.set('ja')}
            aria-pressed={$locale === 'ja'}
          >
            JP
          </button>
          <span class="text-[#EAE5DF]/20 text-xs" aria-hidden="true">|</span>
          <button
            type="button"
            class="text-xs font-sans tracking-widest transition-colors duration-200 cursor-pointer focus-visible:outline-none {$locale === 'en' ? 'text-[#C5A880] font-bold border-b border-[#C5A880]' : 'text-[#A9A39C]/50 hover:text-[#A9A39C]'}"
            onclick={() => locale.set('en')}
            aria-pressed={$locale === 'en'}
          >
            EN
          </button>
        </div>

        <!-- Copyright -->
        <p class="text-xs text-[#A9A39C]/60">
          &copy; {new Date().getFullYear()} 縁しるべ. All rights reserved.
        </p>
      </div>
    </div>
  </div>
</footer>
