
import sys
import os

# Adjust import according to structure
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from app.services.prompt_builder import build_lead_magnet_prompt

def test_build_lead_magnet_prompt_upright():
    card_name = "愚者 (The Fool)"
    is_reversed = False
    love_context = "彼は過去のしがらみを捨て、フラットな状態です。"
    
    prompt = build_lead_magnet_prompt(card_name, is_reversed, love_context)
    
    assert "愚者 (The Fool) (正位置)" in prompt
    assert love_context in prompt
    assert "縁しるべ" in prompt
    assert "クリフハンガー" in prompt

def test_build_lead_magnet_prompt_reversed():
    card_name = "塔 (The Tower)"
    is_reversed = True
    love_context = "予期せぬ出来事によって、混乱の極みにいます。"
    
    prompt = build_lead_magnet_prompt(card_name, is_reversed, love_context)
    
    assert "塔 (The Tower) (逆位置)" in prompt
    assert love_context in prompt
    assert "縁しるべ" in prompt
    assert "クリフハンガー" in prompt

if __name__ == "__main__":
    test_build_lead_magnet_prompt_upright()
    test_build_lead_magnet_prompt_reversed()
    print("All tests passed.")
