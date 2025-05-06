from ply import lex, yacc

# Tokens
tokens = ('NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN')
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Carácter inválido: '{t.value[0]}'")
    t.lexer.skip(1)

# Reglas gramaticales
def p_input(p):
    '''
    input : expr
          | empty
    '''
    if p[1] is not None:
        print("Expresión válida")

def p_expr(p):
    '''
    expr : expr PLUS term
         | expr MINUS term
         | term
    '''
    p[0] = p[1]

def p_term(p):
    '''
    term : term TIMES factor
         | term DIVIDE factor
         | factor
    '''
    p[0] = p[1]

def p_factor(p):
    '''
    factor : LPAREN expr RPAREN
           | NUMBER
    '''
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = p[1]

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print("Expresión inválida")

lexer = lex.lex()
parser = yacc.yacc()

while True:
    try:
        s = input('Ingresa expresión aritmética: ')
        if not s.strip():
            continue
        parser.parse(s)
    except EOFError:
        break