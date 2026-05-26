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
