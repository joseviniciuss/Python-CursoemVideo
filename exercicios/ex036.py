
valorCasa = int(input('Digite o valor da casa: R$'))
salario = int(input('Digite o salário do comprador: R$'))
tempo = int(input('Digite em quantos anos vai pagar: '))

quantidadeDeParcela = tempo * 12

parcela = valorCasa / (tempo * 12)

porcentagemSalario = salario * 0.3

if (parcela <= porcentagemSalario):
    print('Você poderá comprar esta casa, dividido em {} parcelas, no valor de R${:.2f}.'.format(quantidadeDeParcela, parcela))
else:
    print('Infelizmente, com seu salário atual, você não pode comprar esta casa! \nPois seu salário é R${}, e as parcelas serão de R${:.2f}, excedendo 30% de seu salário.'.format(salario, parcela))

