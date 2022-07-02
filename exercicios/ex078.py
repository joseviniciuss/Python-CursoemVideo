print('\n')
print('-'*48)
print('            Bem Vindo(a) ao Programa!')
print('-'*48)

valores = []

for v in range(0,5):
    valores.append(int(input('Digite um valor : ')))

valores.sort()

print(f'\nVocê digitou os valores {valores}')



print(f'\nO maior valor da lista é {valores[4]}. \n')
print(f'O menor valor da lista é {valores[0]}. \n')
