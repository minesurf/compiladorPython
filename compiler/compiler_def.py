from antlr4 import TerminalNode
if "." in __name__:
    from .PythonParser import PythonParser
    from .PythonParserVisitor import PythonParserVisitor
else:
    from PythonParser import PythonParser
    from PythonParserVisitor import PythonParserVisitor

# Excepção customizada para propagar o valor de retorno e interromper a execução do bloco
class ReturnException(Exception):
    def __init__(self, value):
        self.value = value



class Compiler(PythonParserVisitor):



    def __init__(self):
        super(Compiler, self).__init__()
        self.vars = {}
        self.funcs = {}
        self.depth = 0  # Rastreador de profundidade para depuração
        return None

    def visit(self, tree):
        """Override do método visit para rastrear a árvore e detectar loops."""
        if not tree:
            return None
        
        # Debug opcional: descomente a linha abaixo para ver a árvore sendo percorrida
        # print("  " * self.depth + f"-> Visitando: {tree.__class__.__name__}")
        
        self.depth += 1
        result = super().visit(tree)
        self.depth -= 1
        return result

    # Visit a parse tree produced by PythonParser#code.
    
    def visitCode(self, ctx:PythonParser.CodeContext):
        result = None
        # Percorre explicitamente cada instrução no nível raiz
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            # Evita visitar o token EOF ou NEWLINEs soltos diretamente
            if not isinstance(child, TerminalNode):
                result = self.visit(child)
        return result


    # Visit a parse tree produced by PythonParser#stat.
    def visitStat(self, ctx:PythonParser.StatContext):
        # stat : (expr | query | atribuicao | returnStmt) NEWLINE?
        # Visitamos apenas o primeiro filho, que contém a lógica real
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by PythonParser#atribuicao.
    def visitAtribuicao(self, ctx:PythonParser.AtribuicaoContext):
        # Usamos o primeiro filho para o nome e visitamos o nó da expressão para o valor
        variable_name = ctx.getChild(0).getText()
        
        # 2. Avaliar a expressão do lado direito
        # Chamamos self.visit() no nó da expressão para obter o seu valor calculado
        value = self.visit(ctx.expr())
        
        # 3. Guardar o resultado em self.vars
        # Se a chave já existir, o Python sobrescreve o valor automaticamente.
        self.vars[variable_name] = value
        return value


    # Visit a parse tree produced by PythonParser#estruturaWhile.
    def visitEstruturaWhile(self, ctx:PythonParser.EstruturaWhileContext):
        # O loop 'while' do Python executa a lógica de reavaliação nativamente.
        # ctx.query() acede ao nó da condição.
        # ctx.bloco() acede ao nó com as instruções internas.
        
        # Avaliamos a condição (query) a cada iteração
        while self.visit(ctx.query()):
            # Executamos o corpo do loop
            self.visit(ctx.bloco())
            
        return None


    # Visit a parse tree produced by PythonParser#estruturaFor.
    def visitEstruturaFor(self, ctx:PythonParser.EstruturaForContext):
        # 1. Identificar o nome da variável de iteração (o token ID)
        var_name = ctx.ID().getText()

        # 2. Avaliar o iterável (pode ser um range(...) ou uma expressão genérica como lista/tupla)
        if ctx.RANGE():
            start = 0
            if ctx.COMMA():
                # Caso range(start, stop)
                start = int(self.visit(ctx.expr(0)))
                stop = int(self.visit(ctx.expr(1)))
            else:
                # Caso range(stop)
                stop = int(self.visit(ctx.expr(0)))
            iterable = range(start, stop)
        else:
            iterable = self.visit(ctx.expr(0))

        # 3. Iterar sobre a sequência, atribuir o valor e executar o corpo
        for val in iterable:
            self.vars[var_name] = val
            self.visit(ctx.bloco())
            
        return None


    # Visit a parse tree produced by PythonParser#definicaoFuncao.
    def visitDefinicaoFuncao(self, ctx:PythonParser.DefinicaoFuncaoContext):
        # 1. Obter o nome da função (ID na posição 0)
        func_name = ctx.ID(0).getText()
        # 2. Obter a lista de parâmetros (IDs da posição 1 em diante)
        params = [id_node.getText() for id_node in ctx.ID()[1:]]
        # 3. Guardar a definição (corpo e parâmetros) sem executar
        self.funcs[func_name] = {'params': params, 'body': ctx.bloco()}
        return None


    # Visit a parse tree produced by PythonParser#chamadaFuncao.
    def visitChamadaFuncao(self, ctx:PythonParser.ChamadaFuncaoContext):
        name = ctx.getChild(0).getText()
        # Avaliar os argumentos passados na chamada
        args = [self.visit(e) for e in ctx.expr()]

        if name in self.funcs:
            func = self.funcs[name]
            
            # Validação de Segurança: Verificar se o número de argumentos coincide com os parâmetros
            if len(args) != len(func['params']):
                raise TypeError(f"Erro em tempo de execução: A função '{name}' espera {len(func['params'])} argumento(s), mas recebeu {len(args)}.")

            # --- Gestão de Escopo ---
            # Guardamos as variáveis globais atuais
            old_vars = self.vars.copy()
            
            # Criamos o ambiente local associando parâmetros aos argumentos
            local_scope = dict(zip(func['params'], args))
            self.vars.update(local_scope)
            
            # Executamos o corpo da função
            result = None
            try:
                self.visit(func['body'])
            except ReturnException as r:
                result = r.value
            
            # Restauramos o âmbito global original
            self.vars = old_vars
            return result

        # Suporte para Built-ins do Python (print, range, len, etc.)
        builtin = __builtins__.get(name) if isinstance(__builtins__, dict) else getattr(__builtins__, name, None)
        if builtin and callable(builtin):
            return builtin(*args)

        raise NameError(f"Nome '{name}' não definido")

    # Visit a parse tree produced by PythonParser#returnStmt.
    def visitReturnStmt(self, ctx:PythonParser.ReturnStmtContext):
        # Avalia a expressão que acompanha o return
        value = self.visit(ctx.expr())
        # Lança a excepção para interromper o visitBloco e devolver o valor
        raise ReturnException(value)


    # Visit a parse tree produced by PythonParser#estruturaCondicional.
    def visitEstruturaCondicional(self, ctx:PythonParser.EstruturaCondicionalContext):
        # 1. Avaliar a condição do 'if' (sempre no índice 0 de query)
        if self.visit(ctx.query(0)):
            # Se verdadeiro, visita apenas o bloco correspondente e ignora o resto
            return self.visit(ctx.bloco(0))
        
        # 2. Avaliar blocos 'elif' (se existirem)
        # ctx.ELIF() retorna uma lista de tokens. O número de elifs define as iterações.
        num_elifs = len(ctx.ELIF())
        for i in range(num_elifs):
            # As condições elif começam no índice 1 da lista de query()
            if self.visit(ctx.query(i + 1)):
                # O bloco correspondente também está deslocado em 1
                return self.visit(ctx.bloco(i + 1))
        
        # 3. Avaliar o bloco 'else' (se existir)
        # O método ctx.ELSE() retorna o token se ele estiver presente na árvore
        if ctx.ELSE():
            # O bloco do 'else' é garantidamente o último da lista ctx.bloco()
            indice_else = len(ctx.bloco()) - 1
            return self.visit(ctx.bloco(indice_else))
        
        return None


    # Visit a parse tree produced by PythonParser#bloco.
    def visitBloco(self, ctx:PythonParser.BlocoContext):
        last_result = None
        # Um bloco é uma sequência de comandos. Visitamos um por um.
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if not isinstance(child, TerminalNode):
                last_result = self.visit(child)
        return last_result


    # Visit a parse tree produced by PythonParser#expressoesEntreParenteses.
    def visitExpressoesEntreParenteses(self, ctx:PythonParser.ExpressoesEntreParentesesContext):
        # O filho 0 é '(', o 1 é 'expr', o 2 é ')'
        return self.visit(ctx.expr())


    # Visit a parse tree produced by PythonParser#stringsEmExpressao.
    def visitStringsEmExpressao(self, ctx:PythonParser.StringsEmExpressaoContext):
        return ctx.STRING().getText().strip('"').strip("'")


    # Visit a parse tree produced by PythonParser#floats.
    def visitFloats(self, ctx:PythonParser.FloatsContext):
        return float(ctx.getText())


    # Visit a parse tree produced by PythonParser#operacoesComExpressoes.
    def visitOperacoesComExpressoes(self, ctx:PythonParser.OperacoesComExpressoesContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        
        if ctx.PLUS(): return left + right
        if ctx.MINUS(): return left - right
        if ctx.MULTIPLY(): return left * right
        if ctx.DIVISION(): 
            if right == 0:
                raise ZeroDivisionError("Erro: Divisão por zero detectada.")
            return left / right
        if ctx.DOUBLE_SLASH(): return left // right
        if ctx.MODULUS(): return left % right
        if ctx.DOUBLE_STAR(): return left ** right
        return 0


    # Visit a parse tree produced by PythonParser#booleanosEmExpressaoFalse.
    def visitBooleanosEmExpressaoFalse(self, ctx:PythonParser.BooleanosEmExpressaoFalseContext):
        return False


    # Visit a parse tree produced by PythonParser#idsPrint.
    def visitIdsPrint(self, ctx:PythonParser.IdsPrintContext):
        # Trata 'print' como um identificador, buscando seu valor se existir
        return self.vars.get('print', 0)


    # Visit a parse tree produced by PythonParser#numeros.
    def visitNumeros(self, ctx:PythonParser.NumerosContext):
        return int(ctx.getText())


    # Visit a parse tree produced by PythonParser#booleanosEmExpressaoTrue.
    def visitBooleanosEmExpressaoTrue(self, ctx:PythonParser.BooleanosEmExpressaoTrueContext):
        return True


    # Visit a parse tree produced by PythonParser#chamadaFuncaoComoExpressao.
    def visitChamadaFuncaoComoExpressao(self, ctx:PythonParser.ChamadaFuncaoComoExpressaoContext):
        return self.visit(ctx.func_call())


    # Visit a parse tree produced by PythonParser#setEmExpressao.
    def visitSetEmExpressao(self, ctx:PythonParser.SetEmExpressaoContext):
        return self.visit(ctx.set_dados())


    # Visit a parse tree produced by PythonParser#ids.
    def visitIds(self, ctx:PythonParser.IdsContext):
        name = ctx.ID().getText()
        if name in self.vars:
            return self.vars[name]
        
        line = ctx.start.line
        column = ctx.start.column
        raise NameError(f"Erro na linha {line}, coluna {column}: Variável '{name}' não definida. Verifique se a atribuição foi realizada antes do uso.")


    # Visit a parse tree produced by PythonParser#listaEmExpressao.
    def visitListaEmExpressao(self, ctx:PythonParser.ListaEmExpressaoContext):
        return self.visit(ctx.lista())


    # Visit a parse tree produced by PythonParser#tuplaEmExpressao.
    def visitTuplaEmExpressao(self, ctx:PythonParser.TuplaEmExpressaoContext):
        return self.visit(ctx.tupla())


    # Visit a parse tree produced by PythonParser#dicionarioEmExpressao.
    def visitDicionarioEmExpressao(self, ctx:PythonParser.DicionarioEmExpressaoContext):
        return self.visit(ctx.dicionario())


    # Visit a parse tree produced by PythonParser#lista.
    def visitLista(self, ctx:PythonParser.ListaContext):
        return [self.visit(e) for e in ctx.expr()]


    # Visit a parse tree produced by PythonParser#tupla.
    def visitTupla(self, ctx:PythonParser.TuplaContext):
        return tuple([self.visit(e) for e in ctx.expr()])


    # Visit a parse tree produced by PythonParser#set_dados.
    def visitSet_dados(self, ctx:PythonParser.Set_dadosContext):
        return {self.visit(e) for e in ctx.expr()}


    # Visit a parse tree produced by PythonParser#dicionario.
    def visitDicionario(self, ctx:PythonParser.DicionarioContext):
        res = {}
        for elem in ctx.elemento_dict():
            key, val = self.visit(elem)
            res[key] = val
        return res


    # Visit a parse tree produced by PythonParser#elemento_dict.
    def visitElemento_dict(self, ctx:PythonParser.Elemento_dictContext):
        return self.visit(ctx.expr(0)), self.visit(ctx.expr(1))


    # Visit a parse tree produced by PythonParser#queryEntreParenteses.
    def visitQueryEntreParenteses(self, ctx:PythonParser.QueryEntreParentesesContext):
        return self.visit(ctx.query())


    # Visit a parse tree produced by PythonParser#operacoesBooleanasEntreQuerys.
    def visitOperacoesBooleanasEntreQuerys(self, ctx:PythonParser.OperacoesBooleanasEntreQuerysContext):
        if ctx.NOT():
            return not self.visit(ctx.query(0))
        left = self.visit(ctx.query(0))
        right = self.visit(ctx.query(1))
        if ctx.AND(): return left and right
        if ctx.OR(): return left or right
        return False


    # Visit a parse tree produced by PythonParser#relacoesEntreExpressoes.
    def visitRelacoesEntreExpressoes(self, ctx:PythonParser.RelacoesEntreExpressoesContext):
        v1 = self.visit(ctx.expr(0))
        v2 = self.visit(ctx.expr(1))
        if ctx.EQ_EQUAL(): return v1 == v2
        if ctx.NOT_EQUAL(): return v1 != v2
        if ctx.GREATER(): return v1 > v2
        if ctx.LESS(): return v1 < v2
        if ctx.GREATER_EQUAL(): return v1 >= v2
        if ctx.LESS_EQUAL(): return v1 <= v2
        return False


    # Visit a parse tree produced by PythonParser#valoresBooleanos.
    def visitValoresBooleanos(self, ctx:PythonParser.ValoresBooleanosContext):
        if ctx.TRUE(): return True
        return False


del (PythonParser, PythonParserVisitor)
