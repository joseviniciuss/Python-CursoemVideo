print('\n-----Bem vindo(a) ao Programa!-----\n')

contador = 0
total = 0
produtoBarato = 0
nomeBarato = str('0')
contadorBarato = 0 
contagem = 0

while True:
    nome = str(input('\nDigite o nome do produto: '))

    valor = float(input('Informe o seu valor: R$ '))
    total += valor

    if(valor >= 1000):
        contador += 1
    
    if(contagem == 0):
        contadorBarato = valor
        contagem += 1

    if(valor <= contadorBarato):
        contadorBarato = valor
        nomeBarato = nome
        produtoBarato = valor

        
    finalizar = int(input('\nDeseja continuar?\n1 - SIM\n2 - NÃO\n'))

    if(finalizar == 2):
        break
    if(finalizar != 1 or finalizar != 2):

        while True:
            if(finalizar == 1 or finalizar == 2):
                break
            finalizar = int(input('\nDeseja continuar?\n1 - SIM\n2 - NÃO\n'))

        if(finalizar == 2):
            break


print(f'\nO valor gasto em toda a compra foi R${total}.\nA quantidade de produtos que custam mais que R$1.000 é {contador}.\nE o produto mais barato é {nomeBarato}, custando R${produtoBarato}.\n')
