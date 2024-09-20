from pymongo import UpdateOne
from app.models.ingredient import Ingredient
from app.models.ingredientPack import IngredientPack
from flask import Blueprint, jsonify, current_app, request

from app.models.user import User

user_bp = Blueprint('user', __name__, url_prefix='/api/user')

@user_bp.route('/', methods=['GET'], strict_slashes=False)
def get_users():
    mongo_db = current_app.mongo_db
    collection = mongo_db.User_KH2
    try :
        users = collection.find_one({}, {'_id': 0})
        return jsonify(users)
    except Exception as e:
        return jsonify({'error' : str(e)}), 500

@user_bp.route('/<string:user>', methods=['GET'], strict_slashes=False)
def get_user(user):
    mongo_db = current_app.mongo_db
    collection = mongo_db.User_KH2
    try :
        user = collection.find_one({'user' : user}, {'_id' : 0})
        return jsonify(user)
    except Exception as e:
        return jsonify({'error' : str(e)}), 500

@user_bp.route('/', methods=['POST'], strict_slashes=False)
def update_user():
    mongo_db = current_app.mongo_db
    collection = mongo_db.User_KH2
    
    data = request.json
    user = User(
        niveau = data['niveau'],
        user = data['user']
        )
    niveau_dict = user.to_dict()
    result = collection.update_one(
        {'user': niveau_dict['user']},
        { '$set': niveau_dict},
        upsert=True
    )
    return jsonify({
        'message' : 'Niveau mog modifié',
        'niveau' : niveau_dict
    }), 200