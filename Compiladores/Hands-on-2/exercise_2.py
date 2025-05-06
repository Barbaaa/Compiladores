import ply.lex as lex

# Lista de tokens
tokens = (
    'KEYWORD', 'IDENTIFIER', 'NUMBER', 'STRING'
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

def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]  # Elimina las comillas dobles
    return t

# Ignorar comentarios (de una línea y múltiples líneas)
def t_COMMENT(t):
    r'//.*|\/\*[\s\S]*?\*\/'
    pass  # Los comentarios no se devuelven como tokens

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
code = """
int x = 10; // Esto es un comentario de una línea
/* Esto es un comentario
   de múltiples líneas */
return "Hola, mundo!";
"""
lexer.input(code)
while tok := lexer.token():
    print(tok)