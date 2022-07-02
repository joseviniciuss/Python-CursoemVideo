
expressao = str(input('Digite uma expressão : '))

parentesesInicio = expressao.count('(')
parentesesFinal = expressao.count(')')

if parentesesFinal == parentesesInicio:
    print('A expressão está correta!')
else:
    print('A expressão está errada!')




#OUTRA MANEIRA UTILIZANDO LISTAS:




calculo = str(input('Digite uma expressão : '))
lista = []

for parenteses in calculo:
    if parenteses == '(':
        lista.append('(')
    elif parenteses == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break

if len(lista) == 0:
    print('A expressão está correta!')
else:
    print('A expressão está errada!')

