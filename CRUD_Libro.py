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
    
