numero = int(input('Digite um número inteiro, iremos mostrar o seu fatorial: '))

contador = 1
resultado = 1

while(contador <= numero):

    calculo = resultado * contador 
    contador = contador + 1
    resultado = calculo
    


print('O fatorial do número {}, é {}.'.format(numero, resultado))
