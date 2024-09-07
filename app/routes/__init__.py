from flask import Flask
from app.routes.recettes import recettes_bp
from app.routes.farm import farm_bp

def register_blueprints(app: Flask):
    app.register_blueprint(recettes_bp)
    app.register_blueprint(farm_bp)