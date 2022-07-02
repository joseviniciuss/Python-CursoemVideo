print('\n-----Bem vindo(a) ao Programa!-----')

contador = 0


while True:
    numero = int(input('\nDejesa saber a tabuada de qual número? '))

    if(numero < 0):
        break

    while(contador <=10 ):

     calculo = numero * contador

     print(f'{numero} x {contador} = {calculo}')

     contador += 1
  
    contador -= contador

print('\nPROGRAMA ENCERRADO!\nEspero ter ajudado :)\nAté logo.\n')
