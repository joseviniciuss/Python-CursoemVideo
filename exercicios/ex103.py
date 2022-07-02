
def ficha(nome = '<desconhecido>', gols = 0):


    print(f"-"*30)
    print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")
    print()


print()
print(f"-"*30)
nome = str(input(f"Nome do Jogador: "))
gols = int(input(f"Número de Gols: "))
ficha(nome, gols)