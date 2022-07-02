print('\n-----Bem vindo(a) ao Programa!-----')

maior = 0
menor = 0 
contador = 0
media = 0
contagem = 0
calculo = 0 

while(contador == 0):

    numero = int(input('\nDigite um número :'))

    if(numero > maior):
        maior = numero

    else:
        menor = numero

    contagem = contagem + 1

    cancelar = str(input('Caso deseje finalizar o programa digite (Sim/Não) : ')).upper().strip()
    sim = str('SIM')

    if(cancelar == sim):
        contador = contador + 1

    calculo = calculo + numero
    media = calculo / contagem

print('\nA média entre todos os valores digitados foi {:.2f}.\nSendo o maior valor digitado {}.\nE o menor valor digitado {}.'.format(media, maior, menor))
print('\n---Programa Finalizado---\n')