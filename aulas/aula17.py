#Variáveis Compostas
#LISTAS

lista = ['Vinicius', 'Tenório', 'Bezerra', 'Silva']

print(lista)

list.append(lista, 'José')                             #Insere no final da lista
list.insert(lista, 0, 'José')                          #Insere no local desejado OU
#lista.insert(0, 'José')                               #Insere no local desejado

del lista[5]                                           #Deleta o objeto do local marcado
#lista.pop(0)                                          #Deleta o objeto do local marcado
lista.remove('Silva')                                  #Deleta o objeto marcando o conteúdo não a posição

print(lista)

valores = list(range(4,11))                            #Cria uma lista do 4 até o 10
valores.sort()                                         #Organiza em ordem 
#valores.sort(reverse=True)                            #Organiza em ordem contrária

len(valores)                                           #Descobrir o tamanho da lista

print(valores)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')