from helpers import (
    DEFAULT_MAX_RETRIES,
    DEFAULT_REQUEST_COUNT,
    count_requests,
    retry,
)


def main():
    for i in range(10):
        method_to_be_counted(i)

    print(f"Number of requests called: {DEFAULT_REQUEST_COUNT}")


@retry(DEFAULT_MAX_RETRIES)
@count_requests
def method_to_be_counted(i):
    yield


if __name__ == "__main__":
    main()
