def escreva(frase):

    tamanho = len(frase) + 4

    print('~'*tamanho)
    print(f'  {frase}')
    print('~'*tamanho)

print()
frase = str(input('Digite uma frase: '))
print()
escreva(frase)
print()