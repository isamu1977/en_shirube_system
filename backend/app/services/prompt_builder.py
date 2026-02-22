from typing import List

from app.services.draw_service import SPREAD_7_POSITIONS, RETENTION_TRIGGER_TEXT, CardDraw


def build_lead_magnet_prompt(card_name_jp: str, is_reversed: bool, love_context: str) -> str:
    """
    Constructs the strictly formatted Japanese system prompt for the Lead Magnet (1-card) reading.
    
    Args:
        card_name_jp: The Japanese name of the card.
        is_reversed: True if the card was drawn reversed, False if upright.
        love_context: The specific psychological love context of the card in its drawn orientation.
        
    Returns:
        The exact string prompt to be sent to the LLM.
    """
    orientation_str = "逆位置" if is_reversed else "正位置"
    
    return f"""あなたは「縁しるべ」の専属AI案内人です。占い師のようなスピリチュアルで大げさな言葉遣いや、安っぽいオカルト表現は一切避けてください。
心理カウンセラーのように深く寄り添い、かつ論理的で落ち着いたトーン（洗練された丁寧語）で話してください。ターゲットは、元カレとの復縁や現在の恋愛関係に深く悩む大人の女性です。

以下の引いたカードと、その恋愛における心理的意味をベースにして、彼の「今の本音」を1〜2段落で簡潔に伝えてください。

【厳守事項】
1. 文字数: 200〜300文字程度。短く、読みやすくすること。
2. 冒頭: 最初の一文で、彼の現在の心理状態や直面している感情をズバリと指摘してください。
3. 共感: ユーザーが「このAIは私の辛い状況を本当に理解してくれている」と感じるような、深い共感のニュアンスを織り交ぜること。
4. 結論禁止: 最終的な結論（復縁できるかどうか、彼が戻ってくるか）は絶対に書かないこと。
5. クリフハンガー: 最後の一文は、彼の心の奥底にある「まだ見せていない別の感情」や「二人の関係の隠れた障害」を匂わせ、ユーザーが続き（詳細な鑑定）を知りたくてたまらなくなる状態（クリフハンガー）で終わらせること。

【入力データ】
- 引いたカード: {card_name_jp} ({orientation_str})
- カードの恋愛心理的意味: {love_context}
"""


def build_standard_spread_prompt(draws: List[CardDraw], cards_data: dict, card_names: dict) -> str:
    """
    Constructs the Japanese system prompt for the Standard Spread (7-card) reading.
    
    Args:
        draws: List of CardDraw objects with card_id and is_reversed.
        cards_data: Dict mapping card_number to Card objects.
        card_names: Dict mapping card_number to Japanese card name.
        
    Returns:
        The exact string prompt to be sent to the LLM.
    """
    cards_section = []
    for i, draw in enumerate(draws):
        position = SPREAD_7_POSITIONS[i]
        card_name = card_names.get(draw.card_id, f"Card {draw.card_id}")
        orientation_str = "逆位置" if draw.is_reversed else "正位置"
        weight = position["weight"]
        
        cards_section.append(
            f"【Position {i+1}】 {position['jp']} ({position['en']})\n"
            f"カード: {card_name} ({orientation_str})\n"
            f"Weight Guide: {weight}"
        )
    
    cards_text = "\n\n".join(cards_section)
    
    return f"""あなたは「縁しるべ」の専属AI案内人です。心理カウンセラーとして深く寄り添い、かつ論理的で落ち着いたトーンで話してください。

以下の7枚のカードを読み解き、恋愛・復縁についての鑑定結果を出力してください。

{cards_text}

【出力要件】
1. 各カードについて、2〜3段落の説明を書いてください。
2. カード間の関連性を考慮し、ストーリーとして纏まりのある内容にしてください。
3. 心理カウンセラーのように、ユーザーの心に響く解説をしてください。
4. 最後に、具体的なアクションプラン（次のアクション）を1つだけ提示してください。

【最終段落】
{RETENTION_TRIGGER_TEXT}
"""
