"""
class Pessoa
    __init__
        nome str
        sobrenome str
        dados_obtidos bool (inicia com o valor False)
    API:
        obter_todos_os_dados -> method
            OK
            404

            (dados_obtidos se torna True se dados obtifos com sucesso)
"""

try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
        )
    )

    print(
            os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__),
                    '../src'
                )
            )
    )

    print(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
    )

except:
    raise

import unittest
from unittest.mock import patch

from src.Pessoa import Pessoa

class TestPessoa(unittest.TestCase):
    def setUp(self): # Executado antes de cada método de teste
        self.p1 = Pessoa('Daniel', 'Figueiredo')
        self.p2 = Pessoa('Aline', 'Rocha')
        return super().setUp()

    def test_pessoa_attr_nome_tem_o_valor_correto(self):
        self.assertEqual(self.p1.nome, 'Daniel')
        self.assertEqual(self.p2.nome, 'Aline')

    def test_pessoa_attr_nome_e_str(self):
        self.assertIsInstance(self.p1.nome, str)
        self.assertIsInstance(self.p2.nome, str)

    def test_pessoa_attr_sobrenome_tem_o_valor_correto(self):
        self.assertEqual(self.p1.sobrenome, 'Figueiredo')
        self.assertEqual(self.p2.sobrenome, 'Rocha')

    def test_pessoa_attr_sobrenome_e_str(self):
        self.assertIsInstance(self.p1.sobrenome, str)
        self.assertIsInstance(self.p2.sobrenome, str)

    def test_pessoa_attr_dados_obtidos_inicia_false(self):
        self.assertFalse(self.p1.dados_obtidos)
        self.assertFalse(self.p2.dados_obtidos)


    def test_obter_todos_os_dados_sucesso_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p1.dados_obtidos)

            self.assertEqual(self.p2.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p2.dados_obtidos)

    def test_obter_todos_os_dados_falha_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False

            self.assertEqual(self.p1.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p1.dados_obtidos)

            self.assertEqual(self.p2.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p2.dados_obtidos)

    def test_obter_todos_os_dados_sucesso_e_falha_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p1.dados_obtidos)

            self.assertEqual(self.p2.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p2.dados_obtidos)

            fake_request.return_value.ok = False

            self.assertEqual(self.p1.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p1.dados_obtidos)

            self.assertEqual(self.p2.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p2.dados_obtidos)



    def tearDown(self): # Executado após cada método de teste
        # Só é executado se o método setUp foi executado com sucesso
        return super().tearDown()

if __name__ == '__main__':
    unittest.main(verbosity=2)
    