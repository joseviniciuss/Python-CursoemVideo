def linha():
    print('-'*25)


def area(l,c):
    areaTamanho = l * c
    print(f'A área do terreno com {l}m de largura e {c}m de comprimento é {areaTamanho}m.')


print('     MEDIDOR DE ÁREA')

linha()
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
linha()

area(l, c)
print()
