
def aumentar(numero = 0, desconto = 0, moeda = False):
    numero = numero + (numero * (desconto/100))

    if moeda == True:
        numero = str(f"R${numero:.2f}")
    return numero


def diminuir(numero = 0, desconto = 0 , moeda = False):

    numero = numero - (numero * (desconto/100))

    if moeda == True:
        numero = str(f"R${numero:.2f}")
    return numero


def dobro(numero = 0, moeda = False):
    numero *= 2

    if moeda == True:
        numero = str(f"R${numero:.2f}")
    return numero


def metade(numero = 0, moeda = False):
    numero = numero / 2

    if moeda == True:
        numero = str(f"R${numero:.2f}")
    return numero


def resumo(numero = 0, desconto = 0, aumento = 0):

    print()
    print(f"""O valor é {numero}.
    Aumentando  {aumento}%, teremos {aumentar(numero, aumento, True)}.
    Diminuindo {desconto}% teremos {diminuir(numero, desconto, True)}.
    O seu dobro é {dobro(numero, True)}.
    A sua metade tem como valor {metade(numero, True)}.
    """)
    print()
