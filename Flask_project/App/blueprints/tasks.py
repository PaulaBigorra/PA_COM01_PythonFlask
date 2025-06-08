from flask import Blueprint, jsonify, request#Blueprint:Separa rutas en archivos, jsonify:convierte datos a formato JSON, request:permite acceder a los datos
from app.models import Tarea #Del modulo models importa la clase Tarea

tasks_bp = Blueprint('tasks', __name__) #Crea un Blueprint llamado 'tasks', que agrupa todas las rutas relacionadas con las tareas
tareas = []  # Lista de tareas (simulación de base de datos)
@tasks_bp.route('/crear', methods=['POST']) #Define una ruta "/crear" en el Blueprint que solo acepta solicitudes POST para crear tareas con datos enviados por el usuario.

def crear_tarea(): #Funcion que crea tareas y las agrega a la lista
  datos = request.json
  nueva_tarea = Tarea(len(tareas) + 1, datos["titulo"], datos["descripcion"])
  tareas.append(nueva_tarea)
  return jsonify({"mensaje": "Tarea creada exitosamente!"}), 201 #201 = codigo que indica creado exitosamente

@tasks_bp.route('/listar', methods=['GET']) #Define una ruta /listar dentro del Blueprint, indicando que acepta solicitudes GET, es decir, consultas para ver la lista de tareas.
def listar_tareas(): #Recorre la lista devolviendo el id, titulo y el estado de todas las tareas en ella
  return jsonify([{"id": t.obtener_id(), "titulo": t.obtener_titulo(), "estado": t.obtener_estado()} for t in tareas])
