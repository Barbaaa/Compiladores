%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int yylex(void);
int yyerror(char *s) { printf("Error: %s\n", s); return 0; }

#define MAX_SIMB 200
typedef struct {
  char *nombre;
  int tipo;     // 0: variable, 1: función
  int aridad;   // # de parámetros si es función
  int ambito;
} Simbolo;

Simbolo tabla[MAX_SIMB];
int ntabla = 0;
int ambito_actual = 0;

void entrar_ambito() { ambito_actual++; }
void salir_ambito() {
  for (int i = 0; i < ntabla; i++)
    if (tabla[i].ambito == ambito_actual)
      tabla[i].nombre[0] = '\0';
  ambito_actual--;
}

void agregar_variable(char *id) {
  for (int i = 0; i < ntabla; i++)
    if (strcmp(tabla[i].nombre, id)==0 && tabla[i].ambito==ambito_actual) {
      printf("Error: redeclaración de '%s'\n", id);
      return;
    }
  tabla[ntabla++] = (Simbolo){strdup(id), 0, 0, ambito_actual};
}

void agregar_funcion(char *id, int aridad) {
  for (int i = 0; i < ntabla; i++)
    if (strcmp(tabla[i].nombre, id)==0 && tabla[i].tipo==1) {
      printf("Error: función '%s' ya declarada\n", id);
      return;
    }
  tabla[ntabla++] = (Simbolo){strdup(id), 1, aridad, 0};
}

int buscar_variable(char *id) {
  for (int a = ambito_actual; a >= 0; a--)
    for (int i = 0; i < ntabla; i++)
      if (tabla[i].nombre[0] && tabla[i].tipo==0 && tabla[i].ambito==a
          && strcmp(tabla[i].nombre, id)==0)
        return 1;
  return 0;
}

int buscar_funcion(char *id) {
  for (int i = 0; i < ntabla; i++)
    if (tabla[i].nombre[0] && tabla[i].tipo==1
        && strcmp(tabla[i].nombre, id)==0)
      return tabla[i].aridad;
  return -1;
}
%}

%union { char *str; int num; }
%token <str> ID
%token INT FUNC RETURN IGUAL
%token PARIZQ PARDER LLAVEIZQ LLAVEDER PUNTOYCOMA COMA
%type <num> parametros lista_param argumentos lista_args

%%

programa:
    elementos
  ;

elementos:
    elemento
  | elementos elemento
  ;

elemento:
    declaracion
  | instruccion
  | bloque
  ;

declaracion:
    INT ID PUNTOYCOMA
      { agregar_variable($2); }
  | FUNC ID PARIZQ parametros PARDER bloque
      { agregar_funcion($2, $4); }
  ;

instruccion:
    ID IGUAL ID PUNTOYCOMA
      { if (!buscar_variable($1) || !buscar_variable($3))
          printf("Error: identificador no declarado\n");
      }
  | ID PARIZQ argumentos PARDER PUNTOYCOMA
      {
        int e = buscar_funcion($1);
        if (e == -1)
          printf("Error: función '%s' no declarada\n", $1);
        else if (e != $3)
          printf("Error: función '%s' espera %d argumentos\n", $1, e);
      }
  | RETURN ID PUNTOYCOMA
      { if (!buscar_variable($2))
          printf("Error: identificador no declarado\n");
      }
  ;

bloque:
    LLAVEIZQ { entrar_ambito(); } elementos LLAVEDER { salir_ambito(); }
  ;

parametros:
    /* vacío */                           { $$ = 0; }
  | lista_param                           { $$ = $1; }
  ;

lista_param:
    ID                                    { agregar_variable($1); $$ = 1; }
  | lista_param COMA ID                   { agregar_variable($3); $$ = $1 + 1; }
  ;

argumentos:
    /* vacío */                           { $$ = 0; }
  | lista_args                            { $$ = $1; }
  ;

lista_args:
    ID                                    {
                                            if (!buscar_variable($1))
                                              printf("Error: identificador no declarado\n");
                                            $$ = 1;
                                          }
  | lista_args COMA ID                    {
                                            if (!buscar_variable($3))
                                              printf("Error: identificador no declarado\n");
                                            $$ = $1 + 1;
                                          }
  ;

%%

int main() { return yyparse(); }
