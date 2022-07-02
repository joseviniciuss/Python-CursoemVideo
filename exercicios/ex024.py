cidade = str(input('Digite o nome da cidade que você nasceu: ')).strip()

provandoSanto = cidade[:5].upper() == 'SANTO'

print('{}'.format(provandoSanto))