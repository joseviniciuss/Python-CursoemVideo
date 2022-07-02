
def nota(*num, sit = False):

    dici = {}

    tupla = num
    numeros = []

    quantidadeNumeros = 0
    media = 0

    for c in tupla:
        numeros.append(c)
        quantidadeNumeros += 1
        media += c
    
    media = media/quantidadeNumeros
    dici['Média'] = media
    
    if media == 10:
        dici['Situação'] = str('ótima')
    elif media >= 7:
        dici['Situação'] = str('boa')
    elif media >= 6:
        dici['Situação'] = str('razoável')
    elif media <= 4:
        dici['Situação'] = str('péssima')
    elif media < 6:
        dici['Situação'] = str('ruim')



    dici['QuantidadeDeNúmeros'] = quantidadeNumeros

    listaMaior = numeros
    listaMaior.sort(reverse=True)
    maiorNumero = listaMaior[0]
    dici['MaiorNúmero'] = maiorNumero

    listaMenor = numeros
    listaMenor.sort()
    menorNumero = listaMenor[0]
    dici['MenorNúmero'] = menorNumero
    
    print()
    print(f"""A quantidade de notas inseridas foram: {dici['QuantidadeDeNúmeros']}.
    A maior nota é {dici['MaiorNúmero']}.
    A menor nota é {dici['MenorNúmero']}.
    A média é {dici['Média']}.
    A situção do aluno(a) é {dici['Situação']}.""")
    print()


nota(1, 10, 1, 6.5, sit = True) 
