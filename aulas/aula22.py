#MÓDULOS E PACOTES

#MÓDULOS
#Você pode criar modúlos ou seja "bibliotacas",
#e nela adicionar o que você deseja, por exemplo,
#funções e depois importar usando o comando 'import'.

#PACOTES
#usado quando existe uma sobercarga de códigos em um módulo,
#sendo possivel dividir por assuntos.

import mod

num = int(input(f"Digite um número inteiro : "))
fat = mod.fatorial(num)
print(f"O fatorial de {num} é {fat}.")
