
def leiaDinheiro(texto):
    
    valida = False
    while not valida:
        entrada = str(input(texto)).strip().replace(',', '.')
        if entrada.isalpha() or entrada == '':
            print(f"ERRO! '{entrada}' é um valor inválido.")
        else:
            valida = True
            return float(entrada)

