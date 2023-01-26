"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User,Personajes,Vehiculos,Planetas,Favoritos
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

#ACA EL QUE TRAIA EL CODIGO
# @app.route('/user', methods=['GET'])
# def handle_hello():

#     response_body = {
#         "msg": "Hello, this is your GET /user response "
#     }

#     return jsonify(response_body), 200

# ---------------->>>>> ESTE ES EL GET DE TODOS LOS USER <<<<<----------------
@app.route('/user', methods=['GET'])
def handle_user():
    alluser = User.query.all()
    results = list(map(lambda item: item.serialize(),alluser))

    return jsonify(results), 200
    
# ---------------->>>>> ESTE ES EL GET DE TODOS LOS PERSONAJES <<<<<----------------
@app.route('/personajes', methods=['GET'])
def handle_personajes():
    allpersonajes = Personajes.query.all()
    results = list(map(lambda item: item.serialize(),allpersonajes))
    print(results)

    return jsonify(results), 200
    # return jsonify({"msg":"funciona"}), 200

# # ---------------->>>>> ESTE ES EL GET DE UN  PERSONAJE <<<<<----------------
@app.route('/personajes/<int:personajes_id>', methods=['GET'])
def get_info_personajes(personajes_id):
    
    personajes = Personajes.query.filter_by(id=personajes_id).first()
    return jsonify(personajes.serialize()), 200

    # # ---------------->>>>> NO LO PIDE PERO ASI SE HACE EL GET DE VEHICULOS<<<<<----------------
# # ---------------->>>>> ESTE ES EL GET DE TODOS LOS VEHICULOS<<<<<----------------
# @app.route('/vehiculos', methods=['GET'])
# def handle_vehiculos():
#     allvehiculos = vehiculos.query.all()
#     results = list(map(lambda item: item.serialize(),allvehiculos))

#     return jsonify(results), 200

# # # ---------------->>>>> ESTE ES EL GET DE UN VEHICULO <<<<<----------------
# @app.route('/vehiculos/<int:vehiculos_id>', methods=['GET'])
# def get_info_vehiculos(vehiculos_id):
    
#     vehiculos = vehiculos.query.filter_by(id=vehiculos_id).first()
#     return jsonify(Vehiculos.serialize()), 200    

# ---------------->>>>> ESTE ES EL GET DE TODOS LOS PLANETAS <<<<<----------------
@app.route('/planetas', methods=['GET'])
def handle_planetas():
    allplanetas = Planetas.query.all()
    results = list(map(lambda item: item.serialize(),allplanetas))

    return jsonify(results), 200

# # ---------------->>>>> ESTE ES EL GET DE UN  PLANETA <<<<<----------------
@app.route('/planetas/<int:planetas_id>', methods=['GET'])
def get_info_planetas(planetas_id):
    
    planetas = Planetas.query.filter_by(id=planetas_id).first()
    return jsonify(planetas.serialize()), 200


# # ---------------->>>>> ESTE ES EL GET Favoritos <<<<<----------------
@app.route('/user/<int:user_id>/favoritos/', methods=['GET'])
def get_favoritos_user(user_id):
    
    user_favoritos = Favoritos.query.filter_by(user_id=user_id).all()
    results = list(map(lambda item: item.serialize(),user_favoritos))
    print(results)
    return jsonify(results), 200

# # ---------------->>>>> ESTE ES EL POST DE UN  PLANETA <<<<<----------------
@app.route('/todos', methods=['POST'])
def agregar_nuevo_planeta_favorito(user_id):
    # consulta_planeta_favoritos=Favoritos.quety.filer_by()
    # planetas_favoritos_user = User('admin', 'admin@example.com')    
    # db.session.add(me)
    # db.session.commit()
    # request_body = request.json
    # print("Incoming request with the following body", request_body)
    # todos.append(request_body)
    return jsonify({"msg":"funciona"})

# this only runs if `$ python src/app.py` is executed

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
