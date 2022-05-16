
# Constantes
from lib2to3.pgen2.token import STRING
import token


TESTE   = False

# caracteres usados em operadores
OPERADORES = "%*/+-!^="

# caracteres usados em números inteiros
DIGITOS = "0123456789"

# ponto decimal
PONTO = "."

# todos os caracteres usados em um números float
FLOATS = DIGITOS + PONTO

# caracteres usados em nomes de variáveis
LETRAS  = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# abre e fecha parenteses
ABRE_FECHA_PARENTESES = "()"

# abre e fecha colchetes
ABRE_FECHA_COLCHETES = "[]"

# aspas
ASPAS_DUPLA = '"'
ASPAS_SIMPLES = "'"

# categorias
OPERADOR   = 1 # para operadores aritméticos e atribuição
NUMERO     = 2 # para números: todos são considerados float
VARIAVEL   = 3 # para variáveis
PARENTESES = 4 # para '(' e ')
COLCHETES  = 5 # para '[' e ']'
STRING     = 6 # para '"'e "'"

# Whitespace characters: space, newline, horizontal tab,
# vertical tab, form feed, carriage return
BRANCOS    = [' ', '\n', '\t', '\v', '\f', '\r']

# caractere que indica comentário
COMENTARIO = "#"


#------------------------------------------------------------
def tokeniza(exp):
    """(str) -> list

    Recebe uma string exp representando uma expressão e cria 
    e retorna uma lista com os itens léxicos que formam a
    expressão.

    Cada item léxico (= token) é da forma
       
        [item, tipo]

    O componente item de um token é 

        - um float: no caso do item ser um número; ou 
        - um string no caso do item ser um operador ou 
             uma variável ou um abre/fecha parenteses.

    O componente tipo de um token indica a sua categoria
    (ver definição de constantes acima). 

        - OPERADOR;
        - NUMERO; 
        - VARIAVEL; ou 
        - PARENTESES

    A funçao ignora tuo que esta na exp apos o caractere
    COMENTARIO (= "#").
    """
    # escreva o seu código abaixo
    lista_tokens = []
    indice = 0
    string_atual = ''
    float_atual = ''
    start_index_string = 0
    end_index_string = 0
    while indice < len(exp):

        if exp[indice] in COMENTARIO:
            break

        elif exp[indice] in OPERADORES:
            lista_tokens.append([exp[indice], OPERADOR])
        
        elif exp[indice] in ABRE_FECHA_PARENTESES:
            lista_tokens.append([exp[indice], PARENTESES])

        elif exp[indice] in ABRE_FECHA_COLCHETES:
            lista_tokens.append([exp[indice], COLCHETES])

        elif exp[indice] in DIGITOS:
            while indice < len(exp):
                if exp[indice] in DIGITOS or exp[indice] in PONTO:
                    float_atual += exp[indice]
                    indice += 1
                else:
                    break

            if len(float_atual) > 0:
                lista_tokens.append([float(float_atual), NUMERO])
                float_atual = ''

        elif exp[indice] in ASPAS_SIMPLES or exp[indice] in ASPAS_DUPLA or exp[indice]:
            if start_index_string is 0:
                start_index_string = indice
            if end_index_string is 0:
                end_index_string = indice
                string_atual = exp[start_index_string:end_index_string]
            
            if len(string_atual) > 0:
                lista_tokens.append([string_atual, STRING])
                string_atual = ''
                break

        elif exp[indice] in LETRAS or exp[indice] in ASPAS_SIMPLES or exp[indice] in ASPAS_DUPLA or exp[indice]:
            while indice < len(exp):
                if exp[indice] in DIGITOS or exp[indice] in LETRAS:
                    string_atual += exp[indice]
                    indice += 1
                else:
                    break

            if len(string_atual) > 0:
                lista_tokens.append([string_atual, VARIAVEL])
                string_atual = ''

        if indice + 1 <= len(exp):
            indice += 1

    return lista_tokens