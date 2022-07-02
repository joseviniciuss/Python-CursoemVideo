print('-'*29)
print()
print('     CADASTRO DE JOGADOR')
print()

listaFinal = []
listaGol = []
dicionarioJogador = {}

contadorJogador = 0
total_gols = 0
sim = str('S')
nao = str('N')

while True:

    print('-'*29)
    nome = str(input(('Nome do Jogador: ')))
    dicionarioJogador['nome'] = nome
    contadorJogador += 1

    partidas = int(input('Quantas partidas o jogador jogou? '))
    dicionarioJogador['partidas'] = partidas

    for c in range(1,partidas + 1):
        gol = int(input(f'     Quantos gols na {c} partida? '))
        listaGol.append(gol)
        total_gols += gol
    print('-'*29)

    dicionarioJogador['total_gols'] = total_gols
    dicionarioJogador['gols'] = listaGol[:]

    listaFinal.append(dicionarioJogador.copy())
    dicionarioJogador.clear()
    total_gols = 0
    listaGol.clear()

    continuar = str(input('Deseja continuar [S/N] : ')).upper().strip()

    if continuar == nao:
        break
    
    if continuar != sim:
        while True:
            continuar = str(input('Você digitou errado, tente novamente : [S/N] ')).upper().strip()
            if continuar == sim or continuar == nao:
                break
    
    if continuar == nao:
        break
print('-'*29)
print('  Nome               Gols               Total')


for c in range(1,contadorJogador + 1):
    print(f'  {c} {listaFinal[c-1]["nome"]:<15}  {listaFinal[c-1]["gols"]}   {listaFinal[c-1]["total_gols"]}')

print('-'*29)

while True:

    pausar = int(input('Deseja mostrar os dados de qual jogador? (0 para parar)'))

    if pausar == 0:
        break

    print(f'Os dados do jogador {listaFinal[pausar-1]["nome"]}')
    for p, g in enumerate(listaFinal[pausar-1]["gols"]):
        print(f'    No jogo {p+1} fez {g} gols.')
    print('-'*29)