from entities.recipe import Recipe
from bs4 import BeautifulSoup

def get_soup(content):
    return BeautifulSoup(content.decode('utf-8'), 'html.parser')


def get_recipe_links(soup):
    links = soup.findAll('div', {'class': "info col"})
    ingredients_nodes = soup.findAll('ul', {'class': "ingredients-lst"})
    return zip(ingredients_nodes, links)


def get_item_by_class(ingredient, class_name):
    item = ingredient.find('span', {'class': class_name})
    return item.text if item else ''


def get_recipes(soup):
    recipes = []
    
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
                'recipes_name': link_node.text,
                'ingredients': recipe_ingredients,
                'link': link_node.get('href')
            })
        )
    return recipes

def parse(content):
    soup_obj = get_soup(content)
    return get_recipes(soup_obj)

# if __name__ == '__main__':
#     filename = './breakfast.json'
#     default_url = 'https://menunedeli.ru/zavtrak/'

#     page = 20
#     recipes = []
#     while True:
#         try:
#             URL = f'{default_url}page/{page}'
            
#             page += 1
#             print(page)
#         except HTTPError as http_err:
#             print(http_err)
#             break
#     save_to_json(recipes)
#     print(len(recipes))