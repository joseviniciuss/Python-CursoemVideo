listaPrincipal =[[],[]]

for c in range(0,7):

    valor = int(input('Digite um valor : '))

    if valor % 2 == 0:
        listaPrincipal[0].append(valor)
    else:
        listaPrincipal[1].append(valor)
    

listaPrincipal[0].sort()
listaPrincipal[1].sort()

print(f'Os valores pares digitados foram : {listaPrincipal[0]}')
print(f'Os valores ímpares digitados foram : {listaPrincipal[1]}')
