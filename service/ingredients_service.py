from ...entities.Ingredients import Ingredients

class IngredientService:
    
    TABLE = "ingredients"
    
    def __init__(self, *args, **kwargs):
        self.db = kwargs['db']
        if type(self.db) != 'Connection':
            raise Exception("invalid db variable passed to constructor")
        
    def getAll(self) -> Ingredients[]:
        ingredients = []
        result = self.db.execute(f"SELECT * FROM {self.TABLE}")
        if result:
            for row in result:
                ingredients.append(Ingredients(row))
        
        return ingredients
    
    def add(self, ingredients: Ingredients):
        self.db.execute(f"INSERT INTO {self.TABLE}")