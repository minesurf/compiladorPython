lexer grammar PythonLexer;

// ==========================================
// OPERADORES E SÍMBOLOS (Fase 1)
// ==========================================

// Operadores Aritmeticos
PLUS : '+' ;
MINUS : '-' ;
MULTIPLY : '*' ;
DOUBLE_STAR : '**' ;
DIVISION : '/' ;
DOUBLE_SLASH : '//';
MODULUS : '%' ;
AT : '@' ;
AMPERSAND : '&' ;
PIPE : '|' ;

// Operadores Relacionais
EQ_EQUAL : '==' ;
NOT_EQUAL : '!=' ;
GREATER : '>' ;
LESS : '<' ;
GREATER_EQUAL : '>=' ;
LESS_EQUAL : '<=' ;

// Operadores Bitwise / Booleanos Símbolos
XOR : '^';
TILDE : '~';

// Simbolos de atribuicao
PLUS_EQUAL : '+=' ;
MINUS_EQUAL : '-=' ;
MULTIPLY_EQUAL : '*=' ;
DOUBLE_STAR_EQUAL : '**=' ;
DIVISION_EQUAL : '/=' ;
MODULUS_EQUAL : '%=' ;
EQUALS : '=' ;

// Delimitadores / Identificadores de tipos e blocos
LPAREN : '(';
RPAREN : ')';
LBRACK : '[';
RBRACK : ']';
LBRACE : '{';
RBRACE : '}';
COLON : ':';
COMMA : ',';
DOT : '.';
SEMI : ';';

// ==========================================
// PALAVRAS-CHAVE (Fase 1)
// ==========================================

FALSE : 'False';
NONE : 'None';
TRUE : 'True';
AND : 'and';
AS : 'as';
ASSERT : 'assert';
BREAK : 'break';
CLASS : 'class';
CONTINUE : 'continue';
DEF : 'def';
DEL : 'del';
ELIF : 'elif';
ELSE : 'else';
EXCEPT : 'except';
FINALLY : 'finally';
FOR : 'for';
FROM : 'from';
GLOBAL : 'global';
IF : 'if';
IMPORT : 'import';
IN : 'in';
IS : 'is';
LAMBDA : 'lambda';
NONLOCAL : 'nonlocal';
NOT : 'not';
OR : 'or';
PASS : 'pass';
RAISE : 'raise';
RETURN : 'return';
TRY : 'try';
WHILE : 'while';
WITH : 'with';
YIELD : 'yield';

// Tipos de Dados
INT_TYPE : 'int';
FLOAT_TYPE : 'float';
STR_TYPE : 'str';
BOOL_TYPE : 'bool';
LIST_TYPE : 'list';
TUPLE_TYPE : 'tuple';
DICT_TYPE : 'dict';
SET_TYPE : 'set';

// Funcoes Built-in
PRINT : 'print';
INPUT : 'input';
LEN : 'len';
TYPE : 'type';
RANGE : 'range';
OPEN : 'open';
HELP : 'help';
SUM : 'sum';

// Outros padrões genéricos
FLOAT : [0-9]+ '.' [0-9]* | '.' [0-9]+ ;
STRING : '"' (~["\r\n])* '"' | '\'' (~['\r\n])* '\'' ;
COMMENT : '#' ~[\r\n]* -> skip ;
NEWLINE : '\r'? '\n' ;

// ==========================================
// DEFINIÇÕES FINAIS (Ordem Estrita da Fase 2)
// ==========================================

// 1. Identificadores 
ID : (LETTER | '_') (LETTER | DIGIT | '_')* ;

// 2. Letras 
fragment LETTER : [a-zA-Z] ;

// 3. Digitos
DIGIT : [0-9]+ ;

// 4. WS -> skip 
WS : [ \t]+ -> skip ;