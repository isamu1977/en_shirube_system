
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from app.services.sos_service import SOSService, SOS_ERROR_CODES


def test_sos_error_codes():
    assert SOS_ERROR_CODES["SOS_CREDITS_EXHAUSTED"] == "SOS_CREDITS_EXHAUSTED"
    assert SOS_ERROR_CODES["NOT_SUBSCRIBER"] == "NOT_SUBSCRIBER"
    assert SOS_ERROR_CODES["INVALID_USER"] == "INVALID_USER"


def test_build_panic_prompt_upright():
    service = SOSService()
    
    prompt = service.build_panic_prompt("愚者", False)
    
    assert "愚者" in prompt
    assert "正位置" in prompt
    assert "パニック" in prompt or "不安" in prompt


def test_build_panic_prompt_reversed():
    service = SOSService()
    
    prompt = service.build_panic_prompt("塔", True)
    
    assert "塔" in prompt
    assert "逆位置" in prompt


def test_build_panic_prompt_with_anxious_profile():
    service = SOSService()
    
    prompt = service.build_panic_prompt("愚者", False, "anxious")
    
    assert "パニック" in prompt or "anxious" in prompt.lower()


def test_build_panic_prompt_with_logical_profile():
    service = SOSService()
    
    prompt = service.build_panic_prompt("愚者", False, "logical")
    
    assert "論理" in prompt or "logical" in prompt.lower()


def test_build_panic_prompt_with_hopeful_profile():
    service = SOSService()
    
    prompt = service.build_panic_prompt("愚者", False, "hopeful")
    
    assert "希望" in prompt or "hopeful" in prompt.lower()


def test_build_panic_prompt_contains_micro_action():
    service = SOSService()
    
    prompt = service.build_panic_prompt("愚者", False)
    
    assert "メッセージ" in prompt or "アクション" in prompt or "micro" in prompt.lower()


def test_build_panic_prompt_contains_grounding():
    service = SOSService()
    
    prompt = service.build_panic_prompt("愚者", False)
    
    assert "深呼吸" in prompt or " grounding " in prompt.lower()


def test_build_panic_prompt_message_not_to_send():
    service = SOSService()
    
    prompt = service.build_panic_prompt("愚者", False)
    
    assert "送らない" in prompt or "控える" in prompt


def test_build_panic_prompt_short_length():
    service = SOSService()
    
    prompt = service.build_panic_prompt("愚者", False)
    
    assert len(prompt) < 2000


if __name__ == "__main__":
    test_sos_error_codes()
    test_build_panic_prompt_upright()
    test_build_panic_prompt_reversed()
    test_build_panic_prompt_with_anxious_profile()
    test_build_panic_prompt_with_logical_profile()
    test_build_panic_prompt_with_hopeful_profile()
    test_build_panic_prompt_contains_micro_action()
    test_build_panic_prompt_contains_grounding()
    test_build_panic_prompt_message_not_to_send()
    test_build_panic_prompt_short_length()
    print("All SOS service tests passed.")
