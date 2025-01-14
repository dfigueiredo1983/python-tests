import unittest
from calculadora import soma

class TestCalcyuladora(unittest.TestCase):
    def test_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(soma(5, 5), 10)

    def test_soma_5_negativo_e_10_deve_retornar_5(self):
        self.assertEqual(soma(-5, 10), 5)

    def test_soma_varias_entradas(self):
        x_y_saidas = (
            (10, 10, 20),
            (100, 10, 110),
            (20, 100, 120),
            (200, -100, 100),
            (0, 10, 10),
        )

        for x_y_saida in x_y_saidas:
            print(*x_y_saida)
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(soma(x, y), saida)

    def test_soma_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma('10', 10)



unittest.main(verbosity=2)