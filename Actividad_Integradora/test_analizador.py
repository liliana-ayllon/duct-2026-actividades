import unittest

from analizador import contar_frecuencias


class TestContarFrecuencias(unittest.TestCase):
    def test_recuento_basico(self):
        self.assertEqual(
            contar_frecuencias("sol luna sol"),
            {"sol": 2, "luna": 1},
        )

    def test_texto_vacio(self):
        self.assertEqual(contar_frecuencias(""), {})

    def test_mayusculas_y_minusculas(self):
        self.assertEqual(contar_frecuencias("Sol SOL sol"), {"sol": 3})

