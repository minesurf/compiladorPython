lexer grammar PythonLexer;

// Operadores Aritmeticos
PLUS: '+' ;
MINUS: '-' ;
MULTIPLY: '*' ;
DOUBLE_STAR: '**' ;
DIVISION: '/' ;
DOUBLE_SLASH : '//';
MODULUS: '%' ;
AT: '@' ;
AMPERSAND: '&' ;
PIPE: '|' ;

// Operadores Relacionais
EQ_EQUAL: '==' ;
NOT_EQUAL: '!=' ;
GREATER: '>' ;
LESS: '<' ;
GREATER_EQUAL: '>=' ;
LESS_EQUAL: '<=' ;

// Operadores Bitwise
XOR          : '^';
TILDE        : '~';

// Simbolos de atribuição
PLUS_EQUAL: '+=' ;
MINUS_EQUAL: '-=' ;
MULTIPLY_EQUAL: '*=' ;
DOUBLE_STAR_EQUAL: '**=' ;
DIVISION_EQUAL: '/=' ;
MODULUS_EQUAL: '%=' ;
EQUALS: '=' ;

// Delimitadores
LPAREN       : '(';
RPAREN       : ')';
LBRACK       : '[';
RBRACK       : ']';
LBRACE       : '{';
RBRACE       : '}';
COLON        : ':';
COMMA        : ',';
DOT          : '.';
SEMI         : ';';

//PALAVRAS-CHAVE (Keywords)
FALSE    : 'False';
NONE     : 'None';
TRUE     : 'True';
AND      : 'and';
AS       : 'as';
ASSERT   : 'assert';
BREAK    : 'break';
CLASS    : 'class';
CONTINUE : 'continue';
DEF      : 'def';
DEL      : 'del';
ELIF     : 'elif';
ELSE     : 'else';
EXCEPT   : 'except';
FINALLY  : 'finally';
FOR      : 'for';
FROM     : 'from';
GLOBAL   : 'global';
IF       : 'if';
IMPORT   : 'import';
IN       : 'in';
IS       : 'is';
LAMBDA   : 'lambda';
NONLOCAL : 'nonlocal';
NOT      : 'not';
OR       : 'or';
PASS     : 'pass';
RAISE    : 'raise';
RETURN   : 'return';
TRY      : 'try';
WHILE    : 'while';
WITH     : 'with';
YIELD    : 'yield';

// Tipos de Dados (Keywords de tipos)
INT_TYPE   : 'int';
FLOAT_TYPE : 'float';
STR_TYPE   : 'str';
BOOL_TYPE  : 'bool';
LIST_TYPE  : 'list';
TUPLE_TYPE : 'tuple';
DICT_TYPE  : 'dict';
SET_TYPE   : 'set';

// Funções Built-in
PRINT    : 'print';
INPUT    : 'input';
LEN      : 'len';
TYPE     : 'type';
RANGE    : 'range';
OPEN     : 'open';
HELP     : 'help';
SUM      : 'sum';

//DEFINIÇÕES FINAIS (Ordem Obrigatória) ---

//Identificadores
ID : [a-zA-Z_] [a-zA-Z0-9_]* ;

// Números
INTEGER : [0-9]+ ;
FLOAT   : [0-9]+ '.' [0-9]* | '.' [0-9]+ ;

// Strings
STRING : '"' (~["\r\n])* '"' | '\'' (~['\r\n])* '\'' ;

// Comentários
COMMENT : '#' ~[\r\n]* -> skip ;

//Espaços em Branco (WS) -> skip
WS : [ \t\r\n]+ -> skip ;