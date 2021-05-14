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


class ScrapeService:
    '''Initialize the scraper with a URL.
        Args:
            url (str): full HTML link to a page of search results.'''

    _path = '/'

    _db: DbService

    def __init__(self, deps: dict, url: str):
        self._parser = deps["parser"]
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

    def save(self, data: List[dict], urls: List[str], category):
        to_save = []
        try:
            for recipe_data in data:
                if recipe_data["url"] not in urls:
                    recipe_data["categories"] = [category]
                    to_save.append(recipe_data)
                else:
                    recipe = self._db.get_by_url(recipe_data["url"])
                    recipe.categories.append(category)
                    to_save.append(recipe_data)
            if to_save:
                self._db.save_recipes(to_save)
        except Exception as e:
            print(e)

    def get_articles(self):
        categories = self._db.get_all_categoties()
        urls = self._db.get_all_urls()
        for cat in categories:
            page = 21
            while True:
                try:
                    code, content = self._request(
                        f'{self._url}/{cat.url}/page/{page}')
                    if code >= 400:
                        raise HTTPError(f'HTTP error occurred: {code}')
                    data = self._parser.get_data(content)
                    self.save(data, urls, cat)
                    page += 1
                except HTTPError as http_err:
                    print(http_err)
                    break
                except Exception as e:
                    print(e)
                    break
