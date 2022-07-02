
primeiroTermo = int(input('Digite o primerio termo da PA :'))
razao = int(input('Agora digite a razão da PA : '))
numeroN = 0
contador = 1


while(contador <= 10):
    numeroN = primeiroTermo + (contador - 1) * razao
    contador = contador + 1
    print(numeroN)
    