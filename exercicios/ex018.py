import math

angulo = float(input('Digite o valor do Ângulo:'))

cosseno = (math.cos(math.radians(angulo)))
seno = (math.sin(math.radians(angulo)))
tangente = (math.tan(math.radians(angulo)))

print('Valor do seno desse ângulo é {:.2f}, seu cosseno é {:.2f} e sua tangente {:.2f}.'.format(seno, cosseno, tangente))