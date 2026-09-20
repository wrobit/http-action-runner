import requests
from pytest import raises

import main


def test_count_requests_returns_original_value():
    main.request_count = 0

    @main.count_requests
    def test_fn():
        return "bar"

    assert test_fn() == "bar"


def test_count_requests_increments_counter():
    main.request_count = 0
    should_be_called_times = 5

    @main.count_requests
    def test_fn():
        return "bar"

    for i in range(should_be_called_times - 1):
        test_fn()

    assert main.request_count == should_be_called_times


def test_retry_returns_original_value():
    @main.retry(main.max_retries)
    @main.count_requests
    def test_fn():
        return "bar"

    assert test_fn() == "bar"


def test_retry_attempt_fail():
    local_retries = 0

    @main.retry(main.max_retries)
    def test_fn():
        nonlocal local_retries
        local_retries += 1
        raise requests.RequestException

    with raises(RuntimeError, match=main.attempts_failed_error):
        test_fn()

    assert local_retries == main.max_retries
