"""
    1 - Receber um número inteiro
    2 - Saber se o número é múltiplo de 3 e de 5
    Retorna baconcomovos
    3 - Saber se o número e múltiplo apenas de 3
    Retorna bacon
    4 - Saber se o número é múlitplo apenas de 5
    Retornar ovos
    5 Saber se o número não é múltiplo de 3 nem de 5
    Retornar morrer de fome
"""

def bacon_com_ovos(n):
    assert isinstance(n, int), 'n deve ser um valor inteiro'

    if n % 3 == 0 and n % 5 == 0:
        return 'Bacon com ovos'
    
    if n % 3 != 0 and n % 5 != 0:
        return 'Morrer de fome'
    
    if n % 3 == 0:
        return 'Bacon'
    
    if n % 5 == 0:
        return 'Ovos'
    

