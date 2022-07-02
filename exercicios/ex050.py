soma = 1
contagem = 0

for c in range(1,7):
    numero = int(input('Digite o {} número: '.format(soma)))
    soma = c + 1
    if(numero % 2 == 0):
        contagem = numero + contagem
print('A soma dos valores pares que você digitou é: {}.'.format(contagem))