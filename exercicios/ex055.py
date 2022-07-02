
maior = 0
menor = 0

for c in range(1,6):
    peso = int(input('Digite o peso em kg da {} pessoa: '.format(c)))

    if (c == 1):
        maior = peso
        menor = peso
    else:
        if(peso > maior):
            maior = peso
        if(peso < menor):
            menor = peso

print('O maior peso foi {}kg.\nE o menor peso foi {}kg.'.format(maior, menor))
