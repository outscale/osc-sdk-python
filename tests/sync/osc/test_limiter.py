import datetime
from concurrent.futures import ThreadPoolExecutor

from osc_sdk_python import RateLimiter

i = 0


def test_fast(monkeypatch):
    with monkeypatch.context() as m:
        was_called = []

        def mock_sleep(t):
            was_called.append(t)
            assert t > 0
            return

        i = 0

        class MockDateTimeFast(datetime.datetime):
            @classmethod
            def now(cls, tz=None):
                global i
                i += 1
                return cls(2022, 1, 1, microsecond=i, tzinfo=tz)

        m.setattr("time.sleep", mock_sleep)

        rl = RateLimiter(
            datetime.timedelta(seconds=1), 5, datetime_cls=MockDateTimeFast
        )
        for i in range(10):
            rl.acquire()

        assert len(rl.requests) > 5
        assert len(was_called) > 0


def test_slow(monkeypatch):
    with monkeypatch.context() as m:
        was_called = []

        def mock_sleep(t):
            was_called.append(t)
            assert t > 0
            return

        i = 0

        class MockDateTimeSlow(datetime.datetime):
            @classmethod
            def now(cls, tz=None):
                global i
                i += 1
                return cls(2022 + i, 1, 1, tzinfo=tz)

        m.setattr("time.sleep", mock_sleep)

        rl = RateLimiter(
            datetime.timedelta(seconds=1), 5, datetime_cls=MockDateTimeSlow
        )
        for i in range(10):
            rl.acquire()

        assert len(rl.requests) <= 1
        assert len(was_called) == 0


def test_refill_after_window():
    """Test old requests are removed once the limiter window has passed"""
    class MockDateTime(datetime.datetime):
        @classmethod
        def now(cls, tz=None):
            return cls(2022, 1, 1, 0, 0, 2, tzinfo=tz)

    rl = RateLimiter(datetime.timedelta(seconds=1), 5, datetime_cls=MockDateTime)
    rl.requests = [
        MockDateTime(2022, 1, 1, 0, 0, 0, tzinfo=datetime.timezone.utc),
        MockDateTime(2022, 1, 1, 0, 0, 1, 500000, tzinfo=datetime.timezone.utc),
    ]

    rl.acquire()

    assert len(rl.requests) == 2
    print(rl.requests)
    assert rl.requests[0] == MockDateTime(
        2022, 1, 1, 0, 0, 1, 500000, tzinfo=datetime.timezone.utc
    )
    assert rl.requests[1] == MockDateTime.now(datetime.timezone.utc)


def test_concurrent_acquire_completes_without_deadlock(monkeypatch):
    """Test concurrent sync callers complete without deadlocking"""
    with monkeypatch.context() as m:
        sleep_calls = []

        def mock_sleep(t):
            sleep_calls.append(t)

        m.setattr("time.sleep", mock_sleep)

        rl = RateLimiter(datetime.timedelta(seconds=1), 1)

        with ThreadPoolExecutor(max_workers=3) as executor:
            futures = [executor.submit(rl.acquire) for _ in range(3)]
            for future in futures:
                future.result(timeout=1)

        assert len(rl.requests) == 3
        assert len(sleep_calls) == 2
