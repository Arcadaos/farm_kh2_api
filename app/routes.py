from pymongo import UpdateOne
from app.models.recetteComponent import RecetteComponent
from app.models.ingredientPack import IngredientPack
from app.models.recette import Recette
from flask import Blueprint, jsonify, current_app, request

main = Blueprint('main', __name__, url_prefix='/api')

@main.route('/recettes', methods=['GET'], strict_slashes=False)
def get_recettes():
    mongo_db = current_app.mongo_db
    collection = mongo_db.Recettes_KH2
    try :
        recettes = collection.find({}, {'_id' : 0})
        return jsonify(list(recettes))
    except Exception as e:
        return jsonify({'error' : str(e)}), 500

@main.route('/recettes/<string:name>', methods=['GET'], strict_slashes=False)
def get_recette(name):
    mongo_db = current_app.mongo_db
    collection = mongo_db.Recettes_KH2
    try :
        recette = collection.find_one({'name' : name}, {'_id' : 0})
        return recette
    except Exception as e:
        return jsonify({'error' : str(e)}), 500

@main.route('/recettes', methods=['POST'], strict_slashes=False)
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

@main.route('/farm/<string:qualite>/<string:type>', methods=['GET'], strict_slashes=False)
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

@main.route('/serenite', methods=['GET'], strict_slashes=False)
def serenite():
    etat_farm_cristal_serenite = get_quantite_to_farm('Cristal', 'Sérénité')
    print(etat_farm_cristal_serenite["quantite"])
    quantite_restante_a_farm = max(etat_farm_cristal_serenite["quantite"] - etat_farm_cristal_serenite["possede"], 0)
    recette_cristal_serenite = get_recette('Cristal de sérénité')
    new_quantity_to_get = [
        RecetteComponent(
            qualite=component["qualite"],
            type=component["type"],
            quantite= quantite_restante_a_farm * component["quantite"]
        ).to_dict()
        for component in recette_cristal_serenite["components"]
    ]
    return jsonify(new_quantity_to_get)

@main.route('/mithril', methods=['GET'], strict_slashes=False)
def mithril():
    etat_farm_cristal_serenite = get_quantite_to_farm('Cristal', 'Mithril')
    print(etat_farm_cristal_serenite["quantite"])
    quantite_restante_a_farm = max(etat_farm_cristal_serenite["quantite"] - etat_farm_cristal_serenite["possede"], 0)
    recette_cristal_serenite = get_recette('Cristal de mithril')
    new_quantity_to_get = [
        RecetteComponent(
            qualite=component["qualite"],
            type=component["type"],
            quantite= quantite_restante_a_farm * component["quantite"]
        ).to_dict()
        for component in recette_cristal_serenite["components"]
    ]
    return jsonify(new_quantity_to_get)

@main.route('/manifeste', methods=['GET'], strict_slashes=False)
def manifeste():
    etat_farm_cristal_serenite = get_quantite_to_farm('Illusion manifeste', 'Divers')
    print(etat_farm_cristal_serenite["quantite"])
    quantite_restante_a_farm = max(etat_farm_cristal_serenite["quantite"] - etat_farm_cristal_serenite["possede"], 0)
    recette_cristal_serenite = get_recette('Illusion manifeste')
    new_quantity_to_get = [
        RecetteComponent(
            qualite=component["qualite"],
            type=component["type"],
            quantite= quantite_restante_a_farm * component["quantite"]
        ).to_dict()
        for component in recette_cristal_serenite["components"]
    ]
    return jsonify(new_quantity_to_get)
    
@main.route('/farm', methods=['GET'], strict_slashes=False)
def get_farm():
    mongo_db = current_app.mongo_db
    collection = mongo_db.Farm_joueur_KH2
    try :
        farm = collection.find({}, {'_id' : 0})
        return jsonify(list(farm))
    except Exception as e:
        return jsonify({'error' : str(e)}), 500
        
@main.route('/farm', methods=['POST'], strict_slashes=False)
def update_farms():
    mongo_db = current_app.mongo_db
    collection = mongo_db.Farm_joueur_KH2
    
    data_list = request.json
    bulk_operations = []
    
    for ingredient_data in data_list :
        ingredient = IngredientPack(
            type = ingredient_data['type'],
            elements=ingredient_data['elements']
        )
        ingredient_dict = ingredient.to_dict()
        
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
        