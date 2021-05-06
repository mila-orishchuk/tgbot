from model.recipe import Recipe

class DbService:
    def __init__(self, session):
        self._session = session
        
    def save_recipe(self, recipe_data: dict):
        recipe = Recipe(*recipe_data.values())
        
        self._session.add(recipe)
        self._session.commit()
        print(recipe)