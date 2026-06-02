parser grammar PythonParser;
options { tokenVocab=PythonLexer; }

// Regra inicial para a Fase 7
code : (stat | condicional | func | func_call | loop_while | loop_for | NEWLINE)* EOF ;

// Uma instrução simples
stat : (expr | query | atribuicao) NEWLINE? ;

atribuicao : (ID | PRINT) '=' expr ;

// Estrutura de repetição WHILE
loop_while
    : WHILE query COLON NEWLINE bloco # estruturaWhile
    ;

// Estrutura de repetição FOR usando range
loop_for
    : FOR ID IN RANGE LPAREN expr (COMMA expr)? RPAREN COLON NEWLINE bloco # estruturaFor
    ;

// Definição de Funções
func 
    : DEF ID LPAREN (ID (COMMA ID)*)? RPAREN COLON NEWLINE bloco # definicaoFuncao
    ;

// Chamada de Funções
func_call 
    : (ID | PRINT) LPAREN (expr (COMMA expr)*)? RPAREN # chamadaFuncao
    ;

// Condicionais
condicional
    : IF query COLON NEWLINE bloco (ELIF query COLON NEWLINE bloco)* (ELSE COLON NEWLINE bloco)? # estruturaCondicional
    ;

// Bloco que aceita os comandos e ignora linhas vazias
bloco
    : (stat | condicional | func | func_call | loop_while | loop_for | NEWLINE)+
    ;

// Expressões aritméticas e gerais
expr : LPAREN expr RPAREN                                                         # expressoesEntreParenteses
     | expr (MULTIPLY | DIVISION | DOUBLE_SLASH | MODULUS) expr                  # operacoesComExpressoes
     | expr (PLUS | MINUS) expr                                                   # operacoesComExpressoes
     | TRUE                                                                      # booleanosEmExpressao
     | FALSE                                                                     # booleanosEmExpressao
     | func_call                                                                 # chamadaFuncaoComoExpressao
     | ID                                                                        # ids
     | PRINT                                                                     # idsPrint
     | DIGIT                                                                     # numeros
     ;

// Expressões lógicas / Queries
query : (TRUE | FALSE)                                                             # valoresBooleanos
      | LPAREN query RPAREN                                                        # queryEntreParenteses
      | NOT query                                                                  # operacoesBooleanasEntreQuerys
      | query AND query                                                            # operacoesBooleanasEntreQuerys
      | query OR query                                                             # operacoesBooleanasEntreQuerys
      | expr (EQ_EQUAL | NOT_EQUAL | GREATER | LESS | GREATER_EQUAL | LESS_EQUAL) expr # relacoesEntreExpressoes
      ;