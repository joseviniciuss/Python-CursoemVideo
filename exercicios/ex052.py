numero = int(input('Digite um número inteiro, iremos calcular para saber se ele é primo: '))
contagem = 0 

for c in range (1, numero + 1):
    if(numero % c == 0 ):
        contagem = contagem + 1
if(contagem == 2):
    print('Este número é primo!\nPois número {} foi divisivel apenas por {} números.'.format(numero, contagem))
else:
    print('Este número não é primo!\nPois número {} foi divisivel por {} números.'.format(numero, contagem))

