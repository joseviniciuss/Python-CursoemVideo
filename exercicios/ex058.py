import random

numero = int(input('Digite um número entre 0 e 10:'))

numComputador = random.randrange(0,11)

while (numero != numComputador):
    numero = int(input('Você ainda não acertou, digite novamente:\n'))

if (numero == numComputador):
    print('Parabéns, você acertou o número! :)')

    