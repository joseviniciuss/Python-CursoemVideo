soma = 0 
contador = 0
for c in range(1,501,2):
    if(c % 3 == 0):
        soma = soma + c
        contador = contador + 1

print('A soma de todos os valores que estão entre 1 e 500, e são divisiveis por 3 é {}!\nE a quantidade de valores nessa lista é {}.'.format(soma, contador))