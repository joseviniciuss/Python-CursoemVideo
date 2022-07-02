salario = int(input('Digite o valor do seu sálario: '))

calculo1 = salario * 1.10
calculo2 = salario * 1.15

if (salario <= 1250):
    print('O aumento no seu sálario foi de 15%, passando a ser R${:.2f}.'.format(calculo2))
else:
    print('O aumento no seu sálario será de 10%, tornando a ser R${:.2f}.'.format(calculo1))
