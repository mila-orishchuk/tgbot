from entities.base_entity import BaseEntity


class Ingredient(BaseEntity):
    name: str
    description: str

    def __init__(self, data: dict):
        super().__init__(data)
        self.name = data['name']
        self.description = data['description']
