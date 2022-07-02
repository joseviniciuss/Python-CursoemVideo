def leiaInt(texto):
    while True:  

        try:
            numero = int(input(texto))

        except (ValueError, KeyboardInterrupt):

            print(f"ERRO! Foi encontrado um erro.")
            continue

        except Exception as erro:

            print(f"ERRO! Foi encontrado um erro em relação com {erro.__class__}.")
            continue
        else:
            return numero

def linha(tamanho = 40):
    return  '-' * tamanho


def titulo(texto = 'MENU PRINCIPAL'):
    print(linha())
    print(texto.center(40))
    print(linha())

def menu(lista):

    contador = 1

    titulo()

    for c in lista:
        print(f'{contador} - {c}')
        contador += 1
    print(linha())
    
    escolha = leiaInt('OPÇÃO: ')

    return escolha




