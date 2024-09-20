class User:
    def __init__(self, niveau: int, user: str):
        self.niveau = niveau
        self.user = user
        
        
    def to_dict(self):
        return {
            'niveau': self.niveau,
            'user': self.user
        }