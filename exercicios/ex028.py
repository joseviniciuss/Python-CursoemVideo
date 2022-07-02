import random

numero = int(input('Digite um número entre 0 e 5:'))

numComputador = random.randrange(0,6)

if (numero == numComputador):
    print('Parabéns, você acertou o número! :)')
else:
    print('Infelizmente você não acertou o número. :(')
    