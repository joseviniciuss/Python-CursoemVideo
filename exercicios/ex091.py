import random
from time import sleep


dicionario = {}
novoDicionario = {}

contador = 1

print("\nValores sorteados : \n")

for c in range(1,5):

    valor = random.randint(1, 7)
    print(f"O jogador {c} tirou {valor} no dado.")    
    dicionario [f'jogador{c}'] = valor
    sleep(0.5)

print()
print('-'* 30)
print()

for i in sorted(dicionario, key = dicionario.get, reverse=True):

    novoDicionario [f'valor{contador}'] = dicionario[i] 
    print(f"{contador}º lugar :  {i} com {dicionario[i]}")
    contador += 1

print()


