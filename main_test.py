import requests
from pytest import raises

import main


def test_count_requests_returns_original_value():
    main.request_count = 0

    @main.count_requests
    def test_fn():
        return "bar"

    assert test_fn() == "bar"


def test_count_requests_increments_count_for_each_call():
    main.request_count = 0
    should_be_called_times = 5

    @main.count_requests
    def test_fn():
        return "bar"

    for i in range(should_be_called_times):
        test_fn()

    assert main.request_count == should_be_called_times


max_retries = 3


def test_retry_returns_original_value():
    @main.retry(max_retries)
    @main.count_requests
    def test_fn():
        return "bar"

    assert test_fn() == "bar"


def test_retry_raises_runtime_error_after_all_attempts_fail():
    local_retries = 0

    @main.retry(max_retries)
    def test_fn():
        nonlocal local_retries
        local_retries += 1
        raise requests.RequestException

    with raises(RuntimeError, match=main.attempts_failed_error):
        test_fn()

    assert local_retries == max_retries


def test_retry_returns_value_after_some_failures():
    local_retries = 0
    success_after_retries = 2

    @main.retry(max_retries)
    def test_fn():
        nonlocal local_retries
        if local_retries == success_after_retries:
            return "foo"
        else:
            local_retries += 1
            raise requests.RequestException

    assert test_fn() == "foo"
    assert local_retries == success_after_retries
