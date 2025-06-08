#Importamos wraps para crear decoradores personalizados 
from functools import wraps
from flask import request, jsonify #Importamos request para verificar si los datos son formato JSON y con jsonify los convertimos al mismo

def verificar_json(f):
    @wraps(f) #preserva el nombre y documentación original
    #Nueva función que acepta cualquier cantidad de argumentos y parametros
    def envoltura(*args, **kwargs): 
        #Verifica el formato y en caso de no ser JSON devuelve el error 400
        if not request.is_json:
            return jsonify({"error": "El cuerpo debe ser JSON"}), 400 
        return f(*args, **kwargs)
    return envoltura
