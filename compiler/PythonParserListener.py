# Generated from PythonParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PythonParser import PythonParser
else:
    from PythonParser import PythonParser

# This class defines a complete listener for a parse tree produced by PythonParser.
class PythonParserListener(ParseTreeListener):

    # Enter a parse tree produced by PythonParser#code.
    def enterCode(self, ctx:PythonParser.CodeContext):
        pass

    # Exit a parse tree produced by PythonParser#code.
    def exitCode(self, ctx:PythonParser.CodeContext):
        pass


    # Enter a parse tree produced by PythonParser#stat.
    def enterStat(self, ctx:PythonParser.StatContext):
        pass

    # Exit a parse tree produced by PythonParser#stat.
    def exitStat(self, ctx:PythonParser.StatContext):
        pass


    # Enter a parse tree produced by PythonParser#atribuicao.
    def enterAtribuicao(self, ctx:PythonParser.AtribuicaoContext):
        pass

    # Exit a parse tree produced by PythonParser#atribuicao.
    def exitAtribuicao(self, ctx:PythonParser.AtribuicaoContext):
        pass


    # Enter a parse tree produced by PythonParser#returnStmt.
    def enterReturnStmt(self, ctx:PythonParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by PythonParser#returnStmt.
    def exitReturnStmt(self, ctx:PythonParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by PythonParser#estruturaWhile.
    def enterEstruturaWhile(self, ctx:PythonParser.EstruturaWhileContext):
        pass

    # Exit a parse tree produced by PythonParser#estruturaWhile.
    def exitEstruturaWhile(self, ctx:PythonParser.EstruturaWhileContext):
        pass


    # Enter a parse tree produced by PythonParser#estruturaFor.
    def enterEstruturaFor(self, ctx:PythonParser.EstruturaForContext):
        pass

    # Exit a parse tree produced by PythonParser#estruturaFor.
    def exitEstruturaFor(self, ctx:PythonParser.EstruturaForContext):
        pass


    # Enter a parse tree produced by PythonParser#definicaoFuncao.
    def enterDefinicaoFuncao(self, ctx:PythonParser.DefinicaoFuncaoContext):
        pass

    # Exit a parse tree produced by PythonParser#definicaoFuncao.
    def exitDefinicaoFuncao(self, ctx:PythonParser.DefinicaoFuncaoContext):
        pass


    # Enter a parse tree produced by PythonParser#chamadaFuncao.
    def enterChamadaFuncao(self, ctx:PythonParser.ChamadaFuncaoContext):
        pass

    # Exit a parse tree produced by PythonParser#chamadaFuncao.
    def exitChamadaFuncao(self, ctx:PythonParser.ChamadaFuncaoContext):
        pass


    # Enter a parse tree produced by PythonParser#estruturaCondicional.
    def enterEstruturaCondicional(self, ctx:PythonParser.EstruturaCondicionalContext):
        pass

    # Exit a parse tree produced by PythonParser#estruturaCondicional.
    def exitEstruturaCondicional(self, ctx:PythonParser.EstruturaCondicionalContext):
        pass


    # Enter a parse tree produced by PythonParser#bloco.
    def enterBloco(self, ctx:PythonParser.BlocoContext):
        pass

    # Exit a parse tree produced by PythonParser#bloco.
    def exitBloco(self, ctx:PythonParser.BlocoContext):
        pass


    # Enter a parse tree produced by PythonParser#expressoesEntreParenteses.
    def enterExpressoesEntreParenteses(self, ctx:PythonParser.ExpressoesEntreParentesesContext):
        pass

    # Exit a parse tree produced by PythonParser#expressoesEntreParenteses.
    def exitExpressoesEntreParenteses(self, ctx:PythonParser.ExpressoesEntreParentesesContext):
        pass


    # Enter a parse tree produced by PythonParser#stringsEmExpressao.
    def enterStringsEmExpressao(self, ctx:PythonParser.StringsEmExpressaoContext):
        pass

    # Exit a parse tree produced by PythonParser#stringsEmExpressao.
    def exitStringsEmExpressao(self, ctx:PythonParser.StringsEmExpressaoContext):
        pass


    # Enter a parse tree produced by PythonParser#floats.
    def enterFloats(self, ctx:PythonParser.FloatsContext):
        pass

    # Exit a parse tree produced by PythonParser#floats.
    def exitFloats(self, ctx:PythonParser.FloatsContext):
        pass


    # Enter a parse tree produced by PythonParser#operacoesComExpressoes.
    def enterOperacoesComExpressoes(self, ctx:PythonParser.OperacoesComExpressoesContext):
        pass

    # Exit a parse tree produced by PythonParser#operacoesComExpressoes.
    def exitOperacoesComExpressoes(self, ctx:PythonParser.OperacoesComExpressoesContext):
        pass


    # Enter a parse tree produced by PythonParser#booleanosEmExpressaoFalse.
    def enterBooleanosEmExpressaoFalse(self, ctx:PythonParser.BooleanosEmExpressaoFalseContext):
        pass

    # Exit a parse tree produced by PythonParser#booleanosEmExpressaoFalse.
    def exitBooleanosEmExpressaoFalse(self, ctx:PythonParser.BooleanosEmExpressaoFalseContext):
        pass


    # Enter a parse tree produced by PythonParser#idsPrint.
    def enterIdsPrint(self, ctx:PythonParser.IdsPrintContext):
        pass

    # Exit a parse tree produced by PythonParser#idsPrint.
    def exitIdsPrint(self, ctx:PythonParser.IdsPrintContext):
        pass


    # Enter a parse tree produced by PythonParser#numeros.
    def enterNumeros(self, ctx:PythonParser.NumerosContext):
        pass

    # Exit a parse tree produced by PythonParser#numeros.
    def exitNumeros(self, ctx:PythonParser.NumerosContext):
        pass


    # Enter a parse tree produced by PythonParser#booleanosEmExpressaoTrue.
    def enterBooleanosEmExpressaoTrue(self, ctx:PythonParser.BooleanosEmExpressaoTrueContext):
        pass

    # Exit a parse tree produced by PythonParser#booleanosEmExpressaoTrue.
    def exitBooleanosEmExpressaoTrue(self, ctx:PythonParser.BooleanosEmExpressaoTrueContext):
        pass


    # Enter a parse tree produced by PythonParser#chamadaFuncaoComoExpressao.
    def enterChamadaFuncaoComoExpressao(self, ctx:PythonParser.ChamadaFuncaoComoExpressaoContext):
        pass

    # Exit a parse tree produced by PythonParser#chamadaFuncaoComoExpressao.
    def exitChamadaFuncaoComoExpressao(self, ctx:PythonParser.ChamadaFuncaoComoExpressaoContext):
        pass


    # Enter a parse tree produced by PythonParser#setEmExpressao.
    def enterSetEmExpressao(self, ctx:PythonParser.SetEmExpressaoContext):
        pass

    # Exit a parse tree produced by PythonParser#setEmExpressao.
    def exitSetEmExpressao(self, ctx:PythonParser.SetEmExpressaoContext):
        pass


    # Enter a parse tree produced by PythonParser#ids.
    def enterIds(self, ctx:PythonParser.IdsContext):
        pass

    # Exit a parse tree produced by PythonParser#ids.
    def exitIds(self, ctx:PythonParser.IdsContext):
        pass


    # Enter a parse tree produced by PythonParser#listaEmExpressao.
    def enterListaEmExpressao(self, ctx:PythonParser.ListaEmExpressaoContext):
        pass

    # Exit a parse tree produced by PythonParser#listaEmExpressao.
    def exitListaEmExpressao(self, ctx:PythonParser.ListaEmExpressaoContext):
        pass


    # Enter a parse tree produced by PythonParser#tuplaEmExpressao.
    def enterTuplaEmExpressao(self, ctx:PythonParser.TuplaEmExpressaoContext):
        pass

    # Exit a parse tree produced by PythonParser#tuplaEmExpressao.
    def exitTuplaEmExpressao(self, ctx:PythonParser.TuplaEmExpressaoContext):
        pass


    # Enter a parse tree produced by PythonParser#dicionarioEmExpressao.
    def enterDicionarioEmExpressao(self, ctx:PythonParser.DicionarioEmExpressaoContext):
        pass

    # Exit a parse tree produced by PythonParser#dicionarioEmExpressao.
    def exitDicionarioEmExpressao(self, ctx:PythonParser.DicionarioEmExpressaoContext):
        pass


    # Enter a parse tree produced by PythonParser#lista.
    def enterLista(self, ctx:PythonParser.ListaContext):
        pass

    # Exit a parse tree produced by PythonParser#lista.
    def exitLista(self, ctx:PythonParser.ListaContext):
        pass


    # Enter a parse tree produced by PythonParser#tupla.
    def enterTupla(self, ctx:PythonParser.TuplaContext):
        pass

    # Exit a parse tree produced by PythonParser#tupla.
    def exitTupla(self, ctx:PythonParser.TuplaContext):
        pass


    # Enter a parse tree produced by PythonParser#set_dados.
    def enterSet_dados(self, ctx:PythonParser.Set_dadosContext):
        pass

    # Exit a parse tree produced by PythonParser#set_dados.
    def exitSet_dados(self, ctx:PythonParser.Set_dadosContext):
        pass


    # Enter a parse tree produced by PythonParser#dicionario.
    def enterDicionario(self, ctx:PythonParser.DicionarioContext):
        pass

    # Exit a parse tree produced by PythonParser#dicionario.
    def exitDicionario(self, ctx:PythonParser.DicionarioContext):
        pass


    # Enter a parse tree produced by PythonParser#elemento_dict.
    def enterElemento_dict(self, ctx:PythonParser.Elemento_dictContext):
        pass

    # Exit a parse tree produced by PythonParser#elemento_dict.
    def exitElemento_dict(self, ctx:PythonParser.Elemento_dictContext):
        pass


    # Enter a parse tree produced by PythonParser#queryEntreParenteses.
    def enterQueryEntreParenteses(self, ctx:PythonParser.QueryEntreParentesesContext):
        pass

    # Exit a parse tree produced by PythonParser#queryEntreParenteses.
    def exitQueryEntreParenteses(self, ctx:PythonParser.QueryEntreParentesesContext):
        pass


    # Enter a parse tree produced by PythonParser#operacoesBooleanasEntreQuerys.
    def enterOperacoesBooleanasEntreQuerys(self, ctx:PythonParser.OperacoesBooleanasEntreQuerysContext):
        pass

    # Exit a parse tree produced by PythonParser#operacoesBooleanasEntreQuerys.
    def exitOperacoesBooleanasEntreQuerys(self, ctx:PythonParser.OperacoesBooleanasEntreQuerysContext):
        pass


    # Enter a parse tree produced by PythonParser#relacoesEntreExpressoes.
    def enterRelacoesEntreExpressoes(self, ctx:PythonParser.RelacoesEntreExpressoesContext):
        pass

    # Exit a parse tree produced by PythonParser#relacoesEntreExpressoes.
    def exitRelacoesEntreExpressoes(self, ctx:PythonParser.RelacoesEntreExpressoesContext):
        pass


    # Enter a parse tree produced by PythonParser#valoresBooleanos.
    def enterValoresBooleanos(self, ctx:PythonParser.ValoresBooleanosContext):
        pass

    # Exit a parse tree produced by PythonParser#valoresBooleanos.
    def exitValoresBooleanos(self, ctx:PythonParser.ValoresBooleanosContext):
        pass



del PythonParser