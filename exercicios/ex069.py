print('\n-----Bem vindo(a) ao Programa!-----\n')

contadorMaiorDeIdade = 0
contadorHomem = 0
contadorMulher = 0 

masculino = str('M')
feminino = str('F')

while True:

    sexo = str(input('\nDigite o sexo [M/F]: ')).upper().strip()
    if(sexo != masculino or sexo != feminino):
        while True:
            if(sexo == masculino or sexo == feminino):
                break
            sexo = str(input('\nDigite o sexo [M/F]: ')).upper().strip()
            

    idade = int(input('Digite a idade: '))


    if(idade >= 18):
        contadorMaiorDeIdade += 1

    if(sexo == masculino):
        contadorHomem += 1

    if(sexo == feminino):
        if(idade < 20):
            contadorMulher += 1


    finalizar = int(input('\nQuer finalizar o programa?\nDigite --\n1 - Sim\n2 - Não\n'))
    if(finalizar == 1):
        break
    if(finalizar != 1 or finalizar != 2):
        while True:
            if(finalizar == 1 or finalizar == 2):
                break
            finalizar = int(input('\nQuer finalizar o programa?\nDigite --\n1 - Sim\n2 - Não\n'))


print(f'\nA quantidade de pessoas maior de idade é {contadorMaiorDeIdade}.\nTendo {contadorHomem} homens cadastrados.\nE possui {contadorMulher} mulheres com menos de 20 anos.\n')
