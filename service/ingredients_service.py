from ...entities.recipe import Recipe

class RecipeService:
    
    TABLE = "recipes"
    
    def __init__(self, *args, **kwargs):
        self.db = kwargs['db']
        if type(self.db) != 'Connection':
            raise Exception("invalid db variable passed to constructor")
        
    def getAll(self) => Recipe[]:
        recipies = []
        result = self.db.execute(f"SELECT * FROM {self.TABLE}")
        if result:
            for row in result:
                recipies.append(Recipe(row))
        
        return recipies
    
    def add(self, recipe: Recipe):
        self.db.execute(f"INSERT INTO {self.TABLE}")