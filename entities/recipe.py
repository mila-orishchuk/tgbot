class Recipe:
    
    id: int
    name: str
    cooking_time: int
    
    def __init__(self, data: dict):
        if 'id' in data:
            self.id = data['id']
        self.name = data['recipes_name']
        self.ingredients = data['ingredients']
        # self.image = data['image']
        self.link = data['link']
        # self.cooking_time = data['cooking_time']
    
    def __repr__(self):
        return self.name