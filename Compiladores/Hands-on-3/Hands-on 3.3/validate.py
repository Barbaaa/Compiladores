from ply import lex, yacc

# ---- 1. Definición de Tokens ----
tokens = (
    'NUMBER', 'BOOLEAN',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'AND', 'OR', 'NOT',
    'LPAREN', 'RPAREN'
)

# Reglas léxicas
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_AND = r'AND'
t_OR = r'OR'
t_NOT = r'NOT'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_BOOLEAN(t):
    r'0|1'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Error léxico: Carácter inválido '{t.value[0]}'")
    t.lexer.skip(1)

# ---- 2. Gramática ----
def p_expression(p):
    '''
    expression : expression PLUS term
              | expression MINUS term
              | expression AND term
              | expression OR term
              | term
    '''
    pass

def p_term(p):
    '''
    term : term TIMES factor
         | term DIVIDE factor
         | NOT factor
         | factor
    '''
    pass

def p_factor(p):
    '''
    factor : NUMBER
           | BOOLEAN
           | LPAREN expression RPAREN
    '''
    pass

def p_error(p):
    if p:
        print(f"Error sintáctico en '{p.value}'")
    else:
        print("Error: Expresión incompleta")
    raise SyntaxError

# Precedencia
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'NOT'),
)

# ---- 3. Ejecución ----
lexer = lex.lex()
parser = yacc.yacc()

def validate_expression(s):
    try:
        parser.parse(s)
        print("Expresión válida")
    except SyntaxError:
        pass  # El mensaje de error ya se mostró en p_error

if __name__ == '__main__':
    while True:
        try:
            s = input('Ingresa expresión: ').strip()
            if not s:
                continue
            validate_expression(s)
        except EOFError:
            break