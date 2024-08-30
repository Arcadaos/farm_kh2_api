from typing import List
from app.models.recetteComponent import RecetteComponent


class Recette:
    def __init__(self, name, components: List[RecetteComponent], rang, fait, fougue):
        self.name = name
        self.components = components
        self.rang = rang
        self.fait = fait
        self.fougue = fougue
        
    def to_dict(self):
        return {
            'name': self.name,
            'components': self.components,
            'rang' : self.rang,
            'fait' : self.fait,
            'fougue' : self.fougue
        }