%{
#include "parser.tab.h"
#include <string.h>
#include <stdlib.h>
int yywrap(void) { return 1; }
%}
%%
"int"                   { return INT; }
"func"                  { return FUNC; }
"return"                { return RETURN; }
[a-zA-Z_][a-zA-Z0-9_]*  { yylval.str = strdup(yytext); return ID; }
"("                     { return PARIZQ; }
")"                     { return PARDER; }
"{"                     { return LLAVEIZQ; }
"}"                     { return LLAVEDER; }
";"                     { return PUNTOYCOMA; }
","                     { return COMA; }
"="                     { return IGUAL; }
[ \t\n]+                ;    // ignora espacios y saltos de línea
.                       { return yytext[0]; }
%%
