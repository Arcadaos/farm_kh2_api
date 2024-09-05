import string


class Ingredient:
    def __init__(self, qualite: string, possede: int, quantite: int):
        self.qualite = qualite
        self.possede = possede
        self.quantite = quantite
        
        
    def to_dict(self):
        return {
            'qualite': self.qualite,
            'possede': self.possede,
            'quantite': self.quantite
        }