from datetime import datetime, timezone, timedelta
import asyncio
import time
from threading import Lock


class RateLimiter:
    def __init__(self, window: timedelta, max_requests: int, datetime_cls=datetime):
        self.datetime_cls = datetime_cls
        self.window: timedelta = window
        self.max_requests: int = max_requests
        self.requests = []
        self._lock = Lock()
        self._async_lock = None

    def acquire(self):
        with self._lock:
            now = self.datetime_cls.now(timezone.utc)

            self.clean_old_requests(now)

            if len(self.requests) >= self.max_requests:
                oldest = self.requests[0]
                wait_time = self.window - (now - oldest)
                time.sleep(wait_time.total_seconds())

                now = self.datetime_cls.now(timezone.utc)
                self.clean_old_requests(now)

            self.requests.append(now)

    async def async_acquire(self):
        if self._async_lock is None:
            self._async_lock = asyncio.Lock()

        async with self._async_lock:
            now = self.datetime_cls.now(timezone.utc)

            self.clean_old_requests(now)

            if len(self.requests) >= self.max_requests:
                oldest = self.requests[0]
                wait_time = self.window - (now - oldest)
                await asyncio.sleep(wait_time.total_seconds())

                now = self.datetime_cls.now(timezone.utc)
                self.clean_old_requests(now)

            self.requests.append(now)

    def clean_old_requests(self, now):
        while len(self.requests) > 0 and self.requests[0] <= now - self.window:
            self.requests.pop(0)
