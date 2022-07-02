
nome = str(input('Digite o seu nome, por favor: '))

nomeM = nome.upper()
nomem = nome.lower()
nomeL = len(nome.strip()) - nome.count(' ')
nomePrimeiro = nome.find(' ')

print('Este é seu nome com todas as letras maiúsculas: {}' .format(nomeM)) 
print('Seu nome com todas as letras minúsculas é: {}'.format(nomem))
print('Seu nome possui {} letras.'.format(nomeL))
print('Seu primeiro nome possui {} letras.'.format(nomePrimeiro))