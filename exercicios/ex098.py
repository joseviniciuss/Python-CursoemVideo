import time


def contador(primeiro,ultimo,passo):

    print('-'*45)
    print(f'A contagem de {primeiro} até {ultimo}, pulando de {passo} em {passo} é: ')

    if passo < 0:
        passo *= -1

    if passo == 0:
        passo = 1

    if primeiro >= ultimo:

        while (primeiro >= ultimo):
            print(f'{primeiro}', end=' ', flush = True)
            time.sleep(0.5)

            primeiro -= passo

    else:
        while (primeiro <= ultimo):
            print(f'{primeiro}', end=' ', flush = True)
            time.sleep(0.5)

            primeiro += passo

    print('FIM!')
    


contador(1, 10, 1)

contador(10,0,2)

print('-'*45)
print('Agora é sua vez de personalizar!')
primeiro = int(input('Primeiro: '))
ultimo =   int(input('Último:   '))
passo =    int(input('Passo:    '))
contador(primeiro, ultimo, passo)