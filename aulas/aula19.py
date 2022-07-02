#VARIÁVEIS COMPOSTAS
#DICIONÁRIOS

dicionario = {'idade':17,'nome':'José'}

print(dicionario.values())
print(dicionario.keys())
print(dicionario.items())
print(dicionario['idade'])


for c,v in dicionario.items():
    print(f'A chave é {c} e o valor dentro dela é {v}.')

dicionario['sexo'] = 'M'

print(dicionario)

del dicionario['nome']

print(dicionario)

#ORGANIZAR UM DICIONARIO

d = {'cachorro':2, 'gato':3, 'elefante':1 }

for i in sorted(d, key = d.get):
    print(i, d[i])
