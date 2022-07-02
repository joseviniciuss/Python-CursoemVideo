a = int(input('Digite o valor para a primeira reta: '))
b = int(input('Digite o valor para a segunda reta: '))
c = int(input('Sigite o valor para a terceira reta: '))

calculo1 = (b - c) < a < b + c
calculo2 = (a - c) < b < a + c
calculo3 = (a - b) < c < a + b

if (calculo1 and calculo2 and calculo3):
    print('É possível a criação deste triângulo com esses valores.')
else:
    print('Não é possível criar um triângulo com esses valores.')

