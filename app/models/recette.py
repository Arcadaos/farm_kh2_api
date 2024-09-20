from typing import List
from app.models.recetteComponent import RecetteComponent


class Recette:
    def __init__(self, name, components: List[RecetteComponent], rang, fait, fougue, is_niveau_sup, fougue_up_when_fait):
        self.name = name
        self.components = components
        self.rang = rang
        self.fait = fait
        self.fougue = fougue
        self.is_niveau_sup = is_niveau_sup
        self.fougue_up_when_fait = fougue_up_when_fait
        
    def to_dict(self):
        return {
            'name': self.name,
            'components': self.components,
            'rang' : self.rang,
            'fait' : self.fait,
            'fougue' : self.fougue,
            'is_niveau_sup': self.is_niveau_sup,
            'fougue_up_when_fait' : self.fougue_up_when_fait
        }