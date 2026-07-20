class Autor:

    def __init__(self, nombre):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.edad = edad
        
    def mostrar_autor(self):
     return f"Nombre: {self.nombre}, Nacionalidad: {self.nacionalidad}, Edad: {self.edad}"
   
    def actualizar_autor(self, nuevo_nombre, nueva_nacionalidad, nueva_edad):
     self.nombre = nuevo_nombre
     self.nacionalidad = nueva_nacionalidad
     self.edad = nueva_edad
     return "Autor actualizado correctamente"

    def eliminar_autor(self):
     self.nombre = ""
     self.nacionalidad = ""
     self.edad = 0
     return "Autor eliminado"
        