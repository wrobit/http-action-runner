from functools import wraps

import requests

max_retries = 5
request_count = 0


def main():
    for i in range(10):
        method_to_be_counted(i)

    print(f"Number of requests called: {request_count}")


attempts_failed_error = "All request attempts failed"


def retry(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except requests.RequestException:
                    print(f"Attempt {attempt + 1} failed")
            raise RuntimeError(attempts_failed_error)

        return wrapper

    return decorator


def count_requests(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global request_count
        request_count += 1

        return func(*args, **kwargs)

    return wrapper


@retry(max_retries)
@count_requests
def method_to_be_counted(i):
    yield


if __name__ == "__main__":
    main()
