import runner

PATH = "https://test:0000/api"
NUMBER_OF_RETRIES = 10


def test_runner_initialization():
    internal_runner = runner.Runner(PATH, NUMBER_OF_RETRIES)
    assert internal_runner.path == PATH
    assert internal_runner.number_of_retries == NUMBER_OF_RETRIES


def test_runner_set_values():
    internal_runner = runner.Runner(PATH, NUMBER_OF_RETRIES)
    custom_path = "https://custom:0000/api"
    custom_number_of_retries = 20

    internal_runner.path = custom_path
    assert internal_runner.path == custom_path

    internal_runner.number_of_retries = custom_number_of_retries
    assert internal_runner.number_of_retries == custom_number_of_retries
