# Generated from PythonParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PythonParser import PythonParser
else:
    from PythonParser import PythonParser

# This class defines a complete generic visitor for a parse tree produced by PythonParser.

class PythonParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PythonParser#code.
    def visitCode(self, ctx:PythonParser.CodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#stat.
    def visitStat(self, ctx:PythonParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#atribuicao.
    def visitAtribuicao(self, ctx:PythonParser.AtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#returnStmt.
    def visitReturnStmt(self, ctx:PythonParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#estruturaWhile.
    def visitEstruturaWhile(self, ctx:PythonParser.EstruturaWhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#estruturaFor.
    def visitEstruturaFor(self, ctx:PythonParser.EstruturaForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#definicaoFuncao.
    def visitDefinicaoFuncao(self, ctx:PythonParser.DefinicaoFuncaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#chamadaFuncao.
    def visitChamadaFuncao(self, ctx:PythonParser.ChamadaFuncaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#estruturaCondicional.
    def visitEstruturaCondicional(self, ctx:PythonParser.EstruturaCondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#bloco.
    def visitBloco(self, ctx:PythonParser.BlocoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expressoesEntreParenteses.
    def visitExpressoesEntreParenteses(self, ctx:PythonParser.ExpressoesEntreParentesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#stringsEmExpressao.
    def visitStringsEmExpressao(self, ctx:PythonParser.StringsEmExpressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#floats.
    def visitFloats(self, ctx:PythonParser.FloatsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#operacoesComExpressoes.
    def visitOperacoesComExpressoes(self, ctx:PythonParser.OperacoesComExpressoesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#booleanosEmExpressaoFalse.
    def visitBooleanosEmExpressaoFalse(self, ctx:PythonParser.BooleanosEmExpressaoFalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#idsPrint.
    def visitIdsPrint(self, ctx:PythonParser.IdsPrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#numeros.
    def visitNumeros(self, ctx:PythonParser.NumerosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#booleanosEmExpressaoTrue.
    def visitBooleanosEmExpressaoTrue(self, ctx:PythonParser.BooleanosEmExpressaoTrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#chamadaFuncaoComoExpressao.
    def visitChamadaFuncaoComoExpressao(self, ctx:PythonParser.ChamadaFuncaoComoExpressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#setEmExpressao.
    def visitSetEmExpressao(self, ctx:PythonParser.SetEmExpressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#ids.
    def visitIds(self, ctx:PythonParser.IdsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#listaEmExpressao.
    def visitListaEmExpressao(self, ctx:PythonParser.ListaEmExpressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#tuplaEmExpressao.
    def visitTuplaEmExpressao(self, ctx:PythonParser.TuplaEmExpressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#dicionarioEmExpressao.
    def visitDicionarioEmExpressao(self, ctx:PythonParser.DicionarioEmExpressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#lista.
    def visitLista(self, ctx:PythonParser.ListaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#tupla.
    def visitTupla(self, ctx:PythonParser.TuplaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#set_dados.
    def visitSet_dados(self, ctx:PythonParser.Set_dadosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#dicionario.
    def visitDicionario(self, ctx:PythonParser.DicionarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#elemento_dict.
    def visitElemento_dict(self, ctx:PythonParser.Elemento_dictContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#queryEntreParenteses.
    def visitQueryEntreParenteses(self, ctx:PythonParser.QueryEntreParentesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#operacoesBooleanasEntreQuerys.
    def visitOperacoesBooleanasEntreQuerys(self, ctx:PythonParser.OperacoesBooleanasEntreQuerysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#relacoesEntreExpressoes.
    def visitRelacoesEntreExpressoes(self, ctx:PythonParser.RelacoesEntreExpressoesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#valoresBooleanos.
    def visitValoresBooleanos(self, ctx:PythonParser.ValoresBooleanosContext):
        return self.visitChildren(ctx)



del PythonParser