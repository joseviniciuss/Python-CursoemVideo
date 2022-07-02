#FUNÇÕES
#PARTE 1



#EXEMPLO - 1
def mostraLinha():
    print('-----------')

mostraLinha()


#EXEMPLO - 2
def mensagem(msg):
    print('-'*20)
    print(msg)
    print('-'*20)

mensagem('    Hello World')
mensagem('     Olá Mundo')


#EXEMPLO - 3
def contador(*num):
    tamanho = len(num)
    print(f'Os valores são {num} e ao todo contém {tamanho} número(s).')

contador(4,5,12,0)
contador(0,1,2)
contador(0)