numero = int(input('Digite um número inteiro: '))

calculo = (numero % 2) == 0

if (calculo):
    print('Este número é par.')
else:
    print('Este número é ímpar.')