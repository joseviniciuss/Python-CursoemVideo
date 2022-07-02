print('\n-----Bem vindo(a) ao Caixa Eletrônico!-----\n')

valor = int(input('Digite o valor que deseja sacar: R$'))
#total = valor

calculo1 = 0
calculo2 = 0
calculo3 = 0
calculo4 = 0

contadorCinquenta = 0 
contadorVinte = 0
contadorDez = 0
contadorUm = 0

while True:

    while(valor - 50 >= 0):

        calculo1 = valor - 50
        valor = calculo1
        contadorCinquenta += 1

    if(calculo1 <= 0):
        break

    while(valor - 20 >= 0):

        calculo2 = valor - 20
        valor = calculo2
        contadorVinte += 1

    if(calculo2 <= 0):
        break

    if(valor >= 10 ):
 
        while(valor - 10 >= 0):

            calculo3 = valor - 10
            valor = calculo3
            contadorDez += 1

    if(calculo3 <= 0):
        break

    if(valor >= 1):
        
        while(valor - 1 >= 0):

            calculo4 = valor - 1
            valor = calculo4
            contadorUm += 1

    if(calculo4 <= 0):
        break


print(f'\nTotal de {contadorCinquenta} cedúlas de R$50.0.\nTotal de {contadorVinte} cedúlas de R$20.0.\nTotal de {contadorDez} cedúlas de R$10.0.\nTotal de {contadorUm} cedúlas de R$1.0.\n')
print(f'Obrigado pela sua presença!\nVolte sempre!! :)\n')
