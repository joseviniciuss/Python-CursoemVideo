
d = int(input('Informe por quantos dias utilizou o carro: '))
r = int(input('Diga-me também quantos quilômetros você andou com ele: '))

v = (d * 60) + (r * 0.15)

print('O valor que você irá pagar é: R${}'.format(v))