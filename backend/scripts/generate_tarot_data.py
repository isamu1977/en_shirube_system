import json
import os

MAJOR_ARCANA = [
    {
        "id": 1, "name_jp": "愚者 (The Fool)", "name_en": "The Fool", "number": 0,
        "meaning_upright": "新しい始まり、自由、楽観主義、直感に従う。",
        "meaning_reversed": "無責任、現実逃避、躊躇、計画性のなさ。",
        "love_context_upright": "彼は過去のしがらみを捨て、フラットな状態であなたとの関係を見つめ直したいと感じています。プレッシャーを与えない軽いコミュニケーションが吉です。",
        "love_context_reversed": "今の彼は責任や縛られることを極端に恐れています。復縁を迫ると逃げたくなる心理状態なので、今は距離を置くのが賢明です。"
    },
    {
        "id": 2, "name_jp": "魔術師 (The Magician)", "name_en": "The Magician", "number": 1,
        "meaning_upright": "創造性、意思、可能性、行動の始まり。",
        "meaning_reversed": "優柔不断、自信の欠如、空回り、騙し。",
        "love_context_upright": "彼はあなたとの関係を自分の手でリードし、新しい展開を作りたいと意欲的です。コミュニケーションもスムーズに進展するでしょう。",
        "love_context_reversed": "言葉だけで行動が伴わない状態です。建前やその場しのぎの態度に出やすいため、彼の言葉を鵜呑みにせず様子を見る必要があります。"
    },
    {
        "id": 3, "name_jp": "女教皇 (The High Priestess)", "name_en": "The High Priestess", "number": 2,
        "meaning_upright": "直感、知性、精神性、静かな見守り。",
        "meaning_reversed": "ヒステリック、冷酷、秘密主義、無関心。",
        "love_context_upright": "彼は今、自分の内面と静かに向き合っています。プラトニックな好意を抱いており、慎重に関係を深めたいと考えているようです。",
        "love_context_reversed": "感情を閉ざし、あなたに対して冷たい壁を作っている状態です。疑心暗鬼になりやすいため、無理に本音を探らない方が良いでしょう。"
    },
    {
        "id": 4, "name_jp": "女帝 (The Empress)", "name_en": "The Empress", "number": 3,
        "meaning_upright": "豊かさ、母性、深い愛情、魅力の開花。",
        "meaning_reversed": "嫉妬、依存、我が儘、感情の怠惰。",
        "love_context_upright": "あなたを心から愛おしく、大切に守りたいという包容力に満ちています。ありのままのあなたを受け入れる無条件の愛を感じています。",
        "love_context_reversed": "甘えや依存心が強くなり、関係がルーズになっています。あるいは、過干渉を重荷に感じている可能性もあるため、適度な距離感が必要です。"
    },
    {
        "id": 5, "name_jp": "皇帝 (The Emperor)", "name_en": "The Emperor", "number": 4,
        "meaning_upright": "責任感、安定、リーダーシップ、論理的。",
        "meaning_reversed": "頑固、支配的、無責任、独裁的。",
        "love_context_upright": "関係に対して真面目で、あなたを守る責任を果たしたいと考えています。結婚や将来を見据えた堅実な愛情を持っています。",
        "love_context_reversed": "プライドが邪魔をして素直になれず、意固地になっています。自分のペースを押し付けがちなので、今は張り合わず立ててあげる工夫が必要です。"
    },
    {
        "id": 6, "name_jp": "教皇 (The Hierophant)", "name_en": "The Hierophant", "number": 5,
        "meaning_upright": "伝統、信頼、モラル、精神的指導。",
        "meaning_reversed": "束縛、狭い視野、偽善、ルールへの反発。",
        "love_context_upright": "人としてあなたを深く尊敬し、誠実に付き合いたいと望んでいます。周囲からも応援されるような公明正大な関係を求めています。",
        "love_context_reversed": "世間体や固定観念に囚われ、本音で向き合えていません。建前を優先するあまり、二人の間の本当の感情を避けている状態です。"
    },
    {
        "id": 7, "name_jp": "恋人 (The Lovers)", "name_en": "The Lovers", "number": 6,
        "meaning_upright": "調和、選択、深い結びつき、情熱的な恋。",
        "meaning_reversed": "誘惑、不調和、優柔不断、関係の冷却。",
        "love_context_upright": "理屈抜きにあなたに強く惹かれ、一緒にいるだけで心から楽しいと感じています。恋愛感情が最も高まっている最高のタイミングです。",
        "love_context_reversed": "気持ちが揺れ動き、決断を先延ばしにしています。一時的な誘惑に流されやすく、関係に対する真剣さが欠けている兆候です。"
    },
    {
        "id": 8, "name_jp": "戦車 (The Chariot)", "name_en": "The Chariot", "number": 7,
        "meaning_upright": "前進、勝利、行動力、困難の克服。",
        "meaning_reversed": "暴走、挫折、制御不能、焦り。",
        "love_context_upright": "障害があってもそれを乗り越えて、あなたを手に入れたいという強い情熱と行動力を持っています。一気に距離が縮まる予感です。",
        "love_context_reversed": "焦りから相手への配慮を欠き、感情が暴走気味です。自分の思い通りにならないと不満を溜めるため、少し冷静にさせる必要があります。"
    },
    {
        "id": 9, "name_jp": "力 (Strength)", "name_en": "Strength", "number": 8,
        "meaning_upright": "忍耐力、精神的な強さ、受容、思いやり。",
        "meaning_reversed": "無力感、感情の爆発、自己嫌悪、諦め。",
        "love_context_upright": "困難な状況でも、あなたに対する確かな愛情を根底に持ち、信じて待つ強さがあります。お互いの弱さを受け入れ合える深い絆です。",
        "love_context_reversed": "自信を喪失し、関係を維持していく気力や忍耐が尽きかけています。感情的になりやすく、関係を投げ出したい衝動に駆られています。"
    },
    {
        "id": 10, "name_jp": "隠者 (The Hermit)", "name_en": "The Hermit", "number": 9,
        "meaning_upright": "内省、探究心、孤独、思慮深さ。",
        "meaning_reversed": "閉鎖的、孤独感、現実逃避、頑なさ。",
        "love_context_upright": "自分の本心とじっくり向き合いたい時期です。あなたのことは大切に思っていますが、今は恋愛よりも一人の時間を必要としています。",
        "love_context_reversed": "心を完全に閉ざし、周囲からの干渉を拒絶しています。過去の傷に囚われている可能性が高く、今はアプローチを控えるべきです。"
    },
    {
        "id": 11, "name_jp": "運命の輪 (Wheel of Fortune)", "name_en": "Wheel of Fortune", "number": 10,
        "meaning_upright": "好転、チャンス、運命的な出会い、タイミング。",
        "meaning_reversed": "すれ違い、タイミングの悪さ、悪化、抗えない変化。",
        "love_context_upright": "あなたとの出会いや再会に運命的な縁を感じています。思いがけないきっかけでトントン拍子に関係が進展していく心理状態です。",
        "love_context_reversed": "どうしてもタイミングが合わず、「縁がなかったのかもしれない」と諦めの気持ちが芽生え始めています。今は無理に動くべき時ではありません。"
    },
    {
        "id": 12, "name_jp": "正義 (Justice)", "name_en": "Justice", "number": 11,
        "meaning_upright": "バランス、公平さ、誠実、論理的判断。",
        "meaning_reversed": "不公平、偏見、優柔不断、感情的な判断。",
        "love_context_upright": "感情に流されず、あなたとの関係を客観的かつ誠実に評価しています。ギブアンドテイクのバランスが取れた対等な付き合いを望んでいます。",
        "love_context_reversed": "あなたに対する評価が厳しくなり、欠点ばかりに目が向いています。損得勘定が働き、関係をフェアに保とうとする意欲が低下しています。"
    },
    {
        "id": 13, "name_jp": "吊るされた男 (The Hanged Man)", "name_en": "The Hanged Man", "number": 12,
        "meaning_upright": "試練、献身、視点の転換、自己犠牲。",
        "meaning_reversed": "骨折り損、徒労、自己中心、焦り。",
        "love_context_upright": "今は状況が動かなくても、あなたのためなら耐え忍ぶ覚悟があります。身動きがとれない現状の中でも、内面では深い愛情を育てています。",
        "love_context_reversed": "自分の我慢が報われないことに不満を抱いています。あるいは、状況を変える努力を放棄しており、被害者意識が高まっている状態です。"
    },
    {
        "id": 14, "name_jp": "死神 (Death)", "name_en": "Death", "number": 13,
        "meaning_upright": "終焉、再生、リセット、未練を断つ。",
        "meaning_reversed": "執着、停滞、未練、変われない現状。",
        "love_context_upright": "過去のやり方や古い関係性に完全に終止符を打ち、ゼロから新しい形で関係を再構築（再生）したいという強い決意を持っています。",
        "love_context_reversed": "過去の傷やしがらみに執着しており、前に進むことができずにいます。関係を終わらせる勇気も、やり直す気力もない停滞期です。"
    },
    {
        "id": 15, "name_jp": "節制 (Temperance)", "name_en": "Temperance", "number": 14,
        "meaning_upright": "調和、節度、自然体、スムーズな交流。",
        "meaning_reversed": "不均衡、極端、コミュニケーション不足、妥協。",
        "love_context_upright": "あなたと一緒にいると波長が合い、無理なく自分らしくいられると感じています。穏やかな愛情と自然なコミュニケーションがとれる状態です。",
        "love_context_reversed": "価値観の違いや感情のすれ違いから、コミュニケーションのリズムが崩れています。妥協できず、極端な態度に出やすくなっています。"
    },
    {
        "id": 16, "name_jp": "悪魔 (The Devil)", "name_en": "The Devil", "number": 15,
        "meaning_upright": "束縛、執着、誘惑、抜け出せない関係。",
        "meaning_reversed": "解放、執着を捨てる、腐れ縁からの脱却、悪習慣を断つ。",
        "love_context_upright": "純粋な愛情というよりは、肉体的な魅力や執着心に強く縛られています。離れられない腐れ縁や独占欲にとらわれている心理状態です。",
        "love_context_reversed": "長く続いた不健康な執着や依存関係から、ようやく精神的に解放されようとしています。冷静に関係を見つめ直せるようになりつつあります。"
    },
    {
        "id": 17, "name_jp": "塔 (The Tower)", "name_en": "The Tower", "number": 16,
        "meaning_upright": "崩壊、突然のアクシデント、衝撃的な変化、思い込みの破壊。",
        "meaning_reversed": "緊迫感、ゆっくりとした崩壊、トラウマ、避けられないトラブル。",
        "love_context_upright": "予期せぬ出来事によって、あなたに対する今までの価値観や前提が完全に崩れ去りました。大変なショックを受けており、混乱の極みにいます。",
        "love_context_reversed": "いずれ関係が破綻することに気づきながらも、見て見ぬふりをしてジワジワと不安を抱えています。根本的な問題から逃げている状態です。"
    },
    {
        "id": 18, "name_jp": "星 (The Star)", "name_en": "The Star", "number": 17,
        "meaning_upright": "希望、ひらめき、理想、明るい見通し。",
        "meaning_reversed": "失望、悲観的、高望み、夢想。",
        "love_context_upright": "あなたとの未来に純粋な希望を抱いており、理想的な相手だと感じています。傷ついた心も癒え、前向きな気持ちで恋に向き合っています。",
        "love_context_reversed": "期待が大きすぎた反動で失望を感じており、「どうせうまくいかない」と悲観的になっています。理想と現実のギャップに苦しんでいます。"
    },
    {
        "id": 19, "name_jp": "月 (The Moon)", "name_en": "The Moon", "number": 18,
        "meaning_upright": "不安、迷い、見えない真実、潜在意識の揺れ。",
        "meaning_reversed": "不安の解消、真実が明らかになる、誤解が解ける、徐々に視界が開ける。",
        "love_context_upright": "本心が見えず、本当に愛されているのか、今後どうなるのかという漠然とした不安と疑心暗鬼に飲み込まれています。彼の心は霧のなかにあります。",
        "love_context_reversed": "ずっと心の中にあったモヤモヤや疑い、隠されていた嘘が晴れようとしています。不安がスッと消え、関係の真の姿を受け止められる状態です。"
    },
    {
        "id": 20, "name_jp": "太陽 (The Sun)", "name_en": "The Sun", "number": 19,
        "meaning_upright": "成功、誕生、純粋な喜び、活力。",
        "meaning_reversed": "衰退、延期、虚勢、わがまま。",
        "love_context_upright": "あなたと一緒にいる喜びを全身で感じており、何の隠し立てもないオープンで明るい好意を持っています。最も幸福で素直な愛情表現が期待できます。",
        "love_context_reversed": "好意はあるものの、少し熱量が下がり気味です。見栄を張ったり自己中心的になったりして、純粋に楽しむ気持ちが空回りしている状態です。"
    },
    {
        "id": 21, "name_jp": "審判 (Judgement)", "name_en": "Judgement", "number": 20,
        "meaning_upright": "復活、決断、目覚め、奇跡的な回復。",
        "meaning_reversed": "過去への未練、挫折、後悔、許されない感情。",
        "love_context_upright": "一度は終わった関係や冷めた気持ちが、奇跡的に蘇るタイミングです。過去のわだかまりを許し、再び強い覚悟を持ってあなたを求めています。",
        "love_context_reversed": "過去の失敗や後悔をどうしても引きずってしまい、前に進む決断を下せません。『もう取り返しがつかない』という後ろ向きな心理に支配されています。"
    },
    {
        "id": 22, "name_jp": "世界 (The World)", "name_en": "The World", "number": 21,
        "meaning_upright": "完成、完全なる調和、達成、素晴らしい結末。",
        "meaning_reversed": "未完成、中途半端、マンネリ、スランプ。",
        "love_context_upright": "あなたとの関係が彼にとって理想の「完成形」であり、これ以上望むものはないという至福の感情を抱いています。最終的な結ばれる運命を感じています。",
        "love_context_reversed": "関係がどこか中途半端で、あと一歩踏み込みきれない状態です。現状維持のマンネリ感に陥り、完全な満足には至っていません。"
    }
]

SUITS = {
    "wands": {"jp": "ワンド", "en": "Wands", "theme": "情熱や行動、直感", "upright_context": "情熱的で行動を起こしたいという前向きなエネルギー", "reversed_context": "エネルギーの空回りや行き違い、やる気の喪失"},
    "cups": {"jp": "カップ", "en": "Cups", "theme": "感情や愛情、繋がり", "upright_context": "深い愛情や感受性、感情の共有", "reversed_context": "感情のすれ違い、過度な感情や冷め"},
    "swords": {"jp": "ソード", "en": "Swords", "theme": "思考や知性、葛藤", "upright_context": "理性的な判断、問題への論理的な対処", "reversed_context": "傷つけ合い、厳しい言葉、深刻なトラウマや悩み"},
    "pentacles": {"jp": "ペンタクル", "en": "Pentacles", "theme": "現実や物質、安定", "upright_context": "現実的な将来への投資、着実な歩み寄り", "reversed_context": "物質的な執着、関係の停滞、現実の厳しさ"}
}

RANKS = {
    1: {"jp": "エース", "en": "Ace", "meaning_up": "新たな始まり、純粋なエネルギーの誕生。", "meaning_rev": "エネルギーの枯渇、始まりの遅れ。", "love_up": "あなたへの新しい感情が芽生え、関係をイチから育てていきたい強烈な意欲があります。", "love_rev": "関係を進展させるためのきっかけを掴めず、最初の一歩を踏み出す勇気が出ない状態です。"},
    2: {"jp": "の2", "en": "Two of", "meaning_up": "バランス、パートナーシップ、選択。", "meaning_rev": "不和、均衡の崩れ、決定の先延ばし。", "love_up": "あなたとの関係において、お互いの価値観を共有し、協力してバランスを取ろうとしています。", "love_rev": "お互いの気持ちの矢印が少しズレており、コミュニケーションの不和から距離を感じています。"},
    3: {"jp": "の3", "en": "Three of", "meaning_up": "成長、協力、最初の成果。", "meaning_rev": "チームワークの欠如、第三者の介入、計画の遅れ。", "love_up": "関係が順調に育っており、より深い絆へと発展させていく喜びを実感しています。", "love_rev": "周囲の環境や他の人物の存在がノイズとなり、二人の関係に集中できていない状態です。"},
    4: {"jp": "の4", "en": "Four of", "meaning_up": "安定、基盤、休息、固執。", "meaning_rev": "停滞、保守的すぎる態度、不安定な基盤。", "love_up": "あなたとの関係に安心感と確固たる基盤を見出し、ホッと心安らぐ居場所だと感じています。", "love_rev": "現状を維持することに固執しすぎており、新しい変化を拒絶する停滞期に入っています。"},
    5: {"jp": "の5", "en": "Five of", "meaning_up": "喪失、葛藤、困難、変化。", "meaning_rev": "回復の兆し、困難の受容、新たな視点。", "love_up": "関係において深く傷ついたり、期待が外れたことで、強い失望感や喪失感に苛まれています。", "love_rev": "一番辛かった時期を乗り越え、少しずつ現実を受け入れて関係を再構築する気持ちが湧いてきています。"},
    6: {"jp": "の6", "en": "Six of", "meaning_up": "調和、過去の郷愁、助け合い。", "meaning_rev": "過去への執着、未来への不安、不平等。", "love_up": "過去の楽しかった思い出を懐古し、あなたに優しく手を差し伸べたいという純粋な好意があります。", "love_rev": "美化された過去にばかり捉われており、今のあなたと向き合う努力から逃げてしまっています。"},
    7: {"jp": "の7", "en": "Seven of", "meaning_up": "優位性、防衛、評価、挑戦。", "meaning_rev": "圧倒される、自己防衛の崩れ、無力感。", "love_up": "ライバルや障害に対して、あなたを守り抜きたい、自分の立場を維持したいと強く奮闘しています。", "love_rev": "プレッシャーや障害に心が折れかけており、あなたのために戦う気力を失いつつあります。"},
    8: {"jp": "の8", "en": "Eight of", "meaning_up": "継続、動き、制限の認識。", "meaning_rev": "停滞からの脱却、行動の遅れ、集中力の欠如。", "love_up": "関係をより良くするために、今は地道な努力やステップアップに集中したいと考えています。", "love_rev": "惰性で関わっており、本当の意味で関係においての焦点を絞れず、時間だけが過ぎています。"},
    9: {"jp": "の9", "en": "Nine of", "meaning_up": "達成、満足、不安、最終段階。", "meaning_rev": "過剰、不安の解消、不完全な満足。", "love_up": "一人でも自立した上で満たされている状態か、あるいはあなたに対する根深い不安や懸念を一人で抱え込んでいます。", "love_rev": "ずっと抱えていた心配事が嘘のように晴れる兆しがありますが、まだ完全に心を開ききってはいません。"},
    10: {"jp": "の10", "en": "Ten of", "meaning_up": "完成、結末、重圧、最終形。", "meaning_rev": "解放、新たなサイクル、プレッシャーからの脱却。", "love_up": "あなたとの関係がひとつのピークを迎えており、愛情の完成と当時に大きな重圧や責任も感じています。", "love_rev": "背負っていた重荷を下ろし、無理をせずにあなたと等身大の付き合いをしたいと望んでいます。"},
    11: {"jp": "のペイジ", "en": "Page of", "meaning_up": "好奇心、初心、メッセンジャー。", "meaning_rev": "未熟さ、散漫、悪い知らせ。", "love_up": "純粋な好奇心と初々しい感情であなたに関心を寄せており、素直な好意を伝えたがっています。", "love_rev": "子供っぽくわがままな態度が出ており、関係に対する責任感が伴わない未熟な状態です。"},
    12: {"jp": "のナイト", "en": "Knight of", "meaning_up": "行動、推進力、情熱的なアプローチ。", "meaning_rev": "焦り、無鉄砲、感情のムラ。", "love_up": "あなたに向けて真っ直ぐにアプローチしたいという強い推進力と、若々しい情熱を持っています。", "love_rev": "衝動的で自己中心的な振る舞いが目立ち、思いつきで行動するため関係が不安定になりがちです。"},
    13: {"jp": "のクイーン", "en": "Queen of", "meaning_up": "受容、内からの力、育む心。", "meaning_rev": "過干渉、感情的、冷淡。", "love_up": "あなたを優しく包み込み、成熟した愛情で関係を育んでいきたいという受容性に満ちています。", "love_rev": "感情のコントロールが効かず、過干渉になったり急に冷たくなったりと、心が不安定な状態です。"},
    14: {"jp": "のキング", "en": "King of", "meaning_up": "権威、成熟した力、統率力。", "meaning_rev": "支配的、頑固、権力の間違った行使。", "love_up": "大人の余裕と責任感を持ってあなたを守り、関係をリードしていく頼もしい愛情を持っています。", "love_rev": "自分のやり方を押し付けがちで、相手の気持ちよりも自分のプライドを優先してしまう傾向があります。"}
}

all_cards = MAJOR_ARCANA.copy()

card_id = 23
for suit_key, suit_data in SUITS.items():
    for num, rank_data in RANKS.items():
        name_jp = f"{suit_data['jp']}{rank_data['jp']}"
        name_en = f"{rank_data['en']} {suit_data['en']}"
        
        # Merge meaning based on rank's nature and suit's theme
        meaning_up = f"{suit_data['theme']}における{rank_data['meaning_up']}"
        meaning_rev = f"{suit_data['theme']}の側面での{rank_data['meaning_rev']}"
        
        love_up = f"{suit_data['upright_context']}によって、{rank_data['love_up']}"
        love_rev = f"{suit_data['reversed_context']}が影響し、{rank_data['love_rev']}"

        card = {
            "id": card_id,
            "name_jp": f"{name_jp} ({name_en})",
            "name_en": name_en,
            "arcana_type": "minor",
            "suit": suit_key,
            "number": num,
            "meaning_upright": meaning_up,
            "meaning_reversed": meaning_rev,
            "love_context_upright": love_up,
            "love_context_reversed": love_rev
        }
        all_cards.append(card)
        card_id += 1


os.makedirs("/Users/isamumatsuyama/Documents/development/en-shirube-system/backend/data", exist_ok=True)
with open("/Users/isamumatsuyama/Documents/development/en-shirube-system/backend/data/tarot_cards.json", "w", encoding="utf-8") as f:
    json.dump(all_cards, f, ensure_ascii=False, indent=2)

print("Successfully generated data/tarot_cards.json with 78 cards.")
