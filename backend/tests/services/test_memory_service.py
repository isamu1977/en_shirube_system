
import sys
import os
from datetime import datetime, timezone, timedelta

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from app.services.memory_service import MemoryService


def test_calculate_time_elapsed_today():
    service = MemoryService()
    past = datetime.now(timezone.utc)
    
    result = service._calculate_time_elapsed(past)
    
    assert result == "今日"


def test_calculate_time_elapsed_yesterday():
    service = MemoryService()
    past = datetime.now(timezone.utc) - timedelta(days=1)
    
    result = service._calculate_time_elapsed(past)
    
    assert result == "昨日"


def test_calculate_time_elapsed_days():
    service = MemoryService()
    past = datetime.now(timezone.utc) - timedelta(days=5)
    
    result = service._calculate_time_elapsed(past)
    
    assert result == "5日前"


def test_calculate_time_elapsed_one_week():
    service = MemoryService()
    past = datetime.now(timezone.utc) - timedelta(days=7)
    
    result = service._calculate_time_elapsed(past)
    
    assert result == "1週間前"


def test_calculate_time_elapsed_weeks():
    service = MemoryService()
    past = datetime.now(timezone.utc) - timedelta(days=21)
    
    result = service._calculate_time_elapsed(past)
    
    assert result == "3週間前"


def test_calculate_time_elapsed_one_month():
    service = MemoryService()
    past = datetime.now(timezone.utc) - timedelta(days=30)
    
    result = service._calculate_time_elapsed(past)
    
    assert result == "1ヶ月前"


def test_calculate_time_elapsed_months():
    service = MemoryService()
    past = datetime.now(timezone.utc) - timedelta(days=60)
    
    result = service._calculate_time_elapsed(past)
    
    assert result == "2ヶ月前"


def test_calculate_time_elapsed_year():
    service = MemoryService()
    past = datetime.now(timezone.utc) - timedelta(days=400)
    
    result = service._calculate_time_elapsed(past)
    
    assert result == "1年前"


if __name__ == "__main__":
    test_calculate_time_elapsed_today()
    test_calculate_time_elapsed_yesterday()
    test_calculate_time_elapsed_days()
    test_calculate_time_elapsed_one_week()
    test_calculate_time_elapsed_weeks()
    test_calculate_time_elapsed_one_month()
    test_calculate_time_elapsed_months()
    test_calculate_time_elapsed_year()
    print("All memory service tests passed.")
