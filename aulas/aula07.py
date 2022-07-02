
#aula 07
#Ordem de Precedência
#1 - ()
#2 - **
#3 - * / // %
#4 - + -

n1 = int (input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))

s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
d_i = n1 // n2
p = n1 ** n2

print('A soma é {}, a subtração {}, a multiplicação {} e a divisão {:.2f}.'.format(s, sub, m, d))
print('A divisão inteira é {} e potenciação é {}'.format(d_i, p))