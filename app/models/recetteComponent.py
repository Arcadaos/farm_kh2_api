class RecetteComponent:
    def __init__(self, qualite, type, quantite, a_farm, val_enlevee_fait):
        self.qualite = qualite
        self.type = type
        self.quantite = quantite
        self.a_farm = a_farm
        self.val_enlevee_fait = val_enlevee_fait
    
    def to_dict(self):
        return {
            'qualite' : self.qualite,
            'type' : self.type,
            'quantite' : self.quantite,
            'a_farm' : self.a_farm,
            'val_enlevee_fait' : self.val_enlevee_fait
        }