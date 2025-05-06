import ply.lex as lex

# Lista de tokens
tokens = (
    'KEYWORD', 'IDENTIFIER', 'NUMBER'
)

# Definición de palabras clave
keywords = {'int': 'KEYWORD', 'return': 'KEYWORD'}

# Expresiones regulares para tokens

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value, 'IDENTIFIER')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Carácter ilegal: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

# Prueba del analizador
code = "int x = 10; return x;"
lexer.input(code)
while tok := lexer.token():
    print(tok)