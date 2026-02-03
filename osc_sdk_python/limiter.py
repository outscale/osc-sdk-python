from datetime import datetime, timezone, timedelta
import time


class RateLimiter:
    def __init__(self, window: timedelta, max_requests: int, datetime_cls=datetime):
        self.datetime_cls = datetime_cls
        self.window: timedelta = window
        self.max_requests: int = max_requests
        self.requests = []

    def acquire(self):
        now = self.datetime_cls.now(timezone.utc)

        self.clean_old_requests(now)

        if len(self.requests) >= self.max_requests:
            oldest = self.requests[0]
            wait_time = self.window - (now - oldest)
            time.sleep(wait_time.total_seconds())

            now = self.datetime_cls.now(timezone.utc)
            self.clean_old_requests(now)

        self.requests.append(now)

    def clean_old_requests(self, now):
        while len(self.requests) > 0 and self.requests[0] <= now - self.window:
            self.requests.pop(0)
