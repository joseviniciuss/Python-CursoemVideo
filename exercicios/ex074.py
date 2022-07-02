import random

print('\nBem-vindo(a) ao Programa!\n')

numeros = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

numerosAleatorios = (random.choices(numeros, k=5))

print(f'Os valores sorteados foram {numerosAleatorios}.\n')

print(f'O maior valor foi {max(numerosAleatorios)}.\n')

print(f'O menor valor foi {min(numerosAleatorios)}.\n')

