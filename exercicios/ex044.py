valorInicial = float(input('Digite o valor inicial do produto: R$'))
pagamento = int(input('''Informe qual será o método de pagamento: 
\n1 - Á vista (dinheiro/cheque): 10% de desconto.
\n2 - Á vista no cartão: 5% de desconto.
\n3 - Em até 2x no cartão: preço normal.
\n4 - 3x ou mais no cartão: 20% de juros
\nEscolha uma opção:
'''))

descontode10 = valorInicial * 0.9
descontode5 = valorInicial - (valorInicial * 0.05)
aumentode20 = valorInicial * 1.20

if(pagamento == 1):
    print('O valor que será pago é: R${}.'.format(descontode10))
elif(pagamento == 2):
    print('O valor que será pago é: R${}.'.format(descontode5))
elif(pagamento == 3):
    print('O valor que será pago é: R${}.'.format(valorInicial))
else:
    print('O valor que será pago é: R${}.'.format(aumentode20))
