valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))


escolha = int(input('\nEscolha uma opção:\n\n    1 - Somar\n    2 - Multiplicar\n    3 - Maior valor\n    4 - Novos números\n    5 - Sair do Programa\n\n---- Qual é a sua opção? '))

while (escolha != 5):
    
    if(escolha == 1):
        soma = valor1 + valor2
        print('\nA soma entre {} e {}, foi {}.'.format(valor1,valor2,soma))

    elif(escolha == 2):
        multiplicação = valor1 * valor2
        print('\nA multiplicação entre {} e {}, é {}.'.format(valor1,valor2,multiplicação))

    elif(escolha == 3):

        if(valor1 > valor2):
            print('\nO maior valor é {}.'.format(valor1))
        elif(valor2 > valor1):
            print('\nO maior valor é {}.'.format(valor2))
        else:
            print('\nOs valores são iguais.')
    else:
        valor1 = int(input('\nDigite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
    
    escolha = int(input('\nEscolha uma opção:\n\n    1 - Somar\n    2 - Multiplicar\n    3 - Maior valor\n    4 - Novos números\n    5 - Sair do Programa\n\n---- Qual é a sua opção?'))


if(escolha == 5):
    print('\nVocê escolheu sair do programa!\n\n----FIM DO PROGRAMA!----')
