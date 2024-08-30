from typing import List
from app.models.ingredient import Ingredient


class IngredientPack:
    def __init__(self, type, elements: List[Ingredient]):
        self.type = type
        self.elements = elements
        
        
    def to_dict(self):
        return {
            'type': self.type,
            'elements': self.elements,
        }