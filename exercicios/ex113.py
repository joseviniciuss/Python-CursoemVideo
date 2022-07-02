
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

def leiaFloat(texto):

    while True:  

        try:
            numero = float(input(texto))

        except (ValueError, KeyboardInterrupt):

            print(f"ERRO! Foi encontrado um erro.")
            continue

        except Exception as erro:

            print(f"ERRO! Foi encontrado um erro em relação com {erro.__class__}.")
            continue
        else:
            return numero


inteiro = leiaInt('Digite um Inteiro: ')
real = leiaFloat('Digite um Real: ')
print(f"Você acabou de digitar o número {inteiro}(inteiro) e {real}(real).")