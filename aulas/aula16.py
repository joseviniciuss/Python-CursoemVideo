#Variáveis Compostas
#Tuplas

#TUPLAS SÃO IMUTÁVEIS

lanche = ('Hambúrguer' , 'Suco' , 'Pudim', 'Pizza')
print(lanche[0])
print(lanche[-4])
print(lanche[0:2])
print(len(lanche))

for comida in lanche:
    print(f'Eu vou comer {comida}.')

for contador in range(0 , len(lanche)):
    print(f'Eu vou comer {lanche[contador]} na posição {contador}.')

for posicao, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {posicao}.')

print(sorted(lanche))#OrdemAlfabética