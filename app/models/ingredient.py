class Ingredient:
    def __init__(self, qualite: str, possede: int, quantite: int, type: str = None):
        self.qualite = qualite
        self.possede = possede
        self.quantite = quantite
        self.type = type
        
        
    def to_dict(self):
        return {
            'qualite': self.qualite,
            'possede': self.possede,
            'quantite': self.quantite,
            'type': self.type
        }