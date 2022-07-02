print('\n')
print('-'*48)
print('            Bem Vindo(a) ao Programa!')
print('-'*48)

lista = []

while True:

    valor = (int(input('\nDigite um valor : ')))

    if valor not in lista:
        lista.append(valor)
    else:
        print('Este valor já está na lista!')
        

    continuar = str(input('\nDeseja continuar [S/N] ? ')).upper().strip()
    
    if continuar == 'N':
        break

    if continuar != 'S':

        while True:
            continuar = str(input('Digite novamente [S/N] : ')).upper().strip()
            continuar = continuar

            if continuar == 'N' or continuar == 'S':
                break

    if continuar == 'N':
        break

lista.sort()
print('\n')
print(lista)
print('\n')