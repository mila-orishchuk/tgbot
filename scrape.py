from service.scrape_service import WebScraper
from service.parser import parse

BASE_API_SEARCH_URL = 'https://menunedeli.ru'

scraper = WebScraper({
    "parse": parse
}, BASE_API_SEARCH_URL)

scraper.path = '/zavtrak'
# scraper.get_pages_links()
scraper.get_articles()

# scraper.set_path('/obed')
# scraper.get_articles()

# scraper.set_path('/uzhin')
# scraper.get_articles()
