print('\n')

velocidade = int(input('Informe a velocidade que seu carro está (em km/h): '))

velocidadeMaxima = 80

multa = (velocidade - velocidadeMaxima) * 7.0

if (velocidade <= velocidadeMaxima):
    print('Você está dentro do limite de velocidade.')
else:
    print('Você excedeu o limite de velocidade, o valor da sua multa será: R${:.2f}'.format(multa))
    
print('\n')