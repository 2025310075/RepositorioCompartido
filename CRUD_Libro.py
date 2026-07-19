import tkinter as tk
from tkinter import ttk, messagebox


class CRUD_Libro:
 def __init__ (self):
#LISTA
  self.libros = []
  self.ID_Lib = 1
  self.ID_selec = None 


 def limpiar(self,LiNombre, LiAutor,LiAño):
    LiNombre.delete(0, tk.END)
    LiAutor.delete(0, tk.END)
    LiAño.delete(0, tk.END)
    
 def agregar_Libro(self,LiNombre, LiAutor,LiAño,tabla):
    nombre = LiNombre.get()
    autor = LiAutor.get()
    año = LiAño.get()


    if nombre == "" or autor == "" or año=="":
        messagebox.showwarning("Error", "No se pueden dejar campos vacíos")
        return


    # CREATE
    agregar_libro = {
        "id": self.ID_Lib,
        "nombre": nombre,
        "autor": autor,
        "año": año,
    }
    self.libros.append(agregar_libro)
    self.ID_Lib += 1
   
    self.actualizar_tabla(tabla)
    self.limpiar(LiNombre, LiAutor,LiAño)
    messagebox.showinfo("Correcto", "El libro se registrócorrectamente.")


def seleccionar_Libro(self,event,tabla,LiNombre,LiAutor,LiAño):
    # READ
    try:
        seleccion = tabla.selection()[0]
        valores = tabla.item(seleccion, 'values')


        self.limpiar(LiNombre, LiAutor,LiAño)
        #Guardar el id


        self.ID_sele = int(valores[0])


        LiNombre.insert(0, valores[1])
        LiAutor.insert(0, valores[2])
        LiAño.insert(0, valores[3])
    except IndexError:
        pass



    
