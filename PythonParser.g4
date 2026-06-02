parser grammar PythonParser;
options { tokenVocab=PythonLexer; }

// Regra inicial atualizada para a Fase 5
code : (stat | condicional)* EOF ; 

// Uma instrução simples (Fase 4)
stat : (expr | query | atribuicao) NEWLINE? ;

atribuicao: ID '=' expr;

// Nova Regra: Condicionais (Fase 5)
condicional
    : IF query COLON NEWLINE bloco (ELIF query COLON NEWLINE bloco)* (ELSE COLON NEWLINE bloco)? # estruturaCondicional
    ;

// Regra auxiliar para definir o conteúdo dentro de um IF, ELIF ou ELSE
bloco
    : (stat | condicional)+
    ;

// Expressões aritméticas (Fase 3)
expr : LPAREN expr RPAREN                                                         # expressoesEntreParenteses
     | expr (MULTIPLY | DIVISION | DOUBLE_SLASH | MODULUS) expr                  # operacoesComExpressoes
     | expr (PLUS | MINUS) expr                                                   # operacoesComExpressoes
     | ID                                                                         # ids
     | DIGIT                                                                      # numeros
     ;

// Expressões lógicas / Queries (Fase 4)
query : (TRUE | FALSE)                                                            # valoresBooleanos
      | LPAREN query RPAREN                                                       # queryEntreParenteses
      | NOT query                                                                 # operacoesBooleanasEntreQuerys
      | query AND query                                                           # operacoesBooleanasEntreQuerys
      | query OR query                                                            # operacoesBooleanasEntreQuerys
      | expr (EQ_EQUAL | NOT_EQUAL | GREATER | LESS | GREATER_EQUAL | LESS_EQUAL) expr # relacoesEntreExpressoes
      ;