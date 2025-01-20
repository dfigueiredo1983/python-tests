import requests # type: ignore

class Pessoa:
    # self - a instância da classe, ou seja, tudo que a classe tem o método conhece em self
    # nome - str
    # sobrenome - str
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.dados_obtidos = False

    def obter_todos_os_dados(self):
        resposta = requests.get('https://jsonplaceholder.typicode.com/todos/1')

        if resposta.ok:
            self.dados_obtidos = True
            return 'CONECTADO'
        else:
            self.dados_obtidos = False
            return 'ERRO 404'