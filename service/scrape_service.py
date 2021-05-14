import requests
from requests.exceptions import HTTPError
import logging
from service.db_service import DbService
from typing import List

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0', 'accept': '*/*'}


class WebScraper:
    '''Initialize the scraper with a URL.
        Args:
            url (str): full HTML link to a page of search results.'''

    _path = '/'

    _db: DbService

    def __init__(self, deps: dict, url: str):
        self._parse = deps["parse"]
        self._db = deps["db"]
        self._url = url

    @staticmethod
    def _request(url: str) -> (int, str):
        print(f'request to {url}')
        response = requests.get(url, headers=HEADERS)
        return response.status_code, response.content

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path: str):
        self._path = path

    def save(self, data: List[dict]):
        to_save = []
        try:
            for recipe_data in data:
                to_save.append(recipe_data)
            self._db.save_recipes(to_save)
        except Exception as e:
            print(e)

    def get_articles(self):
        page = 20
        while True:
            try:
                code, content = self._request(
                    f'{self._url}{self._path}/page/{page}')
                if code >= 400:
                    raise HTTPError(f'HTTP error occurred: {code}')
                data = self._parse(content)
                self.save(data)
                page += 1
            except HTTPError as http_err:
                print(http_err)
                break
            except Exception as e:
                print(e)
                break
