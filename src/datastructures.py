
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    # metodo constructor(__init__) que se ejecuta instantaneamente despues de crear una nueva instancia
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1  # Inicializa el primer ID a 1
        # example list of members
        # no hay mienbros aun
        self._members = []

    # Este método genera un 'id' único al agregar miembros a la lista (no debes modificar esta función)
    def _generate_id(self):
        # se crea una nueva propiedad "_next_id" y se guarda en una varible
        # obtiene el id actual
        generated_id = self._next_id #self._next_id el valor del id a usar
        # su valor incrementa en 1 y se reasigna
        self._next_id += 1 # asi el proximo id generado sera sucesivo y unico
        # retorna el id generado
        return generated_id
        # return randint(0, 99999999)
    # se espera que member sea un dictionario por eso se accede a su clave "id", que va entre comillas

    def add_member(self, member):
        ## Agrega un nuevo miembro a la lista de _members
        ## pass indica que el metodo no tiene logica, esta vacio 
        # condicion para verificar si el miembro ya tiene un id
        if "id" not in member:
            # si el "id" no esta en el member entonces se llama al metodo
            member["id"] = self._generate_id() #genera un nuevo id

        self._members.append(member)

    def delete_member(self, id):
        ## Recorre la lista y elimina el miembro con el id proporcionado
        self._members = [member for member in self._members if member["id"] != id]

    def get_member(self, id):
        ## Recorre la lista y obtén el miembro con el id proporcionado
        ## Busca un mienbro en la lista y devuele el mienbro que coincide con su id que se busca
        ## obtiene un mienbro de una lista basada en un identificador
        for member in self._members:
            ## si el valor de la clave "id", es igual al id que se ingresa
            if member["id"] == id:
                ## retorna o devuelve member que buscamos
                return member
        ## si se recorre el bucle y no encuentra nada retorna un none
        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        # esta funcion retorna todos los miembros
        return self._members
        