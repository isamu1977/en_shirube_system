<script lang="ts">
  import { fadein } from "$lib/actions/fade";

  let isLoading = false;

  function scrollToPricing() {
    const el = document.getElementById("pricing");
    el?.scrollIntoView({ behavior: "smooth" });
  }

  async function handleCheckout(tier: "standard" | "premium") {
    isLoading = true;
    try {
      const response = await fetch("/api/v1/checkout/create-session", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ tier }),
      });

      if (!response.ok) {
        throw new Error("決済の開始に失敗しました。");
      }

      const data = await response.json();
      if (data.checkout_url) {
        window.location.href = data.checkout_url;
      }
    } catch (error) {
      console.error("Checkout error:", error);
      alert("エラーが発生しました。再度お試しください。");
    } finally {
      isLoading = false;
    }
  }
</script>

<svelte:head>
  <title>縁しるべ - 恋愛羅針盤鑑定</title>
</svelte:head>

<main
  class="min-h-screen bg-brand-offwhite text-brand-charcoal font-sans overflow-x-hidden"
>
  <!-- 1. Hero Section -->
  <section
    class="relative min-h-[90vh] flex flex-col items-center justify-center px-6 py-20 text-center relative overflow-hidden"
  >
    <!-- Subtle Background Element -->
    <div
      class="absolute inset-0 z-0 opacity-10 pointer-events-none flex items-center justify-center"
    >
      <div class="w-96 h-96 rounded-full bg-brand-gold blur-3xl"></div>
    </div>

    <div class="relative z-10 max-w-3xl" use:fadein>
      <h1
        class="font-serif text-4xl md:text-5xl lg:text-6xl font-medium leading-tight mb-8 text-brand-charcoal tracking-wide"
      >
        彼の本当の気持ち、<br class="md:hidden" />そして二人の未来の行方。
      </h1>
      <p
        class="text-lg md:text-xl text-gray-600 mb-12 max-w-2xl mx-auto leading-relaxed"
      >
        1枚のカードでは見えなかった、<br
          class="md:hidden"
        />深層心理と具体的な「次の行動」を解き明かします。
      </p>
      <button
        on:click={scrollToPricing}
        class="bg-brand-gold hover:bg-opacity-90 transition-colors text-white font-serif px-10 py-4 rounded-full shadow-lg text-lg tracking-wider"
      >
        鑑定メニューを見る
      </button>
    </div>
  </section>

  <!-- 2. The Problem / Empathy Block -->
  <section class="py-24 px-6 bg-brand-light">
    <div class="max-w-4xl mx-auto" use:fadein>
      <h2
        class="font-serif text-3xl md:text-4xl text-center mb-16 text-brand-charcoal"
      >
        こんな不安、抱えていませんか？
      </h2>

      <div class="space-y-6 max-w-2xl mx-auto mb-16">
        <div
          class="bg-white p-6 rounded-2xl shadow-sm border border-brand-rose/20"
        >
          <p class="text-gray-700 leading-relaxed font-medium">
            LINEの返信が遅くて、嫌われたのではないかと不安になる…
          </p>
        </div>
        <div
          class="bg-white p-6 rounded-2xl shadow-sm border border-brand-rose/20"
        >
          <p class="text-gray-700 leading-relaxed font-medium">
            あの時の別れは正解だったのか、今でも迷っている…
          </p>
        </div>
        <div
          class="bg-white p-6 rounded-2xl shadow-sm border border-brand-rose/20"
        >
          <p class="text-gray-700 leading-relaxed font-medium">
            復縁したいけれど、彼にどう思われるか怖くて動けない…
          </p>
        </div>
      </div>

      <div class="text-center">
        <p
          class="font-serif text-xl md:text-2xl text-brand-rose max-w-2xl mx-auto leading-relaxed"
        >
          縁しるべは、そんなあなたの心の霧を<br
            class="md:hidden"
          />晴らすための「羅針盤」です。
        </p>
      </div>
    </div>
  </section>

  <!-- 3. The Method -->
  <section class="py-24 px-6 bg-brand-offwhite">
    <div class="max-w-6xl mx-auto" use:fadein>
      <h2
        class="font-serif text-3xl md:text-4xl text-center mb-20 text-brand-charcoal"
      >
        縁しるべの鑑定が選ばれる理由
      </h2>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-12">
        <div class="text-center flex flex-col items-center">
          <div
            class="w-16 h-16 rounded-full bg-brand-gold/10 flex items-center justify-center mb-6"
          >
            <span class="text-2xl">✨</span>
          </div>
          <h3 class="font-serif text-xl mb-4 font-bold text-brand-charcoal">
            深い感情分析
          </h3>
          <p class="text-gray-600 leading-relaxed">
            単なる吉凶占いではありません。彼の現在の心理状態、隠された本音を独自のタロットAIが深く解読します。
          </p>
        </div>

        <div class="text-center flex flex-col items-center">
          <div
            class="w-16 h-16 rounded-full bg-brand-gold/10 flex items-center justify-center mb-6"
          >
            <span class="text-2xl">🧭</span>
          </div>
          <h3 class="font-serif text-xl mb-4 font-bold text-brand-charcoal">
            具体的行動の提示
          </h3>
          <p class="text-gray-600 leading-relaxed">
            「今後14日間でどう動けばいいか」という明確で具体的なアクションプランを提案します。迷うことはもうありません。
          </p>
        </div>

        <div class="text-center flex flex-col items-center">
          <div
            class="w-16 h-16 rounded-full bg-brand-gold/10 flex items-center justify-center mb-6"
          >
            <span class="text-2xl">🔒</span>
          </div>
          <h3 class="font-serif text-xl mb-4 font-bold text-brand-charcoal">
            完全プライベート
          </h3>
          <p class="text-gray-600 leading-relaxed">
            誰かに話すのが恥ずかしい悩みも、AI鑑定なら安心です。誰にも知られず、あなたの心にだけ寄り添います。
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- 4. Pricing & Packages -->
  <section id="pricing" class="py-24 px-6 bg-brand-light relative">
    <div class="max-w-5xl mx-auto" use:fadein>
      <h2
        class="font-serif text-3xl md:text-4xl text-center mb-6 text-brand-charcoal"
      >
        鑑定メニュー
      </h2>
      <p class="text-center text-gray-600 mb-16 max-w-2xl mx-auto">
        あなたの状況や知りたい深さに合わせてお選びください。<br
        />決済完了後、すぐに鑑定が開始されます。
      </p>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-12">
        <!-- Standard Card -->
        <div
          class="bg-white rounded-3xl p-8 lg:p-10 shadow-sm border border-gray-100 flex flex-col"
        >
          <h3
            class="font-serif text-2xl text-center mb-2 font-bold text-brand-charcoal"
          >
            恋愛羅針盤鑑定
          </h3>
          <p
            class="text-center text-brand-gold text-sm font-medium tracking-widest mb-8"
          >
            STANDARD - 7枚展開
          </p>

          <div class="text-center mb-8">
            <span class="text-4xl font-serif">¥4,980</span>
            <span class="text-gray-400 text-sm italic"> (税込)</span>
          </div>

          <ul class="space-y-4 mb-10 flex-grow text-gray-700">
            <li class="flex items-start">
              <span class="text-brand-gold mr-3 mt-1">✓</span>
              <span>二人の現状と、表向きの感情</span>
            </li>
            <li class="flex items-start">
              <span class="text-brand-gold mr-3 mt-1">✓</span>
              <span>あの人が隠している「本当の気持ち」</span>
            </li>
            <li class="flex items-start">
              <span class="text-brand-gold mr-3 mt-1">✓</span>
              <span>二人の関係を阻む障害</span>
            </li>
            <li class="flex items-start">
              <span class="text-brand-gold mr-3 mt-1">✓</span>
              <span>状況が変わるターニングポイント</span>
            </li>
            <li class="flex items-start">
              <span class="text-brand-gold mr-3 mt-1">✓</span>
              <span>あなたが取るべき「次の具体的な行動」</span>
            </li>
          </ul>

          <button
            on:click={() => handleCheckout("standard")}
            disabled={isLoading}
            class="w-full bg-white border-2 border-brand-charcoal text-brand-charcoal hover:bg-brand-charcoal hover:text-white transition-colors font-serif py-4 rounded-xl text-lg font-bold disabled:opacity-50"
          >
            {isLoading ? "処理中..." : "7枚展開で鑑定する"}
          </button>
        </div>

        <!-- Premium Card -->
        <div
          class="bg-brand-charcoal rounded-3xl p-8 lg:p-10 shadow-2xl relative flex flex-col transform lg:-translate-y-4"
        >
          <div
            class="absolute -top-5 left-1/2 transform -translate-x-1/2 bg-brand-rose text-white text-xs font-bold tracking-widest py-2 px-6 rounded-full shadow-md"
          >
            最も深い洞察を得る
          </div>

          <h3
            class="font-serif text-2xl text-center mb-2 text-white font-bold mt-2"
          >
            復縁完全鑑定
          </h3>
          <p
            class="text-center text-brand-gold text-sm font-medium tracking-widest mb-8"
          >
            PREMIUM - 12枚展開
          </p>

          <div class="text-center mb-8">
            <span class="text-4xl font-serif text-white">¥12,800</span>
            <span class="text-gray-400 text-sm italic"> (税込)</span>
          </div>

          <ul class="space-y-4 mb-10 flex-grow text-gray-200">
            <li class="flex items-start">
              <span class="text-brand-gold mr-3 mt-1">✓</span>
              <span>スタンダード鑑定のすべての要素</span>
            </li>
            <li class="flex items-start">
              <span class="text-brand-gold mr-3 mt-1">✓</span>
              <span>二人の間に存在する深いカルマ（宿縁）</span>
            </li>
            <li class="flex items-start">
              <span class="text-brand-gold mr-3 mt-1">✓</span>
              <span>無意識のブロックとトラウマの分析</span>
            </li>
            <li class="flex items-start">
              <span class="text-brand-gold mr-3 mt-1">✓</span>
              <span>時間の経過に対する感情のタイムライン</span>
            </li>
            <li class="flex items-start">
              <span class="text-brand-gold mr-3 mt-1">✓</span>
              <span>復縁・成就に向けた3段階の戦略プラン</span>
            </li>
          </ul>

          <button
            on:click={() => handleCheckout("premium")}
            disabled={isLoading}
            class="w-full bg-brand-gold hover:bg-opacity-90 transition-colors text-white font-serif py-4 rounded-xl text-lg shadow-lg font-bold disabled:opacity-50"
          >
            {isLoading ? "処理中..." : "12枚展開で深く鑑定する"}
          </button>
        </div>
      </div>
    </div>
  </section>

  <!-- 5. Social Proof (Reviews) -->
  <section class="py-24 px-6 bg-white">
    <div class="max-w-6xl mx-auto" use:fadein>
      <h2
        class="font-serif text-3xl md:text-4xl text-center mb-16 text-brand-charcoal"
      >
        心救われたお客様の声
      </h2>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="bg-brand-offwhite p-8 rounded-2xl relative">
          <div
            class="text-brand-gold text-4xl font-serif absolute top-4 left-4 opacity-30"
          >
            "
          </div>
          <p
            class="text-gray-700 leading-relaxed relative z-10 mb-6 font-medium"
          >
            彼の冷たい態度の理由がわかり、自分がどう動けばいいか明確になりました。モヤモヤしていた心がスッと軽くなりました。
          </p>
          <p class="text-sm text-gray-500 font-serif">Kana (32) / デザイン業</p>
        </div>

        <div class="bg-brand-offwhite p-8 rounded-2xl relative">
          <div
            class="text-brand-gold text-4xl font-serif absolute top-4 left-4 opacity-30"
          >
            "
          </div>
          <p
            class="text-gray-700 leading-relaxed relative z-10 mb-6 font-medium"
          >
            痛いところも突かれましたが、とても納得のいく鑑定でした。AIだからこそ、誰にも言えない秘密の悩みも打ち明けられました。
          </p>
          <p class="text-sm text-gray-500 font-serif">M.Y (38) / 会社員</p>
        </div>

        <div class="bg-brand-offwhite p-8 rounded-2xl relative">
          <div
            class="text-brand-gold text-4xl font-serif absolute top-4 left-4 opacity-30"
          >
            "
          </div>
          <p
            class="text-gray-700 leading-relaxed relative z-10 mb-6 font-medium"
          >
            12枚のプレミアム鑑定を受けました。彼との間にある見えない繋がり（カルマ）を知り、今は焦らずに待つべきだと確信できました。
          </p>
          <p class="text-sm text-gray-500 font-serif">Yoko (41) / 主婦</p>
        </div>
      </div>
    </div>
  </section>

  <!-- 6. FAQ & Footer -->
  <section class="py-24 px-6 bg-brand-light border-b border-gray-200">
    <div class="max-w-3xl mx-auto" use:fadein>
      <h2 class="font-serif text-3xl text-center mb-12 text-brand-charcoal">
        よくあるご質問
      </h2>

      <div class="space-y-6">
        <div class="bg-white p-6 rounded-xl shadow-sm">
          <h4
            class="font-bold text-lg mb-2 text-brand-charcoal flex items-center"
          >
            <span class="text-brand-gold mr-2">Q.</span> 定期的な課金（サブスクリプション）ですか？
          </h4>
          <p class="text-gray-600 pl-7 leading-relaxed">
            いいえ、表示されている料金は1回ずつの買い切り型です。自動で継続課金されることはありませんのでご安心ください。
          </p>
        </div>

        <div class="bg-white p-6 rounded-xl shadow-sm">
          <h4
            class="font-bold text-lg mb-2 text-brand-charcoal flex items-center"
          >
            <span class="text-brand-gold mr-2">Q.</span> 鑑定結果はすぐに見られますか？
          </h4>
          <p class="text-gray-600 pl-7 leading-relaxed">
            はい、決済完了後すぐに専用の鑑定ページへご案内し、リアルタイムでAIがタロットを展開・解読いたします。
          </p>
        </div>
      </div>
    </div>
  </section>

  <footer class="bg-white py-12 px-6 text-center">
    <div
      class="max-w-4xl mx-auto flex flex-col md:flex-row items-center justify-between"
    >
      <div class="mb-6 md:mb-0">
        <span
          class="font-serif text-2xl tracking-widest text-brand-charcoal font-bold"
          >縁しるべ</span
        >
      </div>

      <div
        class="flex flex-wrap justify-center gap-6 text-sm text-gray-500 mb-6 md:mb-0"
      >
        <a href="#" class="hover:text-brand-charcoal transition-colors"
          >利用規約 (Terms)</a
        >
        <a href="#" class="hover:text-brand-charcoal transition-colors"
          >プライバシーポリシー (Privacy)</a
        >
        <a href="#" class="hover:text-brand-charcoal transition-colors"
          >特定商取引法に基づく表記</a
        >
        <a
          href="https://line.me/"
          target="_blank"
          rel="noopener noreferrer"
          class="hover:text-brand-charcoal transition-colors"
          >LINE公式アカウント</a
        >
      </div>
    </div>

    <div class="mt-8 text-xs text-gray-400">
      &copy; 2026 En-shirube. All rights reserved.
    </div>
  </footer>
</main>
