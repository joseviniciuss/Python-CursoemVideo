def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    a = open(nome,'wt+')
    a.close()

def lerArquivo(nome):
    a = open(nome, 'rt')
    for linha in a:
        dado = linha.split(':')
        dado[1] = dado[1].replace('\n', '')
        print(f'{dado[0]:<30}{dado[1]:>3} anos')
    a.close()

def cadastrar(arquivo, nome = 'desconhecido' ,idade=0):
    a = open(arquivo, 'at')
    a.write(f'{nome}:{idade}\n')
    a.close()

