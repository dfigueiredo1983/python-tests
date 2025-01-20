from typing import List, Union, Tuple, Dict, Any, NewType, Callable, Sequence, Iterable

# Primitivos
numero: int = 100
flutuante: float = 100.1
booleano: bool = True
string: str = 'Daniel Figueiredo'

# Sequeências
lista: List[int] = [1, 2, 3]
lista_int_str: List[Union[int, str]] = [1, 2, 3, 'Daniel']
tupla: Tuple[int, int, int, str] = (1, 2, 3, 'Daniel')

# Dicionários e conjuntos - sets
# Dicionário - chave: valor
# Dict[chave-tipo, valor-tipo]
pessoa: Dict[str, Union[str, int]] = {
    'nome': 'Daniel',
    'sobrenome': 'Figueiredo',
    'idade': 41,
}

MeuDict = Dict[str, Union[str, int, List[str]]]

pessoa_2: MeuDict = {
    'nome': 'Daniel',
    'sobrenome': 'Figueiredo',
    'idade': 41,
    'filhos': ['Pedro', 'Lara', 'Enzo', 'Gabriel'],
}

UserId = NewType('UserId', int)
user_id = UserId(215111)

# Callabla[Recebe, Devolve]
# Essa função recebe uma função como argumento que é um Callable
# e retorna a funç~]oes recebida que é um Callable
# def retorna_funcao(funcao: Callable[[], None]) -> Callable:
#     return funcao

# def fala_oi():
#     print('Oi')

# retorna_funcao(fala_oi)()

def retorna_funcao(funcao: Callable[[int, int], int]) -> Callable:
    return funcao

def soma(x: int, y: int) -> int:
    return x + y

# print(retorna_funcao(soma)(100, 20))

class Pessoa:
    def __init__(self, nome:str, sobrenome:str, idade:int, profissao:str) -> None:
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.idade: int = idade
        self.profissao: str = profissao
    
    def fala(self) -> None:
        print(f'{self.nome} {self.sobrenome} está falando....')

daniel = Pessoa('Daniel', 'Figueiredo', 41, 'Servidor publico')

# daniel.fala()

def iterar(sequencia: Sequence[int]):
    return [x for x in sequencia]

# print(iterar([1, 2, 3, 4, 5]))
# print(iterar([1, 2, 3, 4, 5, 'a']))

def iterar_2(sequencia: Iterable[int]):
    return [x for x in sequencia]

print(iterar_2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(iterar_2([1, 2, 3, 4, 5, 6, 7, 8, 9, 'a']))