'''
   NÃO MODIFIQUE ESTE ARQUIVO - autor MAC0122

   Este arquivo contem o programa principal do projeto.
'''

# tk.tokeniza(),
import tokeniza as tk

# categorias e dicionario "categoria: decrição"
import operadores as op

import readFile as rf

PROMPT = "expressão >>> "
QUIT = 3

# ------------------------------------------------------------


def main():
    '''None -> None

    Programa que lê do teclado uma expressão aritmética
    e imprime cada item léxico na expressão.

    Exemplos:


    '''
    opcao = 0

    while int(opcao) != QUIT:
        opcoes = ["\n1. Expressão a partir de arquivo",
                  "2. Escrever expressão", "3. Sair"]
        print("Selecione uma opção:\n" + '\n'.join(str(o) for o in opcoes))
        opcao = input(PROMPT)

        if int(opcao) == 1:
            print("Entre com o path do arquivo ou tecle ENTER para encerrar.")
            path = input(PROMPT)
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
        elif int(opcao) == 2:
            print("Entre como uma expressão ou tecle apenas ENTER para encerrar.")
            expressao = input(PROMPT)
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
        elif int(opcao) == 3:
            pass
        else:
            opcao = input(
                "Opção inválida, por favor selecione uma opção válida:\n" + PROMPT)


# -------------------------------------------
# início da execução do programa
main()
