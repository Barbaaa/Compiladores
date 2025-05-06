import ply.lex as lex

# Lista de tokens
tokens = (
    'KEYWORD', 'IDENTIFIER', 'NUMBER', 'STRING', 'OPERATOR', 'DELIMITER'
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

# Comentarios (deben definirse antes que los operadores)
def t_COMMENT(t):
    r'//.*|\/\*[\s\S]*?\*\/'
    pass  # Los comentarios no se devuelven como tokens

# Operadores
def t_OPERATOR(t):
    r'[\+\-\*/=]'
    return t

def t_DELIMITER(t):
    r'[\(\)\{\};,]'
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

# Contadores para cada tipo de token
counters = {
    'KEYWORD': 0,
    'IDENTIFIER': 0,
    'NUMBER': 0,
    'STRING': 0,
    'OPERATOR': 0,
    'DELIMITER': 0,
}

# Función para contar tokens
def count_tokens(code):
    lexer.input(code)
    while tok := lexer.token():
        if tok.type in counters:
            counters[tok.type] += 1
    return counters

# Prueba del analizador
code = """
int main() {
    int x = 10 / 2; // Esto es un comentario
    return "Hola, mundo!";
}
"""

# Contar tokens en el código
token_counts = count_tokens(code)

# Mostrar resultados
print("Conteo de tokens:")
for token_type, count in token_counts.items():
    print(f"{token_type}: {count}")