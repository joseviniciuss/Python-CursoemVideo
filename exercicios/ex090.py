dicionario =  {}

print()

nome =  str(input("Digite o nome: "))
media = float(input("Informe a média: "))

dicionario ['nome'] = nome
dicionario ['media'] = media

print('-'*20)

print(f"     O nome é {dicionario['nome']}.")
print(f"     A média é {dicionario['media']}.")

if media >= 7:
    dicionario['situacao'] = 'aprovado'
    print(f"     A situação do(a) aluno(a) é {dicionario['situacao']}! ")
else:
    dicionario['situacao'] = 'reprovado'
    print(f"     A situação do(a) aluno(a) é {dicionario['situacao']}! ")

print()

print(dicionario)