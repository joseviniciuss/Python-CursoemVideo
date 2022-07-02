

def maior(*num):

    if len(num) == 0:
        
        print('-'*60)
        print('Analisando os valores passados...')
        print(f'Foram informados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi 0.')
    
    if len(num) > 0:

        print('-'*60)
        print('Analisando os valores passados...')
        print(f'{num}')
        print(f'Foram informados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi {max(num)}.')

    

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()


