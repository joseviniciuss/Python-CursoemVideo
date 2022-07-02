print('\n')
print('-'*48)
print('            Bem Vindo(a) ao Programa!')
print('-'*48)


tupla = ('ISABEL', 'VINICIUS', 'GENAINA', 'EDIVAN', 'ANETE', 'JOSE', 'MARIA')


for contador in tupla:
    print(f'\nA palavra {contador}, possui as seguintes vogais : ', end=' ')
    for letra in contador:
        if letra in 'AEIOU':
            print(letra, end=' ')

print('\n')
