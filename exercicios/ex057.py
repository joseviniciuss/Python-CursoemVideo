
sexo = str(input('Digite o seu sexo, M ou F: ')).upper().strip()[0]

masculino = str('M')
feminino = str('F')

while sexo not in 'MF':
    sexo = str(input('Dados inválidos, por favor informe novamente: ')).upper().strip()[0]

if (sexo == masculino):
    print('Dados corretos.\nSeu sexo é {}.\nNo caso, MASCULINO.'.format(sexo))
else:
    print('Dados corretos.\nSeu sexo é {}.\nNo caso, FEMININO.'.format(sexo))
    