def voto(anoDeNascimento):

    idade = 2022 - anoDeNascimento 
    
    if idade < 16:
        print(f'Você possui {idade} anos : VOTO NEGADO!\n')

    if idade >= 16 and idade < 18:
        print(f'Você possui {idade} anos : VOTO OPCIONAL!\n')

    if idade >= 18:
        print(f'Você possui {idade} anos : VOTO OBRIGATÓRIO!\n')


print()
print('-'*50)
anoDeNascimento = int(input('Qual foi o ano de seu nascimento? '))
voto(anoDeNascimento)