from pymongo import UpdateOne
from app.models.ingredient import Ingredient
from app.models.ingredientPack import IngredientPack
from flask import Blueprint, jsonify, current_app, request

farm_bp = Blueprint('farm', __name__, url_prefix='/api/farm')

@farm_bp.route('/<string:qualite>/<string:type>', methods=['GET'], strict_slashes=False)
def get_quantite_to_farm(qualite, type):
    mongo_db = current_app.mongo_db
    collection = mongo_db.Farm_joueur_KH2
    try :
        pipeline = [
        {'$match': {'type': type}},
        {'$unwind': {'path': '$elements'}},
        {'$match': {'elements.qualite': qualite}},
        {'$project': {'quantite': '$elements.quantite', 'possede': '$elements.possede', '_id': 0}}
        ]
        result = list(collection.aggregate(pipeline))
        return result[0]
    except Exception as e:
        return jsonify({'error' : str(e)}), 500

@farm_bp.route('/', methods=['GET'], strict_slashes=False)
def get_farm():
    mongo_db = current_app.mongo_db
    collection = mongo_db.Farm_joueur_KH2
    try :
        farm = collection.find({}, {'_id' : 0})
        return jsonify(list(farm))
    except Exception as e:
        return jsonify({'error' : str(e)}), 500
        
@farm_bp.route('/', methods=['POST'], strict_slashes=False)
def update_farms():
    mongo_db = current_app.mongo_db
    collection = mongo_db.Farm_joueur_KH2
    
    data_list = request.json
    bulk_operations = []
    dict_list = []
    
    for ingredient_data in data_list :
        ingredient = IngredientPack(
            type = ingredient_data['type'],
            elements = ingredient_data['elements']
        )
        ingredient_dict = ingredient.to_dict()
        dict_list.append(ingredient)
        
        bulk_operations.append(
            UpdateOne(
                {'type': ingredient_dict['type']},
                {'$set': ingredient_dict},
                upsert=True
            )
        )
    result = collection.bulk_write(bulk_operations)
    return jsonify({
        'message': 'Avancée du farm mis à jour',
        'modified_count': result.modified_count,
        'upserted_count': result.upserted_count,
        'matched_count': result.matched_count,
        'ingredients' : data_list
    }), 200
        