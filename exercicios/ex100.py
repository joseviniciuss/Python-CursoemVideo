import random


numeros = []
numerosPares = []

def aleatorio(lista):
    
    for c in range(0,5):

        num = random.randint(1, 10)
        numeros.append(num)

    print(f'\nForam sorteados 5 valores: {lista}.')

def somaPar(lista_sorteada):

    soma = 0

    for c in lista_sorteada:

        if c % 2 == 0:
            numerosPares.append(c)
            soma += c

    print(f'\nOs valores pares da lista são: {numerosPares}.\nSomando esses valores temos {soma}.\n')





aleatorio(numeros)

somaPar(numeros)





