from flask import Flask  
from app.blueprints.tasks import tasks_bp #Importa el blueprint tasks_bp
from app.config import Config #Importa la clase Config que contiene variables globales (Secret_key y Debug)

def create_app():#Creamos la clase que construye la app
    app = Flask(__name__)
    app.config.from_object(Config) #Carga la configuración de la clase Config con las variables
    app.register_blueprint(tasks_bp, url_prefix='/tasks') #Registra el Blueprint y hace que todas las rutas empiecen en “/tasks”
    return app
