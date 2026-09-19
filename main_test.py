import main


def test_count_requests_returns_original_value():
    main.request_count = 0

    @main.count_requests
    def test_function():
        return "bar"

    assert test_function() == "bar"


def test_count_requests_increments_counter():
    number_of_calls = 5

    @main.count_requests
    def test_function():
        return "bar"

    for i in range(number_of_calls - 1):
        test_function()

    assert main.request_count == number_of_calls
