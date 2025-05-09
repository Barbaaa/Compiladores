%{
#include "parser.tab.h"
#include <string.h>
#include <stdlib.h>
int yywrap(void) { return 1; }
%}

%%
"func"                  { return FUNC; }
[0-9]+                  { return NUM; } // ← AÑADIDO: reconoce números enteros
[a-zA-Z_][a-zA-Z0-9_]*  { yylval.str = strdup(yytext); return ID; }
"("                     { return PARIZQ; }
")"                     { return PARDER; }
";"                     { return PUNTOYCOMA; }
","                     { return COMA; }
[ \t\n]+                ;
.                       { return yytext[0]; }
%%
