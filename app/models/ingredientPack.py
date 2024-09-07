from typing import List
from app.models.ingredient import Ingredient


class IngredientPack:
    def __init__(self, type: str, elements: List[Ingredient]):
        self.type = type
        self.elements = elements
        
        
    def to_dict(self):
        return {
            'type': self.type,
            'elements': self.ingredient_to_dict(self.elements)
        }
    
    def ingredient_to_dict(self, ingredients: dict):
        return [
                {
                    'qualite': element['qualite'],
                    'possede': element['possede'],
                    'quantite': element['quantite'],
                    **({'quantiteAFougue': element['quantiteAFougue']} if 'quantiteAFougue' in element else {})
                }
            for element in ingredients]