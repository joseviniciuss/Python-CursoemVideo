dici = {}

print()
nome = str(input("Nome: "))
dici['nome'] = nome

nasceu = int(input("Ano de Nascimento: "))
dici['datadenascimento'] = nasceu
calculo = 2022 - nasceu
dici['idade'] = calculo

carteira = int(input("Carteira de Trabalho [(0) caso não tenha]: "))

if carteira != 0:

    dici['carteiradetrabalho'] = carteira

    contrato = int(input("Ano de Contratação: "))
    dici['anodecontrato'] = contrato

    salario = float(input("Salário: R$"))
    dici['salario'] = salario
else:
    dici['carteiradetrabalho'] = 'não possui carteira'

resultado = (contrato + 35) - nasceu
dici['aposentadoria'] = resultado


print('-'*42)

print(f"    - Nome é {dici['nome']}.")
print(f"    - Idade é {dici['idade']}.")
print(f"    - CTPS tem valor: ({dici['carteiradetrabalho']}).")

if carteira != 0:
    print(f"    - Ano em que foi contratado(a): {dici['anodecontrato']}.")
    print(f"    - Salário é R${dici['salario']}.")
    print(f"    - Irá se aposentar com {dici['aposentadoria']}")

print()

