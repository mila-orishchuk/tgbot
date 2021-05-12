from service.scrape_service import WebScraper
from service.parser import parse
from service.db_service import DbService
from base import Session

BASE_API_SEARCH_URL = 'https://menunedeli.ru'

session = Session()
db = DbService(session)

scraper = WebScraper({
    "parse": parse,
    "db": db
}, BASE_API_SEARCH_URL)

path_list = ['/zavtrak']

for scraper.path in path_list:
    print(len(db.get_all_recipes()))
    scraper.get_articles()
    print(len(db.get_all_recipes()))

    
# scraper.path = '/zavtrak'
# scraper.get_pages_links()
# scraper.set_path('/obed')
# scraper.get_articles()

# scraper.set_path('/uzhin')
# scraper.get_articles()
