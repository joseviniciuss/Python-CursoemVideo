idade = int(input('Digite em qual ano você nasceu: '))

menorde18 = 18 - (2022 - idade)
maiorde18 = (2022 - idade) - 18

if (idade == 2004):
    print('Você vai se alistar este ano.')
elif (idade > 2004):
    print('Você ainda vai se alistar.\nE falta {} ano(s) para seu alistamento.'.format(menorde18))
else:
    print('Já passou o tempo do alistamento.\nFaz {} ano(s) que era para ter se alistado.'.format(maiorde18))
    