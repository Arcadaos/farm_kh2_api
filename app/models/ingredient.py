class Ingredient:
    def __init__(self, qualite, possede):
        self.qualite = qualite
        self.possede = possede
        
        
    def to_dict(self):
        return {
            'qualite': self.qualite,
            'possede': self.possede,
        }