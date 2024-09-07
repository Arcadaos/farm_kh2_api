from app.models.recette import Recette
from flask import Blueprint, jsonify, current_app, request

recettes_bp = Blueprint('recettes', __name__, url_prefix='/api/recettes')

@recettes_bp.route('/', methods=['GET'], strict_slashes=False)
def get_recettes():
    mongo_db = current_app.mongo_db
    collection = mongo_db.Recettes_KH2
    try :
        recettes = collection.find({}, {'_id' : 0})
        return jsonify(list(recettes))
    except Exception as e:
        return jsonify({'error' : str(e)}), 500

@recettes_bp.route('/<string:name>', methods=['GET'], strict_slashes=False)
def get_recette(name):
    mongo_db = current_app.mongo_db
    collection = mongo_db.Recettes_KH2
    try :
        recette = collection.find_one({'name' : name}, {'_id' : 0})
        return recette
    except Exception as e:
        return jsonify({'error' : str(e)}), 500

@recettes_bp.route('/', methods=['POST'], strict_slashes=False)
def update_recette():
    mongo_db = current_app.mongo_db
    collection = mongo_db.Recettes_KH2
    
    data = request.json
    recette = Recette(
        name=data['name'],
        components=data['components'],
        rang=data['rang'],
        fait=data['fait'],
        fougue=data['fougue']
    )
    recette_dict = recette.to_dict()
    result = collection.update_one(
        {'name': recette_dict['name']},
        {'$set': recette_dict},
        upsert=True
        )
    print(result)
    return jsonify({
        'message': 'Recette modifiée',
         'recette' : recette_dict
    }), 200
        