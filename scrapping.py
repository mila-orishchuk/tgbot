import requests
from bs4 import BeautifulSoup as bs
from collections import namedtuple

Recipe = namedtuple('Recipe', ['link', 'title'])


def get_recipes(URL) -> Recipe:
    while URL:
        page = get_page_content(URL)
        for recipe in get_recipe_from_page(page):
            yield recipe
        URL = get_next_page(page)


def get_recipe_from_page(soup) -> Recipe:
    links = get_recipe_links(soup)
    for one_link in links:
        one_link = one_link.find('h5', {'class': "hdr"}).find('a')
        link = one_link.get('href')
        title = one_link.text
        yield Recipe(link, title)


def get_next_page(page):
    if page == page.find('a', {'class': "next page-numbers"}):
        print(URL + page.get('href'))
        return URL + page.get('href')


def get_page_content(URL, attempts=3):
    if attempts < 0:
        raise Exception('No attempts')

    response = requests.get(URL)
    if not response.ok:
        return get_page_content(URL, attempts - 1)

    return bs(response.content, 'html.parser')


def get_recipe_links(soup):
    links = soup.findAll('div', {'class': "info col"})
    return links


if __name__ == '__main__':
    URL = 'https://menunedeli.ru/zavtrak/'
    recipes = get_recipes(URL)
    content = get_recipe_from_page(get_page_content(URL))
    recipes_list = list(recipes)
    print(len(recipes_list))
