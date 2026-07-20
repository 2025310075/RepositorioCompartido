class Libro:

    def __init__(self, nombre, isbn):
        self.nombre = nombre
        self.isbn = isbn


try:
    paginas = int(input("Ingrese el número de páginas: "))
except ValueError:
    print("Error: Debe ingresar un número válido.")


try:
    numero = int(input("Ingrese un número: "))
    resultado = 100 / numero
    print("Resultado:", resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")


try:
    raise ConnectionError
except ConnectionError:
    print("Error: No fue posible conectarse a la base de datos.")

libro = Libro("Hasta que no queden mas estrellas que contar", "1234567890123")


try:
    libro_eliminar = None

    if libro_eliminar is None:
        raise LookupError

except LookupError:
    print("Error: El libro que intenta modificar o eliminar no existe.")

try:
    nombre = input("Ingrese el nombre del libro: ")

    if nombre.strip() == "":
        raise ValueError

except ValueError:
    print("Error: El nombre del libro es obligatorio.")