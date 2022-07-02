#Interrompendo repetições while

#While Infinito ->

contador = 0

soma = 0 

while True:
    contador += 1

    if(contador == 11):
        break             #Como interromper um While
    
    print(contador)

while True:

    numero = int(input('Digite um número: '))

    if(numero ==  999):
        break

    soma += numero

print(f'A soma dos valores foi {soma}.')  #Nova maneira de escrever