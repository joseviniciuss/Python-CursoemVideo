lado1 = int(input('Digite o lado 1 do triângulo: '))
lado2 = int(input('Digite o lado 2 do triângulo: '))
lado3 = int(input('Digite o lado 3 do triângulo: '))

if (lado1 == lado2 == lado3):
    print('Este triângulo é Equilátero.')
elif (lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
    print('Este triângulo é Isósceles')
else:
    print('Este triângulo é Escaleno')