nombre = input("Ingrese su nombre: ")

while True:
    try:
        edad = int(input("Ingrese su edad: "))
        break
    except ValueError:
        print("Ingrese un número válido")
        
print(f"Hola {nombre} tienes {edad} años")