import pytest
import requests

import main


MAX_RETRIES = 3


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


def test_retry_returns_original_value():
    @main.retry(MAX_RETRIES)
    def test_fn():
        return "bar"

    assert test_fn() == "bar"


def test_retry_raises_runtime_error_after_all_attempts_fail():
    failed_attempts = 0

    @main.retry(MAX_RETRIES)
    def test_fn():
        nonlocal failed_attempts
        failed_attempts += 1
        raise requests.RequestException

    with pytest.raises(RuntimeError, match=main.ATTEMPTS_FAILED_ERROR):
        test_fn()

    assert failed_attempts == MAX_RETRIES


def test_retry_returns_value_after_some_failures():
    failed_attempts = 0
    total_calls = 0
    failures_before_success = 2

    @main.retry(MAX_RETRIES)
    def test_fn():
        nonlocal total_calls
        nonlocal failed_attempts
        total_calls += 1
        if failed_attempts == failures_before_success:
            return "foo"
        failed_attempts += 1
        raise requests.RequestException

    assert test_fn() == "foo"
    assert total_calls == MAX_RETRIES
    assert failed_attempts == failures_before_success
