class RecetteComponent:
    def __init__(self, qualite, type, quantite):
        self.qualite = qualite
        self.type = type
        self.quantite = quantite
    
    def to_dict(self):
        return {
            'qualite' : self.qualite,
            'type' : self.type,
            'quantite' : self.quantite
        }