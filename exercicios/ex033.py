x = int(input('Digite um valor para X: '))
y = int(input('Digite um valor para Y: '))
z = int(input('Digite um valor para Z: '))

print('\n')

if(x<z and x<y):
    print('O menor número foi x({:.1f}).'.format(x))
if(z<x and z<y):
    print('O menor valor foi z({:.1f}).'.format(z))
if(y<x and y<z):
    print('O menor número foi y({:.1f}).'.format(y)) 

if(x>y and x>z):
    print('O maior número foi X({:.1f}).'.format(x))
if(y>x and y>z):
    print('O maior número foi Y({:.1f}).'.format(y))
if(z>x and z>y):
    print('O maior número foi Z({:.1f}).'.format(z))
print('\n')
print('--- Fim do Programa. ---')