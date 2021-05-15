from bs4 import BeautifulSoup
from typing import List


class Parser:
    def _get_soup(self, content: str) -> BeautifulSoup:
        return BeautifulSoup(content.decode('utf-8'), 'html.parser')

    def _get_ingredients(self, ingredients_nodes: List[BeautifulSoup]) -> List[dict]:
        ingredients = []
        for ingredient in ingredients_nodes:
            ingredients.append({
                'name': self._get_item_by_class(ingredient, 'name'),
                'description': ingredient.text
            })

        return ingredients

    def _get_recipe(self, article: BeautifulSoup) -> dict:
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
                'ingredients': self._get_ingredients(
                    article.find('ul', {'class': 'ingredients-lst'}
                                 ).findAll('span', {'itemprop': 'recipeIngredient'}))
            }
        except:
            pass
        return recipe

    def _get_item_by_class(self, ingredient: BeautifulSoup, class_name: str) -> str:
        item = ingredient.find('span', {'class': class_name})
        return item.text if item else ''

    def _get_recipes(self, soup: BeautifulSoup) -> List[dict]:
        recipes = []
        articles_nodes = soup.findAll('article')
        for article_node in articles_nodes:
            recipe = self._get_recipe(article_node)
            if recipe:
                recipes.append(recipe)

        return recipes

    def get_data(self, content: str) -> List[dict]:
        soup_obj = self._get_soup(content)
        return self._get_recipes(soup_obj)
