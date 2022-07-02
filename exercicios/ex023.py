numero = str(input('Digite um número de 0 até 9999: '))
numeroInt = int(numero)

u = numero[3]
d = numero[2]
c = numero[1]
m = numero[0]

print('A unidadde é: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
