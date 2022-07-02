distancia = int(input('Diga a ditância total da viajem em Km: '))

calculo1 = distancia * 0.50
calculo2 = distancia * 0.45

if ( distancia <= 200):
    print('O valor que será pago é R${}.'.format(calculo1))
else:
    print('O valor que será pago é R${}.'.format(calculo2))
