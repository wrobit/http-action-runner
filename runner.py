import requests

from helpers import DEFAULT_MAX_RETRIES, retry


class Runner:
    path = None
    number_of_retries = DEFAULT_MAX_RETRIES

    def __init__(self, path, number_of_retries=DEFAULT_MAX_RETRIES):
        self.path = path
        self.number_of_retries = number_of_retries

    def get_path(self):
        return self.path

    def set_path(self, path):
        self._path = path

    @retry(number_of_retries)
    async def get(self):
        return requests.get(f"{self.path}/test")
