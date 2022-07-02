print('Bem-vindo(a) ao Programa!')

numeros = ('zero' , 'um', 'dois', 'três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove', 'vinte')

posicao = int(input('Digite um número entre 0 e 20 : '))

while True:

    if(posicao <= 20):
        print(f'O número ({posicao}) por extenso é {numeros[posicao]}.')
        break

    posicao = int(input('Digite novamente.\nTente outro número : '))

