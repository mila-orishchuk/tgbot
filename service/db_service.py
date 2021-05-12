from sqlalchemy import desc
from typing import List
from model.models import Recipe, Ingredient, History

class DbService:
    def __init__(self, session):
        self._session = session

    def save_recipes(self, data: List[dict]):
        if not data:
            return
        data.reverse()
        
        for recipe_data in data:
            recipe_data["ingredients"] = [Ingredient(**ingredient_data) for ingredient_data in recipe_data["ingredients"]]
            recipe = Recipe(**recipe_data)
            self._session.add(recipe)
        
        # objects = [Recipe(**recipe_data) for recipe_data in data]
        # self._session.bulk_save_objects(objects)
        self._session.commit()

    def get_latest(self):
        return self._session.query(Recipe).order_by(desc('id')).first()

    def get_all_recipes(self):
        return self._session.query(Recipe).all()

    def save_recipe_ingredients(self, ingredients):
        pass        