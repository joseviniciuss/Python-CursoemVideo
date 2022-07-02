dados = []
principal = []


maiorPeso = 0
menorPeso = 0

while True:
    nome = str(input('Nome : '))
    peso = float(input('Peso : '))

    dados.append(nome)
    dados.append(peso)

    if len(principal) == 0:
        maiorPeso = menorPeso = dados[1]
    else:
        if dados[1] > maiorPeso:
            maiorPeso = dados[1]
        if dados[1] < menorPeso:
            menorPeso = dados[1]

    principal.append(dados[:])

    continuar = str(input('\nDeseja continuar ? [S/N] ')).upper().strip()
    dados.clear()

    if continuar == 'N':
        break

quantidadePessoas = len(principal)

print(f'Foram cadastradas {quantidadePessoas} pessoas.')

print(f'O maior peso registrado é {maiorPeso}.', end=' ')

for p in principal:

    if p[1] == maiorPeso:
        print(f'[{p[0]}] ', end=' ')

print(f'\nO menor peso registrado é {menorPeso}.', end=' ')

for p in principal:

    if p[1] == menorPeso:
        print(f'[{p[0]}] ', end= ' ')

