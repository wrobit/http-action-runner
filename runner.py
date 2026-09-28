import requests

from helpers import DEFAULT_MAX_RETRIES, retry


class Runner:
    def __init__(self, path, number_of_retries=DEFAULT_MAX_RETRIES):
        self.path = path
        self.number_of_retries = number_of_retries

    def __str__(self):
        return f"{self.path}-{self.number_of_retries}"

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path

    @property
    def number_of_retries(self):
        return self._number_of_retries

    @number_of_retries.setter
    def number_of_retries(self, number_of_retries):
        self._number_of_retries = number_of_retries

    @classmethod
    @retry(number_of_retries)
    async def get(self):
        return requests.get(f"{self.path}/test")
