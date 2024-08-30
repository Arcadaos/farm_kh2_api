from flask import Flask
from flask_pymongo import PyMongo
from pymongo import MongoClient
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}})
    
    app.config.from_object('app.config.Config')
    
    client = MongoClient(app.config['MONGO_URI'])
    app.mongo_client = client
    app.mongo_db = client[app.config['MONGO_DBNAME']]
    
    from app.routes import main
    app.register_blueprint(main)
    
    return app