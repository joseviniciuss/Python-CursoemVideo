numero = int(input('Digite um número inteiro:'))

escolha = int(input('Escolha qual será a base de conversão:\n-1 para binário\n-2 para octal\n-3 para hexadecimal\n'))

conversaoBinario = "{0:b}".format(numero)
conversaoOctal = "{0:o}".format(numero)
conversaoHexa = "{0:x}".format(numero)

if (escolha == 1):
    print('A conversão do número {} para binário será: {}.'.format(numero,conversaoBinario))
elif(escolha == 2):
    print('A conversão do número {} para octal será: {}.'.format(numero, conversaoOctal))
else:
    print('A conervsão do número {} para hexadecimal será: {}.'.format(numero, conversaoHexa))