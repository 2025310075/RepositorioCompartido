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
    
 def actualizar_Libro(self,LiNombre, LiAutor,LiAño,tabla):
    try:
        nombre = LiNombre.get()
        autor = LiAutor.get()
        año = LiAño.get()


        # UPDATE
        for b in self.libros:
            if b["id"] == self.ID_sele:
                b["nombre"] = nombre
                b["autor"] = autor
                b["año"] = año
                break
               
        self.actualizar_tabla(tabla)
        self.limpiar(LiNombre,LiAutor,LiAño)
        messagebox.showinfo("Éxito", "Los datos del libro se actualizaron correctamente.")
    except NameError:
        messagebox.showwarning("Atención", "Se tiene que seleccionar un libro primero")


 def eliminar_Libro(self,LiNombre, LiAutor,LiAño,tabla):
    try:
        # DELETE
        for i, p in enumerate(self.libros):
            if p["id"] == self.ID_sele:
                del self.libros[i]
                break
               
        self.actualizar_tabla(tabla)
        self.limpiar(LiNombre,LiAutor,LiAño)
        messagebox.showinfo("Éxito", "Se eliminó correctamente")
    except NameError:
        messagebox.showwarning("Atención", "Por favor selecciona un libro primero.")
        
 def actualizar_tabla(self,tabla):
    # Limpiar tabla visual
    for item in tabla.get_children():
        tabla.delete(item)


    # llenar tabla con pacientes
    for b in self.libros:
        tabla.insert("", tk.END, values=(b["id"], b["nombre"], b["autor"], b["año"]))







    
