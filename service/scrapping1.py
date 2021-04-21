import json
import requests
from entities.recipe import Recipe
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0', 'accept': '*/*'}


def get_soup(url):
    response = requests.get(url, headers=HEADERS)
    if response.status_code > 400:
        raise HTTPError(f'HTTP error occurred: {response.status_code}')
    return BeautifulSoup(response.content.decode('utf-8'), 'html.parser')


def get_recipe_links(soup):
    links = soup.findAll('div', {'class': "info col"})
    ingredients_nodes = soup.findAll('ul', {'class': "ingredients-lst"})
    return zip(ingredients_nodes, links)


def get_item_by_class(ingredient, class_name):
    item = ingredient.find('span', {'class': class_name})
    return item.text if item else ''


def save_recipes_to_doc(soup, recipes):
    for ingredients_node, one_link in get_recipe_links(soup):
        recipe_ingredients = []
        ingredients = ingredients_node.findAll(
            'span', {'itemprop': "recipeIngredient"})
        for ingredient in ingredients:
            
            recipe_ingredients.append({
                'name': get_item_by_class(ingredient, 'name'),
                'quantity': get_item_by_class(ingredient, 'value'),
                'unit': get_item_by_class(ingredient, 'type') or get_item_by_class(ingredient, 'amount')
            })

        link_node = one_link.find('h5', {'class': "hdr"}).find('a')
        recipes.append(
            Recipe({
                'name': link_node.text,
                'ingredients': recipe_ingredients,
                'link': link_node.get('href')
            })
        )


def save_to_json(recipes):
    with open(filename, 'w') as output_file:
        json.dump(recipes, fp=output_file, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    filename = './breakfast.json'
    default_url = 'https://menunedeli.ru/zavtrak/'

    page = 20
    recipes = []
    while True:
        try:
            URL = f'{default_url}page/{page}'
            soup_obj = get_soup(URL)
            save_recipes_to_doc(soup_obj, recipes)
            page += 1
            print(page)
        except HTTPError as http_err:
            print(http_err)
            break
    save_to_json(recipes)
    print(len(recipes))