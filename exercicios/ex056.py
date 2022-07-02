contagemIdadeHomem = 0
contagemIdadeMulher = 0
contagemMedia = 0
contador = 0 


masculino = str('MASCULINO')
feminino = str('FEMININO')

for c in range(1,5):
    print('----{}ª pessoa----'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade : '))
    sexo = str(input('Sexo: '))

    nome1 = nome.upper()
    nome2 = ''.join(nome1.split())

    sexo1 = sexo.upper()
    sexo2 = ''.join(sexo1.split())

    if (idade > contagemIdadeHomem):
        contagemIdadeHomem = idade
        if(sexo2 == masculino):
         maisVelho = nome

    if(idade > contagemMedia):
        contador = contador + idade
        if(c == 4):
            media = contador / 4 
    
    if(sexo2 == feminino):
        if(idade < 20):
            contagemIdadeMulher = contagemIdadeMulher + 1

        
print('O homem mais velho é {}, com idade de {} anos.'.format(maisVelho,contagemIdadeHomem))
print('A média das idades de todos os participantes é {:.1f}.'.format(media))
print('Quantidade de mulheres com menos de 20 anos é {}.'.format(contagemIdadeMulher))
