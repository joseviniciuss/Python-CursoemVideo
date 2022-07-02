nome = str(input('Escreva alguma frase: ')).strip

nomeMinusculo = nome.lower()

letraA = nomeMinusculo.count('a')
primeiraLetraA = nomeMinusculo.find('a') + 1
ultimaLetraA = nomeMinusculo.rfind('a')


print('Nesta frase possui {} letras A.'.format(letraA))
print('A primeira letra A está na posição: {}.'.format(primeiraLetraA))
print('A última letra A está na posição: {}.'.format(ultimaLetraA))