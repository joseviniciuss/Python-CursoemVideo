
contador = soma = 0

while True:

    numero = int(input('\nDigite um número \nCaso queira parar o programa digite (999) : '))

    if(numero == 999):
        break

    soma += numero
    contador += 1

print(f'\nA quantidade de valores digitados foi {contador}.\nE a soma entre todos eles resultou em {soma}.\n')