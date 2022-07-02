
def leiaInt(texto):

    global numero

    numero = input(texto)

    if numero != numero.isnumeric():

        while True:
            
            if numero.isnumeric():
                break

            print(f"ERRO! Digite um número inteiro válido.")
            numero = input(texto)


n = leiaInt('Digite um número: ')
print(f"Você acabou de digitar o número {numero}.")