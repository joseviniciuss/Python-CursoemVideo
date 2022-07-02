nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if (media < 5):
    print('Infelizmente você foi reprovado.\nPois sua média foi {}.'.format(media))
elif (4.9 < media < 7.0):
    print('Quase!\nVocê está de recuperação.\nPois sua média foi {}.'.format(media))
else:
    print('Parabéns!\nVocê foi aprovado!\nPois sua média foi {}.'.format(media))
