lista = [[], [], []]

print()
for c in range(0,3):

    if c == 0:
        for v in range(0,3):
            valor = int(input(f'Digite um valor para [{c}, {v}] : '))
            lista[0].append(valor)

    if c == 1:
        for v in range(0,3):
            valor = int(input(f'Digite um valor para [{c}, {v}] : '))
            lista[1].append(valor)

    if c == 2:
        for v in range(0,3):
            valor = int(input(f'Digite um valor para [{c}, {v}] : '))
            lista[2].append(valor)

print()
print(f'[ {lista[0][0]} ] [ {lista[0][1]} ] [ {lista[0][2]} ]')
print(f'[ {lista[1][0]} ] [ {lista[1][1]} ] [ {lista[1][2]} ]')
print(f'[ {lista[2][0]} ] [ {lista[2][1]} ] [ {lista[2][2]} ]')
print()

