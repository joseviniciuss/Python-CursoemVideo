
primeiroTermo = int(input('Digite o primerio termo da PA : '))
razao = int(input('Agora digite a razão da PA : '))

numeroN = 0
contador = 1
maisTermos = 1

while(contador <= 10):
    numeroN = primeiroTermo + (contador - 1) * razao
    contador = contador + 1
    print(numeroN)

while(maisTermos !=0):
    maisTermos = int(input('''Você deseja mostrar mais algum termo?\n1 - Sim\n2 - Não\n'''))
    
    while(maisTermos == 1):

     quantidadeDeTermos = int(input('Quantos termos você deseja que mostremos? '))

     calculo = 10 + quantidadeDeTermos
     contador2 = contador
     novoNumero = 0

     while(contador2 <= calculo):
        novoNumero = primeiroTermo + (contador2 - 1) * razao
        contador2 = contador2 + 1
        print(novoNumero)


if(maisTermos == 2):
    print('\nFim do Programa!')
