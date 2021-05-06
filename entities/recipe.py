from entities.base_entity import BaseEntity
from entities.ingredient import Ingredient
from typing import List


class Recipe(BaseEntity):
    name: str
    ingredients: List[Ingredient]
    image: str
    url: str
    cooking_time: int

    def __init__(self, data: dict):
        super().__init__(data)
        self.name = data['recipes_name']
        self.ingredients = data['ingredients']
        self.image = data['image']
        self.url = data['url']
        self.cooking_time = data['cooking_time']

    def __repr__(self):
        return self.name
