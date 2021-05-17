from sqlalchemy import desc
from sqlalchemy.sql.expression import func
from typing import List
from model.models import Recipe, Ingredient, History, Category, recipes_categories_table


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

    def save_recipes_categories(self, rows: List[dict]):
        for row in rows:
            stmt = recipes_categories_table.insert().values(**row)
            self._session.execute(stmt)
        self._session.commit()

    def get_all_urls(self):
        return [*map(
            lambda row: row[0],
            self._session.query(Recipe.url).all()
        )]

    def get_all_recipes(self):
        return self._session.query(Recipe).all()

    def get_random_recipe(self, category_id):
        return self._session.query(Recipe).order_by(func.random()).first()

    def get_all_categoties(self):
        return self._session.query(Category).all()

    def get_by_url(self, url):
        return self._session.query(Recipe).where(Recipe.url == url).first()

    def get_recipe_by_id(self, id):
        return self._session.query(Recipe).where(Recipe.id == id).first()
    
    def save_choise(self, choise, recipe_id, user_id):
        history = History(recipe_id=recipe_id, user_id=user_id, choise=choise)
        self._session.add(history)
        self._session.commit()