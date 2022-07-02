import random

lista = []
numeros = []

contador = 0 
print()
quantidade = int(input('Quantos jogos deseja sortear? '))
print()
for c in range (0,quantidade):

    for c in range(0,6):

        aleatorio = random.randrange(0,60)
        numeros.append(aleatorio)

    if len(numeros) == 6:

        lista.append(numeros[:])
        numeros.clear()


for v in range(1,quantidade + 1):

    print(f'Jogo {v} : {lista[contador]}')
    contador += 1
print()
