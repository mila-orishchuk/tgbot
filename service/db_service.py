from model.recipe import Recipe
from sqlalchemy import desc
from typing import List


class DbService:
    def __init__(self, session):
        self._session = session

    def save_recipes(self, recipes_data: List[dict]):
        if not recipes_data:
            return
        recipes_data.reverse()
        objects = [Recipe(**recipe_data) for recipe_data in recipes_data]
        self._session.bulk_save_objects(objects)
        self._session.commit()

    def get_latest(self):
        return self._session.query(Recipe).order_by(desc('id')).first()

    def get_all_recipes(self):
        return self._session.query(Recipe).all()
