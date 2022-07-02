print('-----------------------------------------')
print('             LISTA DE PREÇOS          ')
print('-----------------------------------------')

tupla = ('Arroz', 4.50, 'Feijão', 7.00, 'Soja', 4.00, 'Frango', 25.00, 'Macarrão', 5.70)

contador = 0 
tamanho = len(tupla) 

for contador in range(0, tamanho, 2):
    print(f'{tupla[contador]:.<30}' f'R$ {tupla[contador + 1]:>7.2f}')


print('\n')