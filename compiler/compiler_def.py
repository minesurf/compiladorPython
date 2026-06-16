if "." in __name__:
    from .PythonParser import PythonParser
    from .PythonParserVisitor import PythonParserVisitor
else:
    from PythonParser import PythonParser
    from PythonParserVisitor import PythonParserVisitor



class Compiler(PythonParserVisitor):



    def __init__(self):
        super(Compiler, self).__init__()
        self.vars = {}
        return None
    
    # Paste here all methods in PythonParserVisitor.py file

    # Visit a parse tree produced by PythonParser#code.
    
    def visitCode(self, ctx:PythonParser.CodeContext):
        print(('Here', ctx.getText(), type(ctx))) ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#stat.
    def visitStat(self, ctx:PythonParser.StatContext):
        print(('Here', ctx.getText(), type(ctx))) ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#atribuicao.
    def visitAtribuicao(self, ctx:PythonParser.AtribuicaoContext):
        print(('Here', ctx.getText(), type(ctx))) ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#estruturaWhile.
    def visitEstruturaWhile(self, ctx:PythonParser.EstruturaWhileContext):
        print(('Here', ctx.getText(), type(ctx))) ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#estruturaFor.
    def visitEstruturaFor(self, ctx:PythonParser.EstruturaForContext):
        print(('Here', ctx.getText(), type(ctx))) ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#definicaoFuncao.
    def visitDefinicaoFuncao(self, ctx:PythonParser.DefinicaoFuncaoContext):
        print(('Here', ctx.getText(), type(ctx))) ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#chamadaFuncao.
    def visitChamadaFuncao(self, ctx:PythonParser.ChamadaFuncaoContext):
        print(('Here', ctx.getText(), type(ctx))) ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#estruturaCondicional.
    def visitEstruturaCondicional(self, ctx:PythonParser.EstruturaCondicionalContext):
        print(('Here', ctx.getText(), type(ctx))) ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#bloco.
    def visitBloco(self, ctx:PythonParser.BlocoContext):
        print(('Here', ctx.getText(), type(ctx))) ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expressoesEntreParenteses.
    def visitExpressoesEntreParenteses(self, ctx:PythonParser.ExpressoesEntreParentesesContext):
        print(('Here', ctx.getText(), type(ctx))) ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#stringsEmExpressao.
    def visitStringsEmExpressao(self, ctx:PythonParser.StringsEmExpressaoContext):
        print(('Here', ctx.getText(), type(ctx))) ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#floats.
    def visitFloats(self, ctx:PythonParser.FloatsContext):
        print(('Here', ctx.getText(), type(ctx))) ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#operacoesComExpressoes.
    def visitOperacoesComExpressoes(self, ctx:PythonParser.OperacoesComExpressoesContext):
        print(('Here', ctx.getText(), type(ctx))) ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#booleanosEmExpressaoFalse.
    def visitBooleanosEmExpressaoFalse(self, ctx:PythonParser.BooleanosEmExpressaoFalseContext):
        print(('Here', ctx.getText(), type(ctx))) ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#idsPrint.
    def visitIdsPrint(self, ctx:PythonParser.IdsPrintContext):
        print(('Here', ctx.getText(), type(ctx))) ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#numeros.
    def visitNumeros(self, ctx:PythonParser.NumerosContext):
        print(('Here', ctx.getText(), type(ctx))) ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#booleanosEmExpressaoTrue.
    def visitBooleanosEmExpressaoTrue(self, ctx:PythonParser.BooleanosEmExpressaoTrueContext):
        print(('Here', ctx.getText(), type(ctx))) ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#chamadaFuncaoComoExpressao.
    def visitChamadaFuncaoComoExpressao(self, ctx:PythonParser.ChamadaFuncaoComoExpressaoContext):
        print(('Here', ctx.getText(), type(ctx))) ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#setEmExpressao.
    def visitSetEmExpressao(self, ctx:PythonParser.SetEmExpressaoContext):
        print(('Here', ctx.getText(), type(ctx))) ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#ids.
    def visitIds(self, ctx:PythonParser.IdsContext):
        print(('Here', ctx.getText(), type(ctx))) ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#listaEmExpressao.
    def visitListaEmExpressao(self, ctx:PythonParser.ListaEmExpressaoContext):
        print(('Here', ctx.getText(), type(ctx))) ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#tuplaEmExpressao.
    def visitTuplaEmExpressao(self, ctx:PythonParser.TuplaEmExpressaoContext):
        print(('Here', ctx.getText(), type(ctx))) ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#dicionarioEmExpressao.
    def visitDicionarioEmExpressao(self, ctx:PythonParser.DicionarioEmExpressaoContext):
        print(('Here', ctx.getText(), type(ctx))) ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#lista.
    def visitLista(self, ctx:PythonParser.ListaContext):
        print(('Here', ctx.getText(), type(ctx))) ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#tupla.
    def visitTupla(self, ctx:PythonParser.TuplaContext):
        print(('Here', ctx.getText(), type(ctx))) ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#set_dados.
    def visitSet_dados(self, ctx:PythonParser.Set_dadosContext):
        print(('Here', ctx.getText(), type(ctx))) ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#dicionario.
    def visitDicionario(self, ctx:PythonParser.DicionarioContext):
        print(('Here', ctx.getText(), type(ctx))) ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#elemento_dict.
    def visitElemento_dict(self, ctx:PythonParser.Elemento_dictContext):
        print(('Here', ctx.getText(), type(ctx))) ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#queryEntreParenteses.
    def visitQueryEntreParenteses(self, ctx:PythonParser.QueryEntreParentesesContext):
        print(('Here', ctx.getText(), type(ctx))) ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#operacoesBooleanasEntreQuerys.
    def visitOperacoesBooleanasEntreQuerys(self, ctx:PythonParser.OperacoesBooleanasEntreQuerysContext):
        print(('Here', ctx.getText(), type(ctx))) ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#relacoesEntreExpressoes.
    def visitRelacoesEntreExpressoes(self, ctx:PythonParser.RelacoesEntreExpressoesContext):
        print(('Here', ctx.getText(), type(ctx))) ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#valoresBooleanos.
    def visitValoresBooleanos(self, ctx:PythonParser.ValoresBooleanosContext):
        print(('Here', ctx.getText(), type(ctx))) ;
        return self.visitChildren(ctx)


del (PythonParser, PythonParserVisitor)
