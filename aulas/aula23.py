#Tratamento de Erros e Exceções

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except ZeroDivisionError:
    print('Não é possível dividir um número por zero.')
except Exception as erro:
    print(f'PROBLEMA! O problema encontrado foi {erro.__class__}')
else:
    print("DEU CERTO!")
    print(f"O seu resultado é {r:.2f}.")
finally:
    print("Volte sempre!")