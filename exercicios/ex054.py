
contador = 0 
contagem = 0

for c in range(1,8):
    anoNascimento = int(input('Digite o ano de nascimento da {} pessoa: '.format(c)))
    idade = 2022 - anoNascimento
    if(idade >= 21):
        contador = contador + 1 
    else:
        contagem = contagem + 1
print('A quantidade de maiores de 21 é {}.\nE a quantidade de menores de 21 é {}.'.format(contador,contagem))
