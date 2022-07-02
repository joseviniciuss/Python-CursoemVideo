
anything = input('Por favor, digite algo:')

print('O tipo primitivo desse valor é:',type(anything))

print('{} só possui espaço?'.format(anything),anything.isspace())

print('{} é alfanúmerico?'.format(anything),anything.isalnum())

print('{} é alfabético?'.format(anything),anything.isalpha())

print('{} é maiúscula?'.format(anything),anything.isupper())

print('{} é decimal?'.format(anything),anything.isdecimal())

print('{} é minúscula?'.format(anything),anything.islower())

print('{} é um número?'.format(anything),anything.isnumeric())