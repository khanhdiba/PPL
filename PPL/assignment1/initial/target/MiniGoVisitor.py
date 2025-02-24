# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_declare.
    def visitList_declare(self, ctx:MiniGoParser.List_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#int_lit.
    def visitInt_lit(self, ctx:MiniGoParser.Int_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_literal.
    def visitArray_literal(self, ctx:MiniGoParser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_type.
    def visitArray_type(self, ctx:MiniGoParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_init.
    def visitArray_init(self, ctx:MiniGoParser.Array_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_index.
    def visitArray_index(self, ctx:MiniGoParser.Array_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_array_index.
    def visitList_array_index(self, ctx:MiniGoParser.List_array_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_literal.
    def visitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_element.
    def visitList_element(self, ctx:MiniGoParser.List_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_expr.
    def visitList_expr(self, ctx:MiniGoParser.List_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr.
    def visitExpr(self, ctx:MiniGoParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr1.
    def visitExpr1(self, ctx:MiniGoParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr2.
    def visitExpr2(self, ctx:MiniGoParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr3.
    def visitExpr3(self, ctx:MiniGoParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr4.
    def visitExpr4(self, ctx:MiniGoParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr5.
    def visitExpr5(self, ctx:MiniGoParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr6.
    def visitExpr6(self, ctx:MiniGoParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr7.
    def visitExpr7(self, ctx:MiniGoParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#log_op.
    def visitLog_op(self, ctx:MiniGoParser.Log_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#add_op.
    def visitAdd_op(self, ctx:MiniGoParser.Add_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#mul_op.
    def visitMul_op(self, ctx:MiniGoParser.Mul_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#una_op.
    def visitUna_op(self, ctx:MiniGoParser.Una_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#parameter.
    def visitParameter(self, ctx:MiniGoParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_call.
    def visitFunc_call(self, ctx:MiniGoParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declared.
    def visitDeclared(self, ctx:MiniGoParser.DeclaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dec_type.
    def visitDec_type(self, ctx:MiniGoParser.Dec_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_declared.
    def visitVar_declared(self, ctx:MiniGoParser.Var_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_full.
    def visitVar_full(self, ctx:MiniGoParser.Var_fullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_type.
    def visitVar_type(self, ctx:MiniGoParser.Var_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_init.
    def visitVar_init(self, ctx:MiniGoParser.Var_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#const_declared.
    def visitConst_declared(self, ctx:MiniGoParser.Const_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_declared.
    def visitFunc_declared(self, ctx:MiniGoParser.Func_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_declared.
    def visitMethod_declared(self, ctx:MiniGoParser.Method_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_struct_name.
    def visitMethod_struct_name(self, ctx:MiniGoParser.Method_struct_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_declared.
    def visitStruct_declared(self, ctx:MiniGoParser.Struct_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_body.
    def visitStruct_body(self, ctx:MiniGoParser.Struct_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_struct_declared.
    def visitList_struct_declared(self, ctx:MiniGoParser.List_struct_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_index.
    def visitStruct_index(self, ctx:MiniGoParser.Struct_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_declared.
    def visitInterface_declared(self, ctx:MiniGoParser.Interface_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_body.
    def visitInterface_body(self, ctx:MiniGoParser.Interface_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_interface_declared.
    def visitList_interface_declared(self, ctx:MiniGoParser.List_interface_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#line_inter.
    def visitLine_inter(self, ctx:MiniGoParser.Line_interContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#inter_para.
    def visitInter_para(self, ctx:MiniGoParser.Inter_paraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_id.
    def visitList_id(self, ctx:MiniGoParser.List_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#para.
    def visitPara(self, ctx:MiniGoParser.ParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#inter_para2.
    def visitInter_para2(self, ctx:MiniGoParser.Inter_para2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#para2.
    def visitPara2(self, ctx:MiniGoParser.Para2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_statement.
    def visitList_statement(self, ctx:MiniGoParser.List_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declared_statement.
    def visitDeclared_statement(self, ctx:MiniGoParser.Declared_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_operator.
    def visitAssign_operator(self, ctx:MiniGoParser.Assign_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_statement.
    def visitAssign_statement(self, ctx:MiniGoParser.Assign_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#scalar_var.
    def visitScalar_var(self, ctx:MiniGoParser.Scalar_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#scalar_var_rec.
    def visitScalar_var_rec(self, ctx:MiniGoParser.Scalar_var_recContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_init_sca.
    def visitArray_init_sca(self, ctx:MiniGoParser.Array_init_scaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_statement.
    def visitIf_statement(self, ctx:MiniGoParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_if_statement.
    def visitElse_if_statement(self, ctx:MiniGoParser.Else_if_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_if_statement_rec.
    def visitElse_if_statement_rec(self, ctx:MiniGoParser.Else_if_statement_recContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_statement.
    def visitElse_statement(self, ctx:MiniGoParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_statement.
    def visitFor_statement(self, ctx:MiniGoParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_3var.
    def visitFor_3var(self, ctx:MiniGoParser.For_3varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#f3v_init.
    def visitF3v_init(self, ctx:MiniGoParser.F3v_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#f3v_modi.
    def visitF3v_modi(self, ctx:MiniGoParser.F3v_modiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_cond.
    def visitFor_cond(self, ctx:MiniGoParser.For_condContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_range.
    def visitFor_range(self, ctx:MiniGoParser.For_rangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#break_statement.
    def visitBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continue_statement.
    def visitContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#call_statement.
    def visitCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#return_statement.
    def visitReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ignore.
    def visitIgnore(self, ctx:MiniGoParser.IgnoreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#body_block.
    def visitBody_block(self, ctx:MiniGoParser.Body_blockContext):
        return self.visitChildren(ctx)



del MiniGoParser