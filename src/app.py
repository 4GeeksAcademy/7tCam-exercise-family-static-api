"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# se esta instanciando de la clase FamilyStructure, el valor de "Jackson",  es el apellido 
jackson_family = FamilyStructure("Jackson")
# agregando mienbros a la familia
# 1er mienbro
jackson_family.add_member(
    {
        "first_name" : "John",
        "age": 33,
        "lucky_numbers" : [7, 13, 22]
    })
# 2do mienbro
jackson_family.add_member(
    {
        "first_name" : "Jane",
        "age": 35,
        # numeros de la suerte
        "lucky_numbers" : [10, 14, 3]
    })
# 3er mienbro
jackson_family.add_member(
    {
        "first_name" : "Jimmy ",
        "age": 5,
        "lucky_numbers" : [1]
    })

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)
# Endpoint para obtener todos los miembros de la familia
@app.route('/members', methods=['GET'])
def get_all_members():
    # jackson_family instancia de FamilyStructure que representa a la familia
    members = jackson_family.get_all_members()# get_all_members metodo de la clase FamilyStructure que devuelve todos lo mienbros
    #se llama a el metodo y se almacena la lista de miembros en una variable members  
    #creando un objeto con informacion que queramos
    # response_body = {
        # la propiedad family guarda o trae la api members, se accede
        # "family": members
    # }
    return jsonify(members), 200

# obteniendo la informacion de un solo miembro
@app.route('/member/<int:member_id>', methods=['GET'])
def get_a_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    else:
        return jsonify({"message" : "member not found"}), 404
#endpoint para agregar un nuevo integrante
@app.route('/member', methods=['POST'])
def add_menber():
    #accedemos al body y lo pasamos al formato python con .get_json(){metodo de Flask}
    data = request.get_json()
    if not data:
        #error 400 por falta de datos
        return jsonify({"message" : "invalid input"}), 400
    # Validar los /campos requeridos/ o necesarios, asegurando que llegue si or si la info complete
    required_fields = ["first_name", "age", "lucky_numbers"]
    #por cada campo in the list
    for field in required_fields:
        if field not in data:
            return jsonify({"message": f"'{field}' is required"}), 400      
    # Agregar el miembro a la familia
    jackson_family.add_member(data)#data es lo que se recibe por eso se agrega
    #201 porque se creo un nuevo recuros con exito
    return jsonify({"message": "Member added successfully", "member": data}), 201
#endpoint eliminar un mienbro
@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    # se busca en la lista que un mienbro tenga id member_id o verifica que exista ese miemnbro con el id 
    member = jackson_family.get_member(member_id)
    if member:
        #si es encontrado el member_id entoces se elimina al miembro de la lista
        jackson_family.delete_member(member_id)
        #obtener la nueva lista sin el elmennto eliminado, /miembnros restantes/
        remaining_members  = jackson_family.get_all_members()
        return jsonify({"done": True, "remaining_members" : remaining_members}), 200
    else:
        #si no es encontrado
        return jsonify({"message": "Member not found"}), 404
# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
