#Importa del modulo app la funcion create_app
from app import create_app

app = create_app() #Guarda la instancia como variable

#Verifica si se ejecuta directamente
if __name__ == '__main__': 
    app.run(debug=True)
    #Inicia el servidor permitiendo acceder en el navegador
