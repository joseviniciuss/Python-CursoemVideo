nome = str(input('Digite seu nome completo: ')).strip()

fraseSeparada = nome.split()

primeiroNome = fraseSeparada[0]
ultimoNome = fraseSeparada[len(fraseSeparada) - 1]

print('Prazer em te conhecer {}!'.format(nome))
print('Seu primeiro nome é: {}.'.format(primeiroNome))
print('Seu último nome é: {}'.format(ultimoNome))