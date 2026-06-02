parser grammar PythonParser;
options { tokenVocab=PythonLexer; }

// Regra inicial atualizada para aceitar quebras de linha soltas/extras entre comandos
code : (stat | condicional | func | func_call | NEWLINE)* EOF ; 

// Uma instrução simples (o NEWLINE agora é obrigatório no fim de um stat para separar comandos)
stat : (expr | query | atribuicao) NEWLINE ;

atribuicao : ID '=' expr ;

// Definição de Funções
func 
    : DEF ID LPAREN (ID (COMMA ID)*)? RPAREN COLON NEWLINE bloco # definicaoFuncao
    ;

// Chamada de Funções
func_call 
    : ID LPAREN (expr (COMMA expr)*)? RPAREN # chamadaFuncao
    ;

// Condicionais
condicional
    : IF query COLON NEWLINE bloco (ELIF query COLON NEWLINE bloco)* (ELSE COLON NEWLINE bloco)? # estruturaCondicional
    ;

// Bloco aceita instruções, condicionais, funções e também ignora linhas em branco extras
bloco
    : (stat | condicional | func | func_call | NEWLINE)+
    ;

// Expressões aritméticas e gerais (Corrigido: adicionado TRUE, FALSE e func_call)
expr : LPAREN expr RPAREN                                                         # expressoesEntreParenteses
     | expr (MULTIPLY | DIVISION | DOUBLE_SLASH | MODULUS) expr                  # operacoesComExpressoes
     | expr (PLUS | MINUS) expr                                                   # operacoesComExpressoes
     | TRUE                                                                      # booleanosEmExpressao
     | FALSE                                                                     # booleanosEmExpressao
     | func_call                                                                 # chamadaFuncaoComoExpressao
     | ID                                                                        # ids
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