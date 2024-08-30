from pymongo import MongoClient
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

#client = MongoClient("mongodb://kingdom:hearts@localhost:27017/?authSource=Kingdom_Hearts")

#db = client["Kingdom_Hearts"]

#recettes = db["Recettes_KH2"]
    
