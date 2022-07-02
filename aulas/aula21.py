#FUNÇÕES
#PARTE 2

#INTERACTIVE HELP

    #help() - Ajuda a conhecer sobre algo do Python,
    #funções, bibliotecas entre outras opções.

    #help(print)
    #print(print.__doc__)

    #Colocar esse comando help() no terminal e 'quit' para sair.

#DOCSTRINGS
    
    #Irá mostra todo o conteúdo de uma função.
     
    
    #EXEMPLO

    #def cntador (i,f,p).
    #""""
    #--> Faz uma contagem e mostra na tela.
    #:param i: inicio da contagem
    #:param f: final da contagem
    #:param p: passo da contagem
    #:return: sem retorno
    #""""

#PARÂMETROS OPCINAIS

    #Atribui um valor a uma váriavel caso ela não seja declarada.
    

    #EXEMPLO

    #def somar(a=0,b=0,c=0)
    #Caso ao chamar a função não seja indicado qual o valor de alguma variavel,
    #já está sendo atribuido o valor no inicio da função.

#ESCOPO DE VARIAVÉIS

    #def teste(b):

        #global a          Vai utilizar o a global

        #a = 3             #ESCOPO LOCAL
        #b += 4            #ESCOPO LOCAL
        #c = 2             #ESCOPO LOCAL

        #print(f'A dentro vale {a}')
        #print(f'B dentro vale {b}')
        #print(f'C dentro vale {c}')
    
    #a = 5     #ESCOPO GLOBAL
    #teste(a)

#RETORNO DE VALORES

def somar(a=0,b=0,c=0):
    s = a + b + c
    return s

r1 = somar(1,2,3)
r2 = somar(1,2)
r3 = somar(1)

print(f'Os cálculos tiveram resultados r1 = {r1}, r2 = {r2}, r3 = {r3}.')