from ex115.modulo import *
from ex115.arquivo import *
from time import sleep

arquivo = 'aquivo.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:

    escolha = menu(['Visualizar Cadastros', 'Novo Cadastramento', 'Sair do Sistema'])

    if escolha == 1:
        titulo('Visualizar Cadastros')
        lerArquivo(arquivo)

        
    elif escolha == 2:

        titulo('Novo Cadastramento')

        nome = str(input('Nome: '))

        idade = leiaInt('Idade: ')

        cadastrar(arquivo,nome,idade)

        print(f"Cadastro de {nome} feito com sucesso.")


    elif escolha == 3:
        titulo('SAINDO DO SISTEMA...')
        break
    else:
        print('ERRO! Digite uma opção existente!')
    sleep(1)

