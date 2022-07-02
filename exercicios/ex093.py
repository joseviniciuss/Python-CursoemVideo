
print('-----CADASTRO DE JOGADOR-----')

dicionario = {}
gols = []

total = 0

nome =str(input('\nNome: '))
dicionario['nome'] = nome

partidas = int(input(f"Quantas partidas {dicionario['nome']} jogou? "))

dicionario['partidas'] = partidas

contpartidas = partidas + 1

print('-'*29)

for c in range(1, contpartidas):

    valor = int(input(f'     Quantos gols fez na {c}º partida? '))
    gols.append(valor)
    total += valor

dicionario['total_gols'] = total
dicionario['gols'] = gols


print('-'*29)
print(dicionario)
print('-'*29)


print(f"O campo nome tem valor {dicionario['nome']}.")
print(f"O campo gols tem valor {dicionario['gols']}.")
print(f"O total de gols é {dicionario['total_gols']}.")
print('-'*29)

print(f"O jogador {dicionario['nome']} jogou {dicionario['partidas']} partidas.")

for p,g in enumerate(dicionario['gols']):

    print(f"     Na partida {p + 1}º, fez {g} gols.")


print(f"No total fez {dicionario['total_gols']} gol(s).\n")




