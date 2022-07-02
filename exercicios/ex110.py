def resumo(numero = 0, desconto = 0, aumento = 0):

    print()
    print(f"""O valor é {numero}.
    Aumentando  {aumento}%, teremos {aumentar(numero, aumento, True)}.
    Diminuindo {desconto}% teremos {diminuir(numero, desconto, True)}.
    O seu dobro é {dobro(numero, True)}.
    A sua metade tem como valor {metade(numero, True)}.
    """)
    print()