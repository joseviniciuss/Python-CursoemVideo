while True:

    print()
    print('-'*26)
    print('     SISTEMA DE AJUDA')
    print('-'*26)
    print()
    
    funcao = str(input("Função ou Biblioteca : "))

    fim = str('Fim')
    if funcao == fim:
        break

    ci = ('\033[1;33;40m')
    cf = ('\033[m')
    print(f'Acessando o manual da função ({funcao}).',ci)
    print()
    print(f'{help(funcao)}',cf)


print()
print('     FIM DO PROGRAMA!')
print()

