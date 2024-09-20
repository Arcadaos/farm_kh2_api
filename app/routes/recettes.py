from pymongo import UpdateOne
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
        return jsonify(recette)
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
        fougue=data['fougue'],
        is_niveau_sup=data['is_niveau_sup']
    )
    recette_dict = recette.to_dict()
    result = collection.update_one(
        {'name': recette_dict['name']},
        {'$set': recette_dict},
        upsert=True
        )
    return jsonify({
        'message': 'Recette modifiée',
         'recette' : recette_dict
    }), 200

@recettes_bp.route('/all', methods=['POST'], strict_slashes=False)
def update_recettes():
    mongo_db = current_app.mongo_db
    collection = mongo_db.Recettes_KH2
    
    data_list = request.json
    bulk_operations = []
    dict_list = []
    
    for recette_data in data_list :
        recette = Recette(
            name = recette_data['name'],
            components = recette_data['components'],
            rang = recette_data['rang'],
            fait = recette_data['fait'],
            fougue = recette_data['fougue'],
            is_niveau_sup = recette_data['is_niveau_sup'],
            fougue_up_when_fait = recette_data['fougue_up_when_fait']
        )
        recette_dict = recette.to_dict()
        dict_list.append(recette_dict)
    
        bulk_operations.append(
            UpdateOne(
                {'name': recette_dict['name']},
                {'$set': recette_dict},
                upsert=True
            )
        )
        result = collection.bulk_write(bulk_operations)
    return jsonify({
        'message': 'Done',
        'recettes': data_list
    }), 200
        