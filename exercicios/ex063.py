print('\n-----Bem vindo(a) ao Programa de Fibonacci!-----')

quantidadeDeNumeros = int(input('\nQuantos números você deseja que mostremos? '))

contador = 0

primeiroNumero = 0
segundoNumero = 1

proximoNumero = 0

while(contador < quantidadeDeNumeros):

    if(primeiroNumero == 0):

        print(primeiroNumero)
        contador = contador + 1

        print(segundoNumero)
        contador = contador + 1

    proximoNumero = primeiroNumero + segundoNumero

    contador = contador + 1

    print(proximoNumero)

    primeiroNumero = proximoNumero

    proximoNumero = primeiroNumero + segundoNumero

    contador = contador + 1

    print(proximoNumero)

    segundoNumero = proximoNumero

