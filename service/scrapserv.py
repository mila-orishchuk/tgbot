import json
import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0', 'accept': '*/*'}


class Webscraper:
    '''Initialize the scraper with a URL from the results of a property
        search performed on https://menunedeli.ru/.
        Args:
            url (str): full HTML link to a page of rightmove search results.'''

    def __init__(self, url: str):
        self.soup = soup
        self._status_code
        self._first_page = self._request(url)
        self._url = url
        self._validate_url()

    @staticmethod
    def _request(url: str):
        response = requests.get(url, headers=HEADERS)
        return response.status_code, response.content