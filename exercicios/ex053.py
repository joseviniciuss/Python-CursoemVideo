frase = str(input('Digite uma frase, para saber se ela é um políndromo: '))
frase1 = frase.upper()
frase2 = ''.join(frase1.split())

frase3 = frase2[::-1]

if(frase3 == frase2):
     print('Esta frase é um políndromo!\nA frase ao contrário é {}.'.format(frase3))
else:
     print('Esta frase não é um políndromo!\nA frase ao contrário é {}'.format(frase3))

