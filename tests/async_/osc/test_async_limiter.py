import asyncio
import datetime

from osc_sdk_python import RateLimiter

i = 0


def test_async_fast(monkeypatch):
    async def run():
        with monkeypatch.context() as m:
            was_called = []

            async def mock_sleep(t):
                was_called.append(t)
                assert t > 0

            class MockDateTimeFast(datetime.datetime):
                @classmethod
                def now(cls, tz=None):
                    global i
                    i += 1
                    return cls(2022, 1, 1, microsecond=i, tzinfo=tz)

            m.setattr("asyncio.sleep", mock_sleep)

            rl = RateLimiter(
                datetime.timedelta(seconds=1), 5, datetime_cls=MockDateTimeFast
            )
            for _ in range(10):
                await rl.async_acquire()

            assert len(rl.requests) > 5
            assert len(was_called) > 0

    asyncio.run(run())


def test_async_slow(monkeypatch):
    async def run():
        with monkeypatch.context() as m:
            was_called = []

            async def mock_sleep(t):
                was_called.append(t)
                assert t > 0

            class MockDateTimeSlow(datetime.datetime):
                @classmethod
                def now(cls, tz=None):
                    global i
                    i += 1
                    return cls(2022 + i, 1, 1, tzinfo=tz)

            m.setattr("asyncio.sleep", mock_sleep)

            rl = RateLimiter(
                datetime.timedelta(seconds=1), 5, datetime_cls=MockDateTimeSlow
            )
            for _ in range(10):
                await rl.async_acquire()

            assert len(rl.requests) <= 1
            assert len(was_called) == 0

    asyncio.run(run())


def test_async_refill_after_window():
    """Test old requests are removed once the async limiter window has passed"""
    async def run():
        class MockDateTime(datetime.datetime):
            @classmethod
            def now(cls, tz=None):
                return cls(2022, 1, 1, 0, 0, 2, tzinfo=tz)

        rl = RateLimiter(datetime.timedelta(seconds=1), 5, datetime_cls=MockDateTime)
        rl.requests = [
            MockDateTime(2022, 1, 1, 0, 0, 0, tzinfo=datetime.timezone.utc),
            MockDateTime(2022, 1, 1, 0, 0, 1, 500000, tzinfo=datetime.timezone.utc),
        ]

        await rl.async_acquire()

        assert len(rl.requests) == 2
        assert rl.requests[0] == MockDateTime(
            2022, 1, 1, 0, 0, 1, 500000, tzinfo=datetime.timezone.utc
        )
        assert rl.requests[1] == MockDateTime.now(datetime.timezone.utc)

    asyncio.run(run())


def test_async_concurrent_acquire_completes_without_deadlock(monkeypatch):
    """Test concurrent async callers complete without deadlocking"""
    async def run():
        with monkeypatch.context() as m:
            sleep_calls = []

            async def mock_sleep(t):
                sleep_calls.append(t)

            m.setattr("asyncio.sleep", mock_sleep)

            rl = RateLimiter(datetime.timedelta(seconds=1), 1)

            await asyncio.wait_for(
                asyncio.gather(*(rl.async_acquire() for _ in range(3))),
                timeout=1,
            )

            assert len(rl.requests) == 3
            assert len(sleep_calls) == 2

    asyncio.run(run())
