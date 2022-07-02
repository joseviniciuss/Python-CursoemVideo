import random

print('Olá!\nBem-vindo(a) ao jogo de Jokenpô.\n\nVocê poderá escolher entre:\nPedra - (1)\nPapel - (2)\nTesoura - (3).\nDivirta-se!\n')

escolha = int(input('Jogue! : '))

lista = ('Pedra','Papel','Tesoura')
maquina = random.randint(1, 3)

if (escolha == 1):

    if(maquina == 1):
        print('Ninguém ganhou.\nVocê escolheu {}, e a máquina {}.'.format(lista[escolha], lista[maquina]))
    elif(maquina == 2):
        print('Infelizmente você perdeu. :(\nVocê escolheu {}, e a máquina {}.'.format(lista[escolha], lista[maquina]))
    else:
        print('Você ganhou!!\nParabéns!!\nVocê escolheu {}, e a máquina {}.'.format(lista[escolha], lista[maquina]))
elif (escolha == 2):

    if(maquina == 1):
        print('Você ganhou!!\nParabéns!!\nVocê escolheu {}, e a máquina {}.'.format(lista[escolha], lista[maquina]))
    elif(maquina == 2):
        print('Ninguém ganhou.\nVocê escolheu {}, e a máquina {}.'.format(lista[escolha], lista[maquina]))
    else:
        print('Infelizmente você perdeu. :(\nVocê escolheu {}, e a máquina {}.'.format(lista[escolha], lista[maquina]))
else:

    if(maquina == 1):
        print('Infelizmente você perdeu. :(\nVocê escolheu {}, e a máquina {}.'.format(lista[escolha], lista[maquina]))
    elif(maquina == 2):
        print('Você ganhou!!\nParabéns!!\nVocê escolheu {}, e a máquina {}.'.format(lista[escolha], lista[maquina]))
    else:
        print('Ninguém ganhou.\nVocê escolheu {}, e a máquina {}.'.format(lista[escolha], lista[maquina]))
