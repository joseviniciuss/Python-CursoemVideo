from random import shuffle

nome1 = str(input('Digite o nome do primerio aluno(a): '))
nome2 = str(input('Segundo aluno(a): '))
nome3 = str(input('Terceiro aluno(a): '))
nome4 = str(input('E por fim, o nome do quarto aluno(a): '))

lista = [nome1, nome2, nome3, nome4]
shuffle(lista)

print('A sequência selecionada foi {}.'.format(lista))
