import random


print('\n-----Bem vindo(a) ao Programa!-----')
print('\n-----VAMOS JOGAR PAR OU ÍMPAR------\n')

par = str('P')
impar = str('I')
soma = 0
contador = 0


while True:
    numero = int(input('\nDigite um número: '))
    escolha = str(input('Escolha PAR ou ÍMPAR [P/I]: ')).upper().strip()
    computador = random.randrange(0, 11)

    soma = numero + computador

    if(soma % 2 == 0):

        print(f'\nVocê jogou {numero} e o computador {computador}.\nSendo o resultado {soma} que no caso é um número PAR.')

        if(escolha == par):
            print('\n---VOCÊ GANHOU!!---\nJOGUE NOVAMENTE PARA CONQUISTAR UMA SEQUÊNCIA DE VITÓRIAS!!')
            contador += 1

        else:
            break

    else:

        print(f'\nVocê jogou {numero} e o computador {computador}.\nSendo o resultado {soma} que no caso é um número ÍMPAR. ')

        if(escolha == impar):
            print('\n---VOCÊ GANHOU!!---\nJOGUE NOVAMENTE PARA CONQUISTAR UMA SEQUÊNCIA DE VITÓRIAS!!')
            contador += 1

        else:
            break


print(f'\n---FIM DE JOGO---\nVocê perdeu!\nConquistando uma sequência de {contador} vitória(s).\n')