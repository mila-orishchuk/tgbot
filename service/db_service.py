from sqlalchemy import desc
from  sqlalchemy.sql.expression import func
from typing import List
from model.models import Recipe, Ingredient, History, Category
# import logging

# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

class DbService:
    def __init__(self, session):
        self._session = session

    def save_recipes(self, data: List):
        if not data:
            return
        data.reverse()

        for recipe_data in data:
            if type(recipe_data) is Recipe:
                recipe = recipe_data
            else:
                recipe_data["ingredients"] = [Ingredient(
                    **ingredient_data) for ingredient_data in recipe_data["ingredients"]]
                recipe = Recipe(**recipe_data)
            self._session.add(recipe)

        self._session.commit()

    def get_all_urls(self):
        return [*map(
            lambda row: row[0],
            self._session.query(Recipe.url).all()
        )]

    def get_all_recipes(self):
        return self._session.query(Recipe).all()

    def get_random_recipe(self, category):
        return self._session.query(Recipe).order_by(func.rand()).first()
    
    def get_all_categoties(self):
        return self._session.query(Category).all()
    
    def get_by_url(sqlf, url):
        return self._session.query(Recipe).where(Recipe.url == url).first()