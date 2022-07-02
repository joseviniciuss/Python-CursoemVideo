lista = [[], [], []]

somaPares = 0
somaColunaTres = 0
maior = 0

print()
for c in range(0,3):

    if c == 0:
        for v in range(0,3):

            valor = int(input(f'Digite um valor para [{c}, {v}] : '))
            lista[0].append(valor)

            if valor % 2 == 0:
                somaPares += valor

    if c == 1:
        for v in range(0,3):

            valor = int(input(f'Digite um valor para [{c}, {v}] : '))
            lista[1].append(valor)

            if valor % 2 == 0:
                somaPares += valor

            if valor >= maior:
                maior = valor

    if c == 2:
        for v in range(0,3):

            valor = int(input(f'Digite um valor para [{c}, {v}] : '))
            lista[2].append(valor)

            if valor % 2 == 0:
                somaPares += valor

somaColunaTres = lista[0][2] + lista[1][2] + lista[2][2]
#Existe outra maneira colocando 'if'

print()
print(f'[ {lista[0][0]} ] [ {lista[0][1]} ] [ {lista[0][2]} ]')
print(f'[ {lista[1][0]} ] [ {lista[1][1]} ] [ {lista[1][2]} ]')
print(f'[ {lista[2][0]} ] [ {lista[2][1]} ] [ {lista[2][2]} ]')
print()

print(f'A soma dos valores pares é : ({somaPares})')
print(f'A soma dos valores da terceira coluna é : ({somaColunaTres})')
print(f'O maior valor da segunda linha é ({maior}).')
print()
