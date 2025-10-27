from datetime import datetime, timezone, timedelta
import time


class RateLimiter:
    def __init__(self, window: int, max_requests: int):
        self.window = window
        self.max_requests = max_requests
        self.requests = []

    def acquire(self):
        now = datetime.now(timezone.utc)

        self.clean_old_requests(now)

        if len(self.requests) >= self.max_requests:
            oldest = self.requests[0]
            wait_time = self.window - (now - oldest)
            time.sleep(wait_time.total_seconds())

            now = datetime.now(timezone.utc)
            self.clean_old_requests(now)

        self.requests.append(now)

    def clean_old_requests(self, now):
        while len(self.requests) > 0 and self.requests[0] <= now - timedelta(
            seconds=self.window
        ):
            self.requests.pop(0)
