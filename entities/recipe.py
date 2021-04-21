class Recipe:
    
    id: int
    name: str
    cooking_time: int
    
    def __init__(self, data: dict):
        self.id = data['id']
        self.name = data['recipes_name']
        self.ingredients = data['ingredients']
        self.image = data['image']
        self.link = data['link']
        self.cooking_time = data['cooking_time']
        
    @property
    def name(self):
        return self.name
    
    @property
    def image(self):
        return self.image
    
    @property
    def link(self):
        return self.link
    
    @property
    def ingredients(self):
        return self.ingredients