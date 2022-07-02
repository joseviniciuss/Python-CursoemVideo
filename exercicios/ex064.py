print('\n-----Bem vindo(a) ao Programa!-----')

contador = 0
contagem = 0
resultado = 0 
numeroNovo = 0

while(contador == 0):

    numero = int(input('\n   ---Digite um número---\nCaso queira parar, digite 999 :\n'))

    if(numero == 999):
        print('   ---Fim do programa---')
        contador = contador + 1
    
    else:

        calculo = numero + numeroNovo
        resultado = resultado + calculo
        contagem = contagem + 1

print('A quantidade de números digitados foi {}, e a soma de todos eles resultou em {}.\n'.format(contagem, resultado))
