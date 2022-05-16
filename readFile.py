def lerArquivo(path_file):
    with open(path_file, 'r', encoding='utf-8') as file:
        texto = file.readlines()

    texto_formatado = ''.join([str(t) for t in texto])

    return texto_formatado