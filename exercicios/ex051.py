primeiroTermo = int(input('Digite o primerio termo da PA :'))
razao = int(input('Agora digite a razão da PA : '))
numeroN = 0


for c in range(1,11):
    numeroN = primeiroTermo + (c - 1) * razao
    print(numeroN)
    
             
