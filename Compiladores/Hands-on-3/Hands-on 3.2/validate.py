from ply import lex, yacc

# Tokens
tokens = ('BOOLEAN', 'AND', 'OR', 'NOT', 'LPAREN', 'RPAREN')

# Reglas léxicas
t_AND = r'AND'
t_OR = r'OR'
t_NOT = r'NOT'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_BOOLEAN(t):
    r'0|1'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"Carácter inválido: '{t.value[0]}'")
    t.lexer.skip(1)

# Reglas gramaticales
def p_input(p):
    '''
    input : logical_expr
          | empty
    '''
    if p[1] is not None:
        print("Expresión válida")

def p_logical_expr(p):
    '''
    logical_expr : logical_expr AND logical_term
                | logical_expr OR logical_term
                | logical_term
    '''
    p[0] = p[1]

def p_logical_term(p):
    '''
    logical_term : NOT logical_factor
                | logical_factor
    '''
    p[0] = p[1]

def p_logical_factor(p):
    '''
    logical_factor : LPAREN logical_expr RPAREN
                  | BOOLEAN
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

# Configuración
lexer = lex.lex()
parser = yacc.yacc()

# Ejecución
while True:
    try:
        s = input('Ingresa expresión lógica: ')
        if not s.strip():
            continue
        parser.parse(s)
    except EOFError:
        break