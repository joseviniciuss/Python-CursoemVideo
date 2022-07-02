

def fatorial(numero, show = False):

    """
    --> Faz um cálculo fatorial.
    #:param numero: Número que será fatorado.
    #:param show: Define se irá mostra o cálculo do fatorial ou não. (opcional)
    #:return: O fatorial de um número retorna 'numero'.
    """

    
    calculo = 1
    contador = 0
    contadorDois = 0
    numeroDois = numero

    while (contador <= numero):

        calculo *= numero
        numero -= 1
        contador =+ 1
    
    print()
    print(f"O fatorial é: ")
    print('-'*50)

    if show == True:

       for c in range(0, numeroDois):

            if numeroDois > 1:

                print(f"{numeroDois} x", end=' ')
                numeroDois -= 1
            else:
                print(f"{numeroDois} = {calculo}.")
                print()

    else:

        print(f"{calculo}")
        print()


fatorial(2, show=True)
help(fatorial)