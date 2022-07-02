listaPrincipal = []
listaTemporaria = []


while True:
    
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1:'))
    nota2 = float(input('Nota 2:'))

    media = (nota1 + nota2) / 2

    listaTemporaria.append(nome)
    listaTemporaria.append(nota1)
    listaTemporaria.append(nota2)
    listaTemporaria.append(media)

    listaPrincipal.append(listaTemporaria[:])
    listaTemporaria.clear()

    print()  
    continuar = str(input('Deseja continuar? ')).upper().strip()
    print()

    if continuar == 'N':
        break


print('-'*30)
print(f'Posição   Nome     Média')
for c in range(0,len(listaPrincipal)):
    print(f'{c}         {listaPrincipal[c][0]}       {listaPrincipal[c][3]}')
print('-'*30)
while True:

    nota = int(input('Mostrar as notas de qual aluno [posição]? (999 interrompe) : '))

    if nota == 999:
        break

    print()
    print(f'As notas do(a) aluno(a) {listaPrincipal[nota][0]}, foram [{listaPrincipal[nota][1],listaPrincipal[nota][2]}].')
    print()
