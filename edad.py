nombre = input("Ingrese su nombre: ")

while True:
    try:
        edad = int(input("Ingrese su edad: "))
        break
    except ValueError:
        print("Ingrese un número válido")
        
print("-------------------")
print("-DATOS DEL USUARIO-")
print("-------------------")
print("Nombre:", nombre)
print("Edad:", edad)