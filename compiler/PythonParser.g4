parser grammar PythonParser;
options { tokenVocab=PythonLexer; }

// Regra inicial para a Fase 8
code : (stat | condicional | func | func_call | loop_while | loop_for | NEWLINE)* EOF ;

// Uma instrução simples
stat : (expr | query | atribuicao | returnStmt) NEWLINE? ;

atribuicao : (ID | PRINT) '=' expr ;

returnStmt : RETURN expr # returnStmtt ;

// Estrutura de repetição WHILE
loop_while
    : WHILE query COLON NEWLINE bloco # estruturaWhile
    ;

// Estrutura de repetição FOR usando range ou coleções iteráveis
loop_for
    : FOR ID IN (RANGE LPAREN expr (COMMA expr)? RPAREN | expr) COLON NEWLINE bloco # estruturaFor
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

// Expressões aritméticas, gerais e Estruturas de Dados (Fase 8)
expr : LPAREN expr RPAREN                                                         # expressoesEntreParenteses
     | <assoc=right> expr DOUBLE_STAR expr                                        # operacoesComExpressoes
     | expr (MULTIPLY | DIVISION | DOUBLE_SLASH | MODULUS) expr                  # operacoesComExpressoes
     | expr (PLUS | MINUS) expr                                                   # operacoesComExpressoes
     | TRUE                                                                      # booleanosEmExpressaoTrue
     | FALSE                                                                     # booleanosEmExpressaoFalse
     | func_call                                                                 # chamadaFuncaoComoExpressao
     | ID                                                                        # ids
     | PRINT                                                                     # idsPrint
     | DIGIT                                                                     # numeros
     | FLOAT                                                                     # floats
     | STRING                                                                    # stringsEmExpressao
     | lista                                                                     # listaEmExpressao
     | tupla                                                                     # tuplaEmExpressao
     | set_dados                                                                 # setEmExpressao
     | dicionario                                                                # dicionarioEmExpressao
     ;

// --- Estruturas de Dados Avançadas (Fase 8) ---

lista
    : LBRACK (expr (COMMA expr)*)? RBRACK
    ;

tupla
    : LPAREN (expr (COMMA (expr)*)?)? RPAREN
    ;

set_dados
    : LBRACE expr (COMMA expr)* RBRACE
    ;

dicionario
    : LBRACE (elemento_dict (COMMA elemento_dict)*)? RBRACE
    ;

elemento_dict
    : expr COLON expr
    ;

// Expressões lógicas / Queries
query : (TRUE | FALSE)                                                             # valoresBooleanos
      | LPAREN query RPAREN                                                        # queryEntreParenteses
      | NOT query                                                                  # operacoesBooleanasEntreQuerys
      | query AND query                                                            # operacoesBooleanasEntreQuerys
      | query OR query                                                             # operacoesBooleanasEntreQuerys
      | expr (EQ_EQUAL | NOT_EQUAL | GREATER | LESS | GREATER_EQUAL | LESS_EQUAL) expr # relacoesEntreExpressoes
      ;