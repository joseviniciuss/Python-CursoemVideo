
print('\nBem-vindo(a) ao Programa!\n')

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
numero3 = int(input('Digite mais um número: '))
numero4 = int(input('Digite o último número: '))

tupla = (numero1, numero2, numero3, numero4)

print(f'\nOs valores digitados foram {tupla}.\n')

print(f'O valor 9 foi digitado {tupla.count(9)} vezes.\n')

if 3 in tupla:
    print(f'O primeiro valor 3 foi digitado na {tupla.index(3)+1}ª posição.\n')
else:
    print(f'Não foi digitado nenhum número (3).\n')

print(f'Os valores digitados que são pares é ', end='')

for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')

print('\n')

