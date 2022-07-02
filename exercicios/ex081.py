
lista = []

contador = 0

while True:

    valor = int(input('\nDigite um valor : '))
    lista.append(valor)

    if valor == 5:
        contador += 1

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


lista.sort(reverse=True)
tamanho = len(lista)

print(f'\nVocê digitou {tamanho} números.')

print(f'\nA lista em ordem decrescente é {lista}.')

if 5 in lista:
    print(f'\nO valor (5) está contido {contador} vezes na lista!')
else:
    print('\nNão foi digitado nenhum valor (5).')


