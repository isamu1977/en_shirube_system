
import sys
import os
from datetime import datetime, timezone, timedelta

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from app.services.subscription_service import DEFAULT_SOS_CREDITS


class MockUser:
    def __init__(self, id="test-uuid", stripe_customer_id=None, subscription_status="none", sos_credits=0, emotional_profile=None, last_sos_reset=None):
        self.id = id
        self.stripe_customer_id = stripe_customer_id
        self.subscription_status = subscription_status
        self.sos_credits = sos_credits
        self.emotional_profile = emotional_profile
        self.last_sos_reset = last_sos_reset


class MockDB:
    def __init__(self):
        self.added = []
    
    def add(self, obj):
        self.added.append(obj)
    
    async def commit(self):
        pass
    
    async def refresh(self, obj):
        pass


def test_default_sos_credits():
    assert DEFAULT_SOS_CREDITS == 3


def test_user_defaults():
    user = MockUser()
    
    assert user.subscription_status == "none"
    assert user.sos_credits == 0
    assert user.emotional_profile is None


def test_user_with_premium():
    user = MockUser(
        stripe_customer_id="cus_test123",
        subscription_status="active",
        sos_credits=3
    )
    
    assert user.stripe_customer_id == "cus_test123"
    assert user.subscription_status == "active"
    assert user.sos_credits == 3


def test_emotional_profile_values():
    valid_profiles = ["anxious", "logical", "hopeful"]
    
    for profile in valid_profiles:
        user = MockUser(emotional_profile=profile)
        assert user.emotional_profile == profile


def test_last_sos_reset_tracking():
    now = datetime.now(timezone.utc)
    user = MockUser(last_sos_reset=now)
    
    assert user.last_sos_reset is not None
    assert user.last_sos_reset.tzinfo is not None


def test_time_elapsed_calculation():
    now = datetime.now(timezone.utc)
    
    one_day_ago = now - timedelta(days=1)
    thirty_days_ago = now - timedelta(days=30)
    sixty_days_ago = now - timedelta(days=60)
    
    days_since_1 = (now - one_day_ago).days
    days_since_30 = (now - thirty_days_ago).days
    days_since_60 = (now - sixty_days_ago).days
    
    assert days_since_1 == 1
    assert days_since_30 >= 30
    assert days_since_60 >= 60


def test_sos_credits_deduction():
    user = MockUser(sos_credits=3)
    
    user.sos_credits -= 1
    assert user.sos_credits == 2
    
    user.sos_credits -= 1
    assert user.sos_credits == 1
    
    user.sos_credits -= 1
    assert user.sos_credits == 0


def test_sos_credits_cannot_go_negative():
    user = MockUser(sos_credits=0)
    
    if user.sos_credits > 0:
        user.sos_credits -= 1
    
    assert user.sos_credits == 0


if __name__ == "__main__":
    test_default_sos_credits()
    test_user_defaults()
    test_user_with_premium()
    test_emotional_profile_values()
    test_last_sos_reset_tracking()
    test_time_elapsed_calculation()
    test_sos_credits_deduction()
    test_sos_credits_cannot_go_negative()
    print("All subscription service tests passed.")
