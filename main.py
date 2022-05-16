'''
   NÃO MODIFIQUE ESTE ARQUIVO - autor MAC0122

   Este arquivo contem o programa principal do projeto.
'''

import os

# tk.tokeniza(),
import tokeniza as tk

# categorias e dicionario "categoria: decrição"
import operadores as op

import readFile as rf

PROMPT = "\nopcao >>> "
PROMPT2 = "\npath >>> "
PROMPT3 = "\nexpressão >>> "
QUIT = '3'

# ------------------------------------------------------------


def main():
    '''None -> None

    Programa que lê do teclado uma expressão aritmética
    e imprime cada item léxico na expressão.

    Exemplos:


    '''
    opcao = 0

    while opcao != QUIT:
        opcoes = ["\n1. Expressão a partir de arquivo",
                  "2. Escrever expressão", "3. Sair"]
        print("\nSelecione uma opção:\n" + '\n'.join(str(o) for o in opcoes))
        opcao = input(PROMPT).strip()

        if opcao == '1':
            print("\nEntre com o path do arquivo")
            path = input(PROMPT2)
            if os.path.exists(path):
                txt_arquivo = rf.lerArquivo(path)
                lista_tokens = tk.tokeniza(txt_arquivo)

                for token in lista_tokens:
                    # pegue item e tipo
                    item, tipo = token

                    # cri string com a descriçao
                    if tipo in [tk.OPERADOR, tk.PARENTESES, tk.COLCHETES]:
                        descricao = "'%s' : %s" % (item, op.DESCRICAO[item])
                    elif tipo == tk.VARIAVEL:
                        descricao = "'%s' : nome de variável" % item
                    elif tipo == tk.NUMERO:
                        descricao = "%f : constante float" % item
                    else:
                        descricao = "'%s' : categoria desconhecida" % item

                    # imprima a descriçao
                    print(descricao)
            else:
                print("\nArquivo não encontrado!")
        elif opcao == '2':
            print("\nEntre como uma expressão")
            expressao = input(PROMPT3)
            lista_tokens = tk.tokeniza(expressao)

            for token in lista_tokens:
                # pegue item e tipo
                item, tipo = token

                # cri string com a descriçao
                if tipo in [tk.OPERADOR, tk.PARENTESES, tk.COLCHETES]:
                    descricao = "'%s' : %s" % (item, op.DESCRICAO[item])
                elif tipo == tk.VARIAVEL:
                    descricao = "'%s' : nome de variável" % item
                elif tipo == tk.NUMERO:
                    descricao = "%f : constante float" % item
                else:
                    descricao = "'%s' : categoria desconhecida" % item

                # imprima a descriçao
                print(descricao)
        elif opcao == '3':
            pass
        else:
            opcao = input(
                "Opção inválida, por favor selecione uma opção válida:\n" + PROMPT).strip()


# -------------------------------------------
# início da execução do programa
main()
