#Dinh Ba Khanh - 2252323
from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *
from functools import reduce

class ASTGeneration(MiniGoVisitor):
    """program: list_declare EOF;"""
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return Program(self.visit(ctx.list_declare()))


    """list_declare: declared list_declare | declared ;"""
    def visitList_declare(self, ctx:MiniGoParser.List_declareContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.declared())]
        return [self.visit(ctx.declared())] + self.visit(ctx.list_declare())

    """int_lit: DEC | BIN | OCT | HEX ;"""
    def visitInt_lit(self, ctx:MiniGoParser.Int_litContext):
        if ctx.DEC():
            return IntLiteral(ctx.DEC().getText())
        elif ctx.BIN():
            return IntLiteral(ctx.BIN().getText())
        elif ctx.HEX():
            return IntLiteral(ctx.HEX().getText())
        elif ctx.OCT():
            return IntLiteral(ctx.OCT().getText())

    """
    literal:
    int_lit
    | FLOAT_LIT
    | STR_LIT
    | TRUE
    | FALSE
    | NIL
    | array_literal
    | struct_literal;
    """
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        if ctx.int_lit():
            return self.visit(ctx.int_lit())
        elif ctx.FLOAT_LIT():
            return FloatLiteral(ctx.FLOAT_LIT().getText())
        elif ctx.STR_LIT():
            return StringLiteral(ctx.STR_LIT().getText())
        elif ctx.TRUE():
            return BooleanLiteral(ctx.TRUE().getText())
        elif ctx.FALSE():
            return BooleanLiteral(ctx.FALSE().getText())
        elif ctx.NIL():
            return NilLiteral()       #recheck here
        elif ctx.array_literal():
            return self.visit(ctx.array_literal())
        else:
            return self.visit(ctx.struct_literal())

    """array_literal: array_init array_type LCB list_array_index RCB;"""
    def visitArray_literal(self, ctx:MiniGoParser.Array_literalContext):
        dim = self.visit(ctx.array_init())
        typ = self.visit(ctx.array_type())
        val = self.visit(ctx.list_array_index())

        return ArrayLiteral(dim, typ, val)



    """array_type: INT | FLOAT | BOOLEAN | STRING | ID;"""
    def visitArray_type(self, ctx:MiniGoParser.Array_typeContext):
        if ctx.INT(): return IntType()
        elif ctx.FLOAT(): return FloatType()
        elif ctx.BOOLEAN(): return BoolType()
        elif ctx.STRING(): return StringType()
        elif ctx.ID(): return Id(ctx.ID().getText())


    """array_init: array_init LSB (int_lit | ID) RSB | LSB (int_lit | ID) RSB ;"""
    def visitArray_init(self, ctx:MiniGoParser.Array_initContext):
        if ctx.getChildCount() == 3:
            if ctx.int_lit():
                return [self.visit(ctx.int_lit())]
            else:
                return [Id(ctx.ID().getText())]

        if ctx.int_lit():  
            return self.visit(ctx.array_init()) + [self.visit(ctx.int_lit())]
        
        return self.visit(ctx.array_init()) + [Id(ctx.ID().getText())]
        

    """
    array_index:
    int_lit
    | FLOAT_LIT
    | STR_LIT
    | TRUE
    | FALSE
    | NIL
    | ID            //just add on H14/02 4:40pm
    | struct_literal
    | LCB list_array_index RCB;
    """
    def visitArray_index(self, ctx:MiniGoParser.Array_indexContext):
        if ctx.int_lit():
            return self.visit(ctx.int_lit())
        elif ctx.FLOAT_LIT():
            return FloatLiteral(ctx.FLOAT_LIT().getText())
        elif ctx.STR_LIT():
            return StringLiteral(ctx.STR_LIT().getText())
        elif ctx.TRUE():
            return BooleanLiteral(ctx.TRUE().getText())
        elif ctx.FALSE():
            return BooleanLiteral(ctx.FALSE().getText())
        elif ctx.NIL():
            return NilLiteral()
        elif ctx.struct_literal():
            return self.visit(ctx.struct_literal())
        else:
            return self.visit(ctx.list_array_index())

    """list_array_index: array_index COMMA list_array_index | array_index ;"""
    def visitList_array_index(self, ctx:MiniGoParser.List_array_indexContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.array_index())]
        return [self.visit(ctx.array_index())] + self.visit(ctx.list_array_index())

    """struct_literal: ID LCB list_element  RCB;"""
    def visitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        nam = ctx.ID().getText()
        lst = self.visit(ctx.list_element())

        return StructLiteral(nam, lst)


    """list_element: ID COLON expr COMMA list_element | ID COLON expr | ;"""
    def visitList_element(self, ctx:MiniGoParser.List_elementContext):
        if ctx.getChildCount() == 0:
            return []
        elif ctx.getChildCount() == 3:
            return [(ctx.ID().getText(), self.visit(ctx.expr()))]
        return [(ctx.ID().getText(), self.visit(ctx.expr()))] + self.visit(ctx.list_element())


    """list_expr: expr COMMA list_expr | expr ;"""
    def visitList_expr(self, ctx:MiniGoParser.List_exprContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.list_expr())

    """expr: expr OR expr1 | expr1;"""
    def visitExpr(self, ctx:MiniGoParser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr1())
        
        op = ctx.OR().getText()
        left = self.visit(ctx.expr())
        right = self.visit(ctx.expr1())

        return BinaryOp(op, left, right)


    """expr1: expr1 AND expr2 | expr2;"""
    def visitExpr1(self, ctx:MiniGoParser.Expr1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr2())
        
        op = ctx.AND().getText()
        left = self.visit(ctx.expr1())
        right = self.visit(ctx.expr2())

        return BinaryOp(op, left, right)

    """expr2: expr2 log_op expr3 | expr3;"""
    def visitExpr2(self, ctx:MiniGoParser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr3())
        
        op = self.visit(ctx.log_op())
        left = self.visit(ctx.expr2())
        right = self.visit(ctx.expr3())

        return BinaryOp(op, left, right)

    """expr3: expr3 add_op expr4 | expr4;"""
    def visitExpr3(self, ctx:MiniGoParser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr4())
        
        op = self.visit(ctx.add_op())
        left = self.visit(ctx.expr3())
        right = self.visit(ctx.expr4())

        return BinaryOp(op, left, right)

    """expr4: expr4 mul_op expr5 | expr5;"""
    def visitExpr4(self, ctx:MiniGoParser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr5())
        
        op = self.visit(ctx.mul_op())
        left = self.visit(ctx.expr4())
        right = self.visit(ctx.expr5())

        return BinaryOp(op, left, right)


    """expr5: una_op expr5 | expr6;"""
    def visitExpr5(self, ctx:MiniGoParser.Expr5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr6())
        
        op = self.visit(ctx.una_op())
        e = self.visit(ctx.expr5())

        return UnaryOp(op, e)


    """expr6: expr6 LSB expr RSB | expr6 DOT (ID | func_call) | expr7;"""
    def visitExpr6(self, ctx:MiniGoParser.Expr6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr7())
        elif ctx.getChildCount() == 4:
            rec_part = self.visit(ctx.expr6())
            if type(rec_part) == ArrayCell:
                return ArrayCell(rec_part.arr, rec_part.idx + [self.visit(ctx.expr())])
            return ArrayCell(self.visit(ctx.expr6()), [self.visit(ctx.expr())])
        elif ctx.ID():
            return FieldAccess(self.visit(ctx.expr6()), ctx.ID().getText())
        else:
            func_call = self.visit(ctx.func_call())
            
            return MethCall(self.visit(ctx.expr6()), func_call.funName, func_call.args)


    """expr7: literal | ID | LRB expr RRB | func_call ;"""
    def visitExpr7(self, ctx:MiniGoParser.Expr7Context):
        if ctx.literal(): return self.visit(ctx.literal())
        elif ctx.ID(): return Id(ctx.ID().getText())
        elif ctx.expr(): return self.visit(ctx.expr())

        return self.visit(ctx.func_call())



    """log_op: (EQUAL | NOT_EQUAL | LT | LTE | GT | GTE) ;"""
    def visitLog_op(self, ctx: MiniGoParser.Log_opContext):
        if ctx.EQUAL(): return ctx.EQUAL().getText()
        elif ctx.NOT_EQUAL(): return ctx.NOT_EQUAL().getText()
        elif ctx.LT(): return ctx.LT().getText()
        elif ctx.LTE(): return ctx.LTE().getText()
        elif ctx.GT(): return ctx.GT().getText()
        elif ctx.GTE(): return ctx.GTE().getText()

    """add_op: (ADD | SUB);"""
    def visitAdd_op(self, ctx: MiniGoParser.Add_opContext):
        if ctx.ADD(): return ctx.ADD().getText()
        elif ctx.SUB(): return ctx.SUB().getText()


    """mul_op: (MUL | DIV | MOD);"""
    def visitMul_op(self, ctx: MiniGoParser.Mul_opContext):
        if ctx.MUL(): return ctx.MUL().getText()
        elif ctx.DIV(): return ctx.DIV().getText()
        elif ctx.MOD(): return ctx.MOD().getText()

    """una_op: (SUB | NOT | ADD);"""
    def visitUna_op(self, ctx: MiniGoParser.Una_opContext):
        if ctx.ADD(): return ctx.ADD().getText()
        elif ctx.SUB(): return ctx.SUB().getText()
        elif ctx.NOT(): return ctx.NOT().getText()

    """parameter: expr COMMA parameter | expr;"""
    def visitParameter(self, ctx:MiniGoParser.ParameterContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.parameter())


    """func_call: ID LRB parameter? RRB;"""
    def visitFunc_call(self, ctx:MiniGoParser.Func_callContext):
        name = ctx.ID().getText()
        param = []
        if ctx.parameter():
            param = self.visit(ctx.parameter())
        return FuncCall(name, param)



    """
    declared:
    var_declared
    | const_declared
    | func_declared
    | method_declared
    | struct_declared
    | interface_declared;
    """
    def visitDeclared(self, ctx:MiniGoParser.DeclaredContext):
        return self.visitChildren(ctx)


    """dec_type: array_init? INT | array_init? FLOAT | array_init? BOOLEAN | array_init? STRING | array_init? ID;"""
    def visitDec_type(self, ctx:MiniGoParser.Dec_typeContext):
        if ctx.array_init():
            arr_part = self.visit(ctx.array_init())
            if ctx.INT():
                Typ = IntType()
                return ArrayType(arr_part, Typ)
            elif ctx.FLOAT():
                Typ = FloatType()
                return ArrayType(arr_part, Typ)
            elif ctx.BOOLEAN():
                Typ = BoolType()
                return ArrayType(arr_part, Typ)
            elif ctx.STRING():
                Typ = StringType()
                return ArrayType(arr_part, Typ)
            else:
                Typ = Id(ctx.ID().getText())
                return ArrayType(arr_part, Typ)
        else:
            if ctx.INT():
                return IntType()
            elif ctx.FLOAT():
                return FloatType()
            elif ctx.BOOLEAN():
                return BoolType()
            elif ctx.STRING():
                return StringType()
            else:
                return Id(ctx.ID().getText())


    """var_declared: var_full | var_type | var_init;"""
    def visitVar_declared(self, ctx:MiniGoParser.Var_declaredContext):
        return self.visitChildren(ctx)


    """var_full: VAR ID dec_type (ASSIGN expr) ignore;"""
    def visitVar_full(self, ctx:MiniGoParser.Var_fullContext):
        nam = ctx.ID().getText()
        typ = self.visit(ctx.dec_type())
        ini = self.visit(ctx.expr())

        return VarDecl(nam, typ, ini)

    """var_type: VAR ID dec_type ignore;"""
    def visitVar_type(self, ctx:MiniGoParser.Var_typeContext):
        nam = ctx.ID().getText()
        typ = self.visit(ctx.dec_type())
        ini = None

        return VarDecl(nam, typ, ini)

    """var_init: VAR ID (ASSIGN expr) ignore;"""
    def visitVar_init(self, ctx:MiniGoParser.Var_initContext):
        nam = ctx.ID().getText()
        typ = None
        ini = self.visit(ctx.expr())

        return VarDecl(nam, typ, ini)

    """const_declared: CONST ID ASSIGN expr ignore;"""
    def visitConst_declared(self, ctx:MiniGoParser.Const_declaredContext):
        nam = ctx.ID().getText()
        typ = None
        ini = self.visit(ctx.expr())

        return ConstDecl(nam, typ, ini)

    """func_declared: FUNC ID para dec_type? body_block ignore;"""
    def visitFunc_declared(self, ctx:MiniGoParser.Func_declaredContext):
        nam = ctx.ID().getText()
        param = self.visit(ctx.para())
        typ = VoidType()

        if ctx.dec_type():
            typ = self.visit(ctx.dec_type())
        body = self.visit(ctx.body_block())
        return FuncDecl(nam, param, typ, body)


    """method_declared: FUNC method_struct_name ID para dec_type? body_block ignore;"""
    def visitMethod_declared(self, ctx:MiniGoParser.Method_declaredContext):
        nam = ctx.ID().getText()
        param = self.visit(ctx.para())
        typ = VoidType()
        if ctx.dec_type():
            typ = self.visit(ctx.dec_type())
        body = self.visit(ctx.body_block())
        fun = FuncDecl(nam, param, typ, body)
        rec, rectyp = self.visit(ctx.method_struct_name())

        return MethodDecl(rec, rectyp, fun)

    """method_struct_name: (LRB ID ID RRB) ;"""
    def visitMethod_struct_name(self, ctx:MiniGoParser.Method_struct_nameContext):
        return ctx.ID()[0].getText(), Id(ctx.ID()[1].getText())
    #(c Calculator) -> c is receiver, Calculator is type


    """struct_declared: TYPE ID STRUCT struct_body ignore;"""
    def visitStruct_declared(self, ctx:MiniGoParser.Struct_declaredContext):
        nam = ctx.ID().getText()
        ele = self.visit(ctx.struct_body())
        med = []

        return StructType(nam, ele, med)


    """struct_body: (LCB list_struct_declared RCB) ;"""
    def visitStruct_body(self, ctx:MiniGoParser.Struct_bodyContext):
        return self.visit(ctx.list_struct_declared())


    """list_struct_declared: struct_index list_struct_declared | struct_index ;"""
    def visitList_struct_declared(self, ctx:MiniGoParser.List_struct_declaredContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.struct_index())]
        return [self.visit(ctx.struct_index())] + self.visit(ctx.list_struct_declared())


    """struct_index: (ID dec_type ignore) ;"""
    def visitStruct_index(self, ctx:MiniGoParser.Struct_indexContext):
        nam = ctx.ID().getText()
        typ = self.visit(ctx.dec_type())

        return (nam, typ)


    """interface_declared: TYPE ID INTERFACE interface_body ignore;"""
    def visitInterface_declared(self, ctx:MiniGoParser.Interface_declaredContext):
        nam = ctx.ID().getText()
        method = self.visit(ctx.interface_body())

        return InterfaceType(nam, method)


    """interface_body: (LCB list_interface_declared RCB) ;"""
    def visitInterface_body(self, ctx:MiniGoParser.Interface_bodyContext):
        return self.visit(ctx.list_interface_declared())


    """list_interface_declared: line_inter list_interface_declared | line_inter;"""
    def visitList_interface_declared(self, ctx:MiniGoParser.List_interface_declaredContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.line_inter())]
        return [self.visit(ctx.line_inter())] + self.visit(ctx.list_interface_declared())


    """line_inter: ID para2 dec_type? ignore;"""
    def visitLine_inter(self, ctx:MiniGoParser.Line_interContext):
        nam = ctx.ID().getText()
        params = self.visit(ctx.para2())
        retyp = VoidType()

        if ctx.dec_type():
            retyp = self.visit(ctx.dec_type())
        return Prototype(nam, params, retyp)


    """inter_para: list_id dec_type COMMA inter_para | list_id dec_type;"""
    def visitInter_para(self, ctx:MiniGoParser.Inter_paraContext):
        if ctx.getChildCount() == 2:
            names = self.visit(ctx.list_id())
            typ = self.visit(ctx.dec_type())
            return [ParamDecl(nam, typ) for nam in names]
        
        names = self.visit(ctx.list_id())
        typ = self.visit(ctx.dec_type())
        return [ParamDecl(nam, typ) for nam in names] + self.visit(ctx.inter_para())


    """list_id: ID COMMA list_id | ID;"""
    def visitList_id(self, ctx:MiniGoParser.List_idContext):
        if ctx.getChildCount() == 1:
            return [ctx.ID().getText()]
        return [ctx.ID().getText()] + self.visit(ctx.list_id())
    

    """para: LRB inter_para? RRB ;"""
    def visitPara(self, ctx:MiniGoParser.ParaContext):
        if ctx.inter_para():
            return self.visit(ctx.inter_para())
        return []


    """inter_para2: list_id dec_type COMMA inter_para2 | list_id dec_type;"""
    def visitInter_para2(self, ctx:MiniGoParser.Inter_para2Context):
        if ctx.getChildCount() == 2:
            names = self.visit(ctx.list_id())
            typ = self.visit(ctx.dec_type())
            cnt = len(names)
            ret = [typ] * cnt
            return ret
        
        names = self.visit(ctx.list_id())
        typ = self.visit(ctx.dec_type())
        cnt = len(names)
        ret = [typ] * cnt
        return ret + self.visit(ctx.inter_para2())


    """para2: LRB inter_para2? RRB ;"""
    def visitPara2(self, ctx:MiniGoParser.Para2Context):
        if ctx.inter_para2():
            return self.visit(ctx.inter_para2())
        return []

    """list_statement: statement list_statement | statement;"""
    def visitList_statement(self, ctx:MiniGoParser.List_statementContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.statement())]
        return [self.visit(ctx.statement())] + self.visit(ctx.list_statement())
        


    """
    statement:
    (
        declared_statement
        | assign_statement
        | if_statement
        | for_statement
        | break_statement
        | continue_statement
        | call_statement
        | return_statement
    );
    """
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visitChildren(ctx)


    """declared_statement: var_declared | const_declared ;"""
    def visitDeclared_statement(self, ctx:MiniGoParser.Declared_statementContext):
        return self.visitChildren(ctx)


    """assign_operator: ASSIGN_ADD | ASSIGN_DIV | ASSIGN_MOD | ASSIGN_MUL | ASSIGN_OP | ASSIGN_SUB;"""
    def visitAssign_operator(self, ctx:MiniGoParser.Assign_operatorContext):
        if ctx.ASSIGN_ADD():
            return '+'
        elif ctx.ASSIGN_SUB():
            return '-'
        elif ctx.ASSIGN_MUL():
            return '*'
        elif ctx.ASSIGN_DIV():
            return '/'
        elif ctx.ASSIGN_MOD():
            return '%'
        elif ctx.ASSIGN_OP():
            return '='


    """assign_statement: scalar_var_rec assign_operator expr ignore ;"""
    def visitAssign_statement(self, ctx:MiniGoParser.Assign_statementContext):
        op = self.visit(ctx.assign_operator())
        lhs = self.visit(ctx.scalar_var_rec())
        rhs = self.visit(ctx.expr())
        if op != '=':
            return Assign(lhs, BinaryOp(op, lhs, rhs))
        return Assign(lhs, rhs)


    """scalar_var: (ID | ID array_init_sca);"""
    def visitScalar_var(self, ctx:MiniGoParser.Scalar_varContext):
        if ctx.getChildCount() == 1:
            return Id(ctx.ID().getText())
        
        nam = Id(ctx.ID().getText())
        idx = self.visit(ctx.array_init_sca())
        
        return ArrayCell(nam, idx)


    """scalar_var_rec: scalar_var_rec DOT scalar_var | scalar_var;"""
    def visitScalar_var_rec(self, ctx:MiniGoParser.Scalar_var_recContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.scalar_var())
        
        rec = self.visit(ctx.scalar_var_rec())
        fie = self.visit(ctx.scalar_var())
        # return FieldAccess(rec, fie)

        if isinstance(fie, ArrayCell):
            # return FieldAccess(rec, str(fie))
            return ArrayCell(FieldAccess(rec, fie.arr.name), fie.idx)
        if isinstance(fie, Id):
            return FieldAccess(rec, fie.name)
        


    """array_init_sca: array_init_sca LSB expr RSB | LSB expr RSB;"""
    def visitArray_init_sca(self, ctx:MiniGoParser.Array_init_scaContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.expr())]
        return self.visit(ctx.array_init_sca()) + [self.visit(ctx.expr())]


    """if_statement: IF (LRB expr RRB) body_block else_if_statement_rec? else_statement? ignore;"""
    def visitIf_statement(self, ctx:MiniGoParser.If_statementContext):

        if_exp = self.visit(ctx.expr())
        if_block = self.visit(ctx.body_block())
        ret = If(if_exp, if_block, None)

        if ctx.else_if_statement_rec():
            lst_elif = self.visit(ctx.else_if_statement_rec())
            len_elif = len(lst_elif)
            
            curr = ret
            for i in range(len_elif):
                next_if = If(lst_elif[i][0], lst_elif[i][1], None)
                curr.elseStmt = next_if
                curr = next_if

            if ctx.else_statement():
                else_block = self.visit(ctx.else_statement())
                curr.elseStmt = else_block

        elif ctx.else_statement():
            else_block = self.visit(ctx.else_statement())
            ret.elseStmt = else_block
        
        return ret

        


    """else_if_statement: ELSE IF (LRB expr RRB) body_block;"""
    def visitElse_if_statement(self, ctx:MiniGoParser.Else_if_statementContext):
        exp = self.visit(ctx.expr())
        body = self.visit(ctx.body_block())
        
        return (exp, body)


    """else_if_statement_rec: else_if_statement else_if_statement_rec | else_if_statement;"""
    def visitElse_if_statement_rec(self, ctx:MiniGoParser.Else_if_statement_recContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.else_if_statement())]
        return [self.visit(ctx.else_if_statement())] + self.visit(ctx.else_if_statement_rec())


    """else_statement: ELSE body_block;"""
    def visitElse_statement(self, ctx:MiniGoParser.Else_statementContext):
        return self.visit(ctx.body_block())


    """for_statement: (for_cond | for_3var | for_range) body_block ignore;"""
    def visitFor_statement(self, ctx:MiniGoParser.For_statementContext):
        body = self.visit(ctx.body_block())

        if ctx.for_cond():
            for_exp = self.visit(ctx.for_cond())
            return ForBasic(for_exp, body)
        
        elif ctx.for_3var():
            init, cond, upda = self.visit(ctx.for_3var())
            return ForStep(init, cond, upda, body)
        
        else:
            idx, value, arr = self.visit(ctx.for_range())
            return ForEach(idx, value, arr, body)


    """for_3var: FOR f3v_init SEMICOLON expr SEMICOLON f3v_modi;"""
    def visitFor_3var(self, ctx:MiniGoParser.For_3varContext):
        init = self.visit(ctx.f3v_init())
        cond = self.visit(ctx.expr())
        upda = self.visit(ctx.f3v_modi())

        return init, cond, upda


    """f3v_init: (ID assign_operator expr) | (VAR ID dec_type? ASSIGN expr);"""
    def visitF3v_init(self, ctx:MiniGoParser.F3v_initContext):
        if ctx.VAR():
            typ = None
            if ctx.dec_type():
                typ = self.visit(ctx.dec_type())
            nam = ctx.ID().getText()
            init = self.visit(ctx.expr())

            return VarDecl(nam, typ, init)
        
        #Assign stmt case:
        op = self.visit(ctx.assign_operator())
        lhs = Id(ctx.ID().getText())
        rhs = self.visit(ctx.expr())
        if op != '=':
            return Assign(lhs, BinaryOp(op, lhs, rhs))
        return Assign(lhs, rhs)



    """f3v_modi: ID assign_operator expr;"""
    def visitF3v_modi(self, ctx:MiniGoParser.F3v_modiContext):
        op = self.visit(ctx.assign_operator())
        lhs = Id(ctx.ID().getText())
        rhs = self.visit(ctx.expr())
        if op != '=':
            return Assign(lhs, BinaryOp(op, lhs, rhs))
        return Assign(lhs, rhs)

    """for_cond: FOR expr;"""
    def visitFor_cond(self, ctx:MiniGoParser.For_condContext):
        return self.visit(ctx.expr())


    """for_range: FOR ID COMMA ID ASSIGN_OP RANGE expr;"""
    def visitFor_range(self, ctx:MiniGoParser.For_rangeContext):
        idx = Id(ctx.ID()[0].getText())
        value = Id(ctx.ID()[1].getText())
        arr = self.visit(ctx.expr())

        return idx, value, arr


    """break_statement:  BREAK ignore;"""
    def visitBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        return Break()


    """continue_statement:  CONTINUE ignore;"""
    def visitContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
        return Continue()


    """call_statement:  scalar_var_rec LRB list_expr? RRB ignore ;"""
    def visitCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        caller = self.visit(ctx.scalar_var_rec())
        argm = []

        if ctx.list_expr():
            argm = self.visit(ctx.list_expr())
        if isinstance(caller, FieldAccess):
            return MethCall(caller.receiver, caller.field, argm)
        elif isinstance(caller, Id):
            return FuncCall(caller.name, argm)


    """return_statement: RETURN expr? ignore;"""
    def visitReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
        expr = None
        if ctx.expr():
            expr = self.visit(ctx.expr())
        return Return(expr)


    """ignore: SEMICOLON | NEWLINE ;"""
    def visitIgnore(self, ctx:MiniGoParser.IgnoreContext):
        if ctx.SEMICOLON():
            return ctx.SEMICOLON()
        return ctx.NEWLINE()


    """body_block: LCB list_statement? RCB;"""
    def visitBody_block(self, ctx:MiniGoParser.Body_blockContext):
        return Block(self.visit(ctx.list_statement())) if ctx.list_statement() else Block([])
