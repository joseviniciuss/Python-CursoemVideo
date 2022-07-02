idade = int(input('Digite a sua idade: '))

if (idade <= 9):
    print('A sua categoria é MIRIM.')
elif (9 < idade <=14):
    print('A sua categoria é INFANTIL.')
elif (14 < idade <=19):
    print('A sua categoria é JUNIOR.')
elif (idade == 20):
    print('A sua categoria é SÊNIOR.')
else:
    print('A sua categoria é MASTER!')