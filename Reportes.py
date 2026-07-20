import tkinter as tk
from tkinter import messagebox


class Reportes:
    def llenar_tabla(self,tabla,libros):
        for item in tabla.get_children():
            tabla.delete(item)
        for libro in libros:
            tabla.insert("",tk.END,values=(libro["id"],libro["nombre"],libro["autor"],libro["año"]))

    def buscar(self,libros,entrada,tabla):
        texto=entrada.get().lower()
        encontrados=[]
        for libro in libros:
            if texto in libro["nombre"].lower() or texto in libro["autor"].lower() or texto in str(libro["año"]):
                encontrados.append(libro)
        self.llenar_tabla(tabla,encontrados)
        if len(encontrados)==0:
            messagebox.showinfo("Búsqueda","No se encontraron libros")
    def mostrar_todos(self,libros,entrada,tabla):
        entrada.delete(0,tk.END)
        self.llenar_tabla(tabla,libros)