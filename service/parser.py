from entities.recipe import Recipe
from bs4 import BeautifulSoup


def get_soup(content):
    return BeautifulSoup(content.decode('utf-8'), 'html.parser')


def get_ingredients(ingredients_nodes):
    ingredients = []
    for ingredient in ingredients_nodes:
        ingredients.append({
            'name': get_item_by_class(ingredient, 'name'),
            'quantity': get_item_by_class(ingredient, 'value'),
            'unit': get_item_by_class(ingredient, 'type') or get_item_by_class(ingredient, 'amount')
        })
    return ingredients


def get_recipe(article):
    recipe = None
    try:
        hdr = article.find('div', {'class': "info col"}).find(
            'h5', {'class': 'hdr'}).find('a')
        recipe = Recipe({
            "recipes_name": hdr.text,
            "link": hdr.get('href'),
            "image": article.find('div', {'class': "img col-auto"}).find('img').get('src'),
            "cooking_time": article.find('ul', {'class': "params-detail-lst row"})
            .find('span', {'class': 'duration'}).text,
            "ingredients": get_ingredients(
                article.find('ul', {'class': "ingredients-lst"}
                             ).findAll('span', {'itemprop': "recipeIngredient"})
            )
        })
    except:
        pass
    return recipe


def get_item_by_class(ingredient, class_name):
    item = ingredient.find('span', {'class': class_name})
    return item.text if item else ''


def get_recipes(soup):
    recipes = []
    articles_nodes = soup.findAll('article')
    for article_node in articles_nodes:
        recipe = get_recipe(article_node)
        if recipe:
            recipes.append(recipe)

    return recipes


def parse(content):
    soup_obj = get_soup(content)
    return get_recipes(soup_obj)
