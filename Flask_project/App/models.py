#Creamos una clase con atributos privados

class Tarea:
    def __init__(self, id, titulo, descripcion, completado=False):
        self.__id = id  # Encapsulación: atributo privado
        self.__titulo = titulo
        self.__descripcion = descripcion
        self.__completado = completado
      
    # Métodos para acceder y modificar atributos encapsulados
    def obtener_id(self):
      return self.__id

    def obtener_titulo(self):
      return self.__titulo

    def marcar_completado(self):
      self.__completado = True

    #Dependiendo el estado de la tarea devuelve Completado o Pendiente
    def obtener_estado(self):
      return "Completado" if self.__completado else "Pendiente"
