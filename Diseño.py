
import tkinter as tk
from tkinter import ttk
import CRUD_Libro
import Reportes

class Biblioteca: 
    
 def __init__ (self):
  self.crud = CRUD_Libro.CRUD_Libro()
  self.reportes=Reportes.Reportes()
  self.ventana = tk.Tk()
  self.ventana.title("Biblioteca Registro de Libros")
  self.ventana.geometry("500x600")

# Formulario
  self.frame_for = tk.LabelFrame(self.ventana, text="Datos del libro")
  self.frame_for.pack(fill="both")

  self.EtiqNom= tk.Label(self.ventana, text="Nombre:")
  self.EtiqNom.pack(pady=5)
  self.EnNombre = tk.Entry(self.ventana)
  self.EnNombre.pack(pady=5)

  self.EtiqAutor = tk.Label(self.ventana, text="Autor:")
  self.EtiqAutor.pack( pady=5)
  self.EnAutor = tk.Entry(self.ventana)
  self.EnAutor.pack(pady=5)

  self.EtiqAño = tk.Label(self.ventana, text="Año:")
  self.EtiqAño.pack(pady=5)
  self.EnAño = tk.Entry(self.ventana)
  self.EnAño.pack(pady=5)
  
#Botones
  self.Agregar= tk.Button(self.ventana, text="Agregar", command= lambda: self.crud.agregar_Libro(self.EnNombre,self.EnAutor,self.EnAño,self.tabla))
  self.Agregar.pack(pady=5)
  self.Actualizar = tk.Button(self.ventana, text="Actualizar", command=lambda: self.crud.actualizar_Libro(self.EnNombre,self.EnAutor,self.EnAño,self.tabla))
  self.Actualizar.pack(pady=5)
  self.Eliminar = tk.Button(self.ventana, text="Eliminar", command=lambda: self.crud.eliminar_Libro(self.EnNombre,self.EnAutor,self.EnAño,self.tabla))
  self.Eliminar.pack(pady=5)
  self.Limpiar = tk.Button(self.ventana, text="Limpiar", command=lambda: self.crud.limpiar(self.EnNombre,self.EnAutor,self.EnAño))
  self.Limpiar.pack(pady=5)
  self.Salir = tk.Button(self.ventana, text="Salir", command=lambda: self.ventana.destroy())
  self.Salir.pack(pady=5)

# Búsqueda y reporte
  self.frame_buscar=tk.Frame(self.ventana)
  self.frame_buscar.pack(pady=10)

  self.EnBuscar=tk.Entry(self.frame_buscar,width=20)
  self.EnBuscar.pack(side="left",padx=5)

  self.Buscar=tk.Button(self.frame_buscar,text="Buscar",command=lambda:self.reportes.buscar(self.crud.libros,self.EnBuscar,self.tabla))
  self.Buscar.pack(side="left",padx=5)

  self.Mostrar=tk.Button(self.frame_buscar,text="Mostrar todos",command=lambda:self.reportes.mostrar_todos(self.crud.libros,self.EnBuscar,self.tabla))
  self.Mostrar.pack(side="left",padx=5)

  self.Reporte=tk.Button(self.frame_buscar,text="Reporte",command=lambda:self.reportes.reporte(self.crud.libros))
  self.Reporte.pack(side="left",padx=5)

# Treeview
  columnas = ("id", "nombre", "autor", "año")
  self.tabla = ttk.Treeview(self.ventana, columns=columnas, show="headings", height=8)

  self.tabla.heading("id", text="ID")
  self.tabla.heading("nombre", text="Nombre")
  self.tabla.heading("autor", text="Autor")
  self.tabla.heading("año", text="Año Publicación")


  self.tabla.column("id", width=30, anchor="center")
  self.tabla.column("nombre", width=150)
  self.tabla.column("autor", width=150)
  self.tabla.column("año", width=200)

  self.tabla.pack(fill="both", expand=True)

# Datos de paciente al formulario
  self.tabla.bind("<ButtonRelease-1>", lambda event: self.crud.seleccionar_Libro(event,self.tabla,self.EnNombre,self.EnAutor,self.EnAño))

  self.ventana.mainloop()
  
app = Biblioteca()