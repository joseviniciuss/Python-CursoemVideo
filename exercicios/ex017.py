import math

catetoOposto = float(input('Digite o valor do cateto oposto do triângulo retângulo: '))
catetoAdjacente = float(input('Digite o valor do cateto adjacente do triângulo retângulo: '))

hipotenusa = math.hypot(catetoOposto, catetoAdjacente)

print('O valor da Hipotenusa deste triângulo retângulo é: {}'.format(hipotenusa))