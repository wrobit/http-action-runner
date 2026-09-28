from functools import wraps

import requests

DEFAULT_MAX_RETRIES = 5
DEFAULT_REQUEST_COUNT = 0

ATTEMPTS_FAILED_ERROR = "All request attempts failed"


def retry(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except requests.RequestException:
                    print(f"Attempt {attempt + 1} failed")
            raise RuntimeError(ATTEMPTS_FAILED_ERROR)

        return wrapper

    return decorator


def count_requests(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global request_count
        request_count += 1

        return func(*args, **kwargs)

    return wrapper
