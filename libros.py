import unittest

class Libro:

    def __init__(self, nombre, isbn):
        self.nombre = nombre
        self.isbn = isbn

    def registrar_libro(self):
        return "Libro registrado"

    def buscar_libro(self):
        return self.nombre

    def actualizar_libro(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def eliminar_libro(self):
        self.nombre = ""

    def validar_isbn(self):
        return len(self.isbn) == 13


class TestLibro(unittest.TestCase):

    def setUp(self):
        self.libro = Libro(
            "Hasta que no queden mas estrellas que contar",
            "1234567890123"
        )

    def test_registrar_libro(self):
        self.assertEqual(
            self.libro.registrar_libro(),
            "Libro registrado"
        )

    def test_buscar_libro(self):
        self.assertEqual(
            self.libro.buscar_libro(),
            "Hasta que no queden mas estrellas que contar"
        )

    def test_actualizar_libro(self):
        self.libro.actualizar_libro("Nuevo Libro")
        self.assertEqual(
            self.libro.nombre,
            "Nuevo Libro"
        )

    def test_eliminar_libro(self):
        self.libro.eliminar_libro()
        self.assertEqual(
            self.libro.nombre,
            ""
        )

    def test_validar_isbn(self):
        self.assertTrue(
            self.libro.validar_isbn()
        )


if __name__ == "__main__":
    unittest.main()