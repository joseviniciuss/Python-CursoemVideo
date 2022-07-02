listaTotal = []
lista = []
dici = {}
listaMulher = []

masculino = str('M')
feminino = str('F')

sim = str('S')
nao = str('N')

soma = 0

while True:

    nome = str(input("Nome: "))
    dici['nome'] = nome

    sexo = str(input("Sexo: [M/F] ")).strip().upper()

    if (sexo != feminino or sexo != masculino):

        while True:

            if sexo == masculino or sexo == feminino:
                break
            else:
                print("ERRO! Digite apenas 'F' ou 'M'.")
                sexo = str(input("Sexo: [M/F] ")).strip().upper()

    dici['sexo'] = sexo

    if sexo == feminino:
        listaMulher.append(nome)

    idade = int(input("Idade: "))
    dici['idade'] = idade
    soma = soma + idade

    lista.append(dici.copy())
    dici.clear()

    continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()

    media = soma/ len(lista)

    if continuar != sim or continuar != nao:
        
        while True:

            if continuar == sim or continuar == nao:
                break
            else:
                print("ERRO! Digite apenas 'S' ou 'N'.")
                continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()

    if continuar == nao:
        break



print(f"\nA quantidade de pessoas cadastradas foram {len(lista)}.")
print(f'A média de todas as idades é {media:.1f}.')
print(f"As mulheres cadastradas foram {listaMulher}.")
print(f"A lista das pessoas com idade acima da média:\n    ")


for i in lista:

    if i['idade'] >= media:
        print('    ', end='')
        for k, v in i.items():
            print(f"{k} = {v}  ", end='')
        print()
