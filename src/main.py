from calculadora import soma

print(soma(10, 20))

try:
    print(soma('10', 20))    
except AssertionError as e:
    print(f'Conta inválida: {e}')

print('Continuou o programa')

# try:
#     print(soma('10', 10))
# except TypeError as e:
#     print('Conta inválida')
#     print(e)