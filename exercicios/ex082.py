
lista = []
listaPares = []
listaImpares = []
valor = 0


while True:

    valor = int(input('\nDigite um valor : '))
    lista.append(valor)

    if valor % 2 == 0:
        listaPares.append(valor)
    else:
        listaImpares.append(valor)

    continuar = str(input('\nDeseja continuar ? [S/N] ')).upper().strip()

    if continuar == 'N':
        break

    if continuar != 'S':

        while True:

            continuar = str(input('\nDigite novamente : [S/N] ')).upper().strip()

            if continuar == 'S' or continuar == 'N':
                break

    if continuar == 'N':
        break

print(f'\nA lista digitada é {lista}.')
print(f'A lista somente com números pares é {listaPares}.')
print(f'A lista com números ímpares é {listaImpares}.\n')
