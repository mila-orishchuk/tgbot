class Ingredient:
    id: int
    name: str
    unit_id: int
    
    def __init__(self, data: dict):
        self.id = data['id']
        self.name = data['name']
        self.unit = data['unit']
    
    @property
    def name(self):
        return self.name
    
    @property
    def unit(self):
        return self.unit