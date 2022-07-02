lista = []

maior = 0
menor = 0
contador = 0

for c in range(0,5):

    valor = int(input('Digite um valor : '))

    if c == 0 or valor > lista[-1]:
        lista.append(valor)
        print('O valor foi adicionado no final da lista!')

    else:
        posicao = 0

        while posicao < len(lista):

            if valor <= lista[posicao]:

                lista.insert(posicao, valor)
                print(f'O valor digitado foi adicionado na posição {posicao} da lista!')
                break
            
            posicao += 1
        


print('\n')
print(lista)
