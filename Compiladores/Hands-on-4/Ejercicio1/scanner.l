%{
#include "parser.tab.h"
#include <string.h>
#include <stdlib.h>
int yywrap(void) { return 1; }
%}
%%
"int"                   { return INT; }
[a-zA-Z_][a-zA-Z0-9_]*  { yylval.str = strdup(yytext); return ID; }
";"                     { return PUNTOYCOMA; }
[ \t\n]+                ;
.                       { return yytext[0]; }
%%
