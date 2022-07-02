print('Bem vindo(a) ao meu programa!\nAqui iremos calcular seu IMC.')

altura = float(input('Digite a sua altura em metros: '))
peso = float(input('Digite o seu peso em kg: '))

imc = peso / (altura * altura)

if(imc < 18.5):
    print('Seu IMC é {:.2f}, estando abaixo do peso recomendado.'.format(imc))
elif(18.5 <= imc <= 24.9):
    print('Seu IMC é {:.2f}, que bom, você está no peso ideal.'.format(imc))
elif(25 <= imc <= 29.9):
    print('Seu IMC é {:.2f}, cuidado!\nVocê está em sobre peso.'.format(imc))
elif(29.9 < imc <= 30):
    print('Seu IMC é {:.2f}, preocupante seu estado.\nVocê está obeso.'.format(imc))
else:
    print('Seu IMC é {:.2f}, CUIDE-SE URGENTEMENTE, VOCÊ ESTÁ EM OBESIDADE MÓRBIDA!'.format(imc))