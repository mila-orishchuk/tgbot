from bs4 import BeautifulSoup
from typing import List


# def get_last_page(soup: str):
#     print(soup.find('class': 'page-numbers').find_previous_sibling().text)


def get_soup(content: str) -> BeautifulSoup:
    return BeautifulSoup(content.decode('utf-8'), 'html.parser')


def get_ingredients(ingredients_nodes: List[BeautifulSoup]) -> List[dict]:
    ingredients = []
    for ingredient in ingredients_nodes:
        ingredients.append({
            'name': get_item_by_class(ingredient, 'name'),
            'description': ingredient.text
        })

    return ingredients


def get_recipe(article: BeautifulSoup) -> dict:
    recipe = None
    try:
        hdr = article.find('div', {'class': 'info col'}).find(
            'h5', {'class': 'hdr'}).find('a')
        recipe = {
            'name': hdr.text,
            'url': hdr.get('href'),
            'image': article.find(
                'div', {'class': 'img col-auto'}).find('img').get('src'),
            'cooking_time': article.find(
                'ul', {'class': 'params-detail-lst row'}).find('span', {'class': 'duration'}).text,
            'ingredients': get_ingredients(
                article.find('ul', {'class': 'ingredients-lst'}
                             ).findAll('span', {'itemprop': 'recipeIngredient'}))
        }
    except:
        pass
    return recipe


def get_item_by_class(ingredient: BeautifulSoup, class_name: str) -> str:
    item = ingredient.find('span', {'class': class_name})
    return item.text if item else ''


def get_recipes(soup: BeautifulSoup) -> List[dict]:
    recipes = []
    articles_nodes = soup.findAll('article')
    for article_node in articles_nodes:
        recipe = get_recipe(article_node)
        if recipe:
            recipes.append(recipe)

    return recipes


def parse(content: str) -> List[dict]:
    soup_obj = get_soup(content)
    return get_recipes(soup_obj)
