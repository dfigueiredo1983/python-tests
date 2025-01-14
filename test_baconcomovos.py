"""
    TDD - Test driven development - Desenvolvimento dirigido por testes
    Primeiro faz o teste e depois faz o desenvolvimento da função   
    
    Red 
    Parte 1 -> Criar o teste e ver ele falhar

    Green
    Parte 2 -> Criar o código e ver o teste passar

    Refactor
    Parte 3 -> Melhorar o código

    
"""

from baconcomovos import bacon_com_ovos
import unittest

class TestBaconComOvos(unittest.TestCase):
    def test_bacon_com_ovos_deve_levantar_assertion_error_se_nao_receber_int(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos('0')

    def test_bacon_com_ovos_deve_retornar_bacon_com_ovos_se_3_e_5_forem_multiplos_da_entrada(self):
        entradas = (
            15, 30, 45, 60, 75, 90, 105, 120
        )
        saida  = 'Bacon com ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)

    def test_bacon_com_ovos_deve_retornar_passar_fome_se_3_e_5_nao_forem_multiplos_da_entrada(self):
        entradas = (
            7, 31, 44, 67, 71, 92, 151, 181
        )
        saida  = 'Morrer de fome'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)

    def test_bacon_com_ovos_deve_retornar_bacon_se_entrar_for_mulitplo_de_3(self):
        entradas = (
            3, 6, 9, 12, 18, 21,
        )
        saida  = 'Bacon'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)

    def test_bacon_com_ovos_deve_retornar_ovos_se_entrar_for_mulitplo_de_5(self):
        entradas = (
            5, 10, 200, 250
        )
        saida  = 'Ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)



unittest.main(verbosity=2)


