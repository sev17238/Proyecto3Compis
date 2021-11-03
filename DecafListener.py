# Generated from Decaf.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DecafParser import DecafParser
else:
    from DecafParser import DecafParser

# This class defines a complete listener for a parse tree produced by DecafParser.
class DecafListener(ParseTreeListener):

    # Enter a parse tree produced by DecafParser#program.
    def enterProgram(self, ctx:DecafParser.ProgramContext):
        pass

    # Exit a parse tree produced by DecafParser#program.
    def exitProgram(self, ctx:DecafParser.ProgramContext):
        pass


    # Enter a parse tree produced by DecafParser#declaration.
    def enterDeclaration(self, ctx:DecafParser.DeclarationContext):
        pass

    # Exit a parse tree produced by DecafParser#declaration.
    def exitDeclaration(self, ctx:DecafParser.DeclarationContext):
        pass


    # Enter a parse tree produced by DecafParser#normalVar.
    def enterNormalVar(self, ctx:DecafParser.NormalVarContext):
        pass

    # Exit a parse tree produced by DecafParser#normalVar.
    def exitNormalVar(self, ctx:DecafParser.NormalVarContext):
        pass


    # Enter a parse tree produced by DecafParser#arrayVar.
    def enterArrayVar(self, ctx:DecafParser.ArrayVarContext):
        pass

    # Exit a parse tree produced by DecafParser#arrayVar.
    def exitArrayVar(self, ctx:DecafParser.ArrayVarContext):
        pass


    # Enter a parse tree produced by DecafParser#structDeclaration.
    def enterStructDeclaration(self, ctx:DecafParser.StructDeclarationContext):
        pass

    # Exit a parse tree produced by DecafParser#structDeclaration.
    def exitStructDeclaration(self, ctx:DecafParser.StructDeclarationContext):
        pass


    # Enter a parse tree produced by DecafParser#varType.
    def enterVarType(self, ctx:DecafParser.VarTypeContext):
        pass

    # Exit a parse tree produced by DecafParser#varType.
    def exitVarType(self, ctx:DecafParser.VarTypeContext):
        pass


    # Enter a parse tree produced by DecafParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:DecafParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by DecafParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:DecafParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by DecafParser#methodType.
    def enterMethodType(self, ctx:DecafParser.MethodTypeContext):
        pass

    # Exit a parse tree produced by DecafParser#methodType.
    def exitMethodType(self, ctx:DecafParser.MethodTypeContext):
        pass


    # Enter a parse tree produced by DecafParser#parameter.
    def enterParameter(self, ctx:DecafParser.ParameterContext):
        pass

    # Exit a parse tree produced by DecafParser#parameter.
    def exitParameter(self, ctx:DecafParser.ParameterContext):
        pass


    # Enter a parse tree produced by DecafParser#parameterType.
    def enterParameterType(self, ctx:DecafParser.ParameterTypeContext):
        pass

    # Exit a parse tree produced by DecafParser#parameterType.
    def exitParameterType(self, ctx:DecafParser.ParameterTypeContext):
        pass


    # Enter a parse tree produced by DecafParser#block.
    def enterBlock(self, ctx:DecafParser.BlockContext):
        pass

    # Exit a parse tree produced by DecafParser#block.
    def exitBlock(self, ctx:DecafParser.BlockContext):
        pass


    # Enter a parse tree produced by DecafParser#ifScope.
    def enterIfScope(self, ctx:DecafParser.IfScopeContext):
        pass

    # Exit a parse tree produced by DecafParser#ifScope.
    def exitIfScope(self, ctx:DecafParser.IfScopeContext):
        pass


    # Enter a parse tree produced by DecafParser#whileScope.
    def enterWhileScope(self, ctx:DecafParser.WhileScopeContext):
        pass

    # Exit a parse tree produced by DecafParser#whileScope.
    def exitWhileScope(self, ctx:DecafParser.WhileScopeContext):
        pass


    # Enter a parse tree produced by DecafParser#stmnt_return.
    def enterStmnt_return(self, ctx:DecafParser.Stmnt_returnContext):
        pass

    # Exit a parse tree produced by DecafParser#stmnt_return.
    def exitStmnt_return(self, ctx:DecafParser.Stmnt_returnContext):
        pass


    # Enter a parse tree produced by DecafParser#stmnt_methodCall.
    def enterStmnt_methodCall(self, ctx:DecafParser.Stmnt_methodCallContext):
        pass

    # Exit a parse tree produced by DecafParser#stmnt_methodCall.
    def exitStmnt_methodCall(self, ctx:DecafParser.Stmnt_methodCallContext):
        pass


    # Enter a parse tree produced by DecafParser#stmnt_block.
    def enterStmnt_block(self, ctx:DecafParser.Stmnt_blockContext):
        pass

    # Exit a parse tree produced by DecafParser#stmnt_block.
    def exitStmnt_block(self, ctx:DecafParser.Stmnt_blockContext):
        pass


    # Enter a parse tree produced by DecafParser#stmnt_equal.
    def enterStmnt_equal(self, ctx:DecafParser.Stmnt_equalContext):
        pass

    # Exit a parse tree produced by DecafParser#stmnt_equal.
    def exitStmnt_equal(self, ctx:DecafParser.Stmnt_equalContext):
        pass


    # Enter a parse tree produced by DecafParser#stmnt_expression.
    def enterStmnt_expression(self, ctx:DecafParser.Stmnt_expressionContext):
        pass

    # Exit a parse tree produced by DecafParser#stmnt_expression.
    def exitStmnt_expression(self, ctx:DecafParser.Stmnt_expressionContext):
        pass


    # Enter a parse tree produced by DecafParser#location.
    def enterLocation(self, ctx:DecafParser.LocationContext):
        pass

    # Exit a parse tree produced by DecafParser#location.
    def exitLocation(self, ctx:DecafParser.LocationContext):
        pass


    # Enter a parse tree produced by DecafParser#expr_cond_op.
    def enterExpr_cond_op(self, ctx:DecafParser.Expr_cond_opContext):
        pass

    # Exit a parse tree produced by DecafParser#expr_cond_op.
    def exitExpr_cond_op(self, ctx:DecafParser.Expr_cond_opContext):
        pass


    # Enter a parse tree produced by DecafParser#expr_location.
    def enterExpr_location(self, ctx:DecafParser.Expr_locationContext):
        pass

    # Exit a parse tree produced by DecafParser#expr_location.
    def exitExpr_location(self, ctx:DecafParser.Expr_locationContext):
        pass


    # Enter a parse tree produced by DecafParser#expr_literal.
    def enterExpr_literal(self, ctx:DecafParser.Expr_literalContext):
        pass

    # Exit a parse tree produced by DecafParser#expr_literal.
    def exitExpr_literal(self, ctx:DecafParser.Expr_literalContext):
        pass


    # Enter a parse tree produced by DecafParser#expr_op.
    def enterExpr_op(self, ctx:DecafParser.Expr_opContext):
        pass

    # Exit a parse tree produced by DecafParser#expr_op.
    def exitExpr_op(self, ctx:DecafParser.Expr_opContext):
        pass


    # Enter a parse tree produced by DecafParser#expr_eq_op.
    def enterExpr_eq_op(self, ctx:DecafParser.Expr_eq_opContext):
        pass

    # Exit a parse tree produced by DecafParser#expr_eq_op.
    def exitExpr_eq_op(self, ctx:DecafParser.Expr_eq_opContext):
        pass


    # Enter a parse tree produced by DecafParser#expr_minus.
    def enterExpr_minus(self, ctx:DecafParser.Expr_minusContext):
        pass

    # Exit a parse tree produced by DecafParser#expr_minus.
    def exitExpr_minus(self, ctx:DecafParser.Expr_minusContext):
        pass


    # Enter a parse tree produced by DecafParser#expr_par.
    def enterExpr_par(self, ctx:DecafParser.Expr_parContext):
        pass

    # Exit a parse tree produced by DecafParser#expr_par.
    def exitExpr_par(self, ctx:DecafParser.Expr_parContext):
        pass


    # Enter a parse tree produced by DecafParser#expr_arith_op.
    def enterExpr_arith_op(self, ctx:DecafParser.Expr_arith_opContext):
        pass

    # Exit a parse tree produced by DecafParser#expr_arith_op.
    def exitExpr_arith_op(self, ctx:DecafParser.Expr_arith_opContext):
        pass


    # Enter a parse tree produced by DecafParser#expr_rel_op.
    def enterExpr_rel_op(self, ctx:DecafParser.Expr_rel_opContext):
        pass

    # Exit a parse tree produced by DecafParser#expr_rel_op.
    def exitExpr_rel_op(self, ctx:DecafParser.Expr_rel_opContext):
        pass


    # Enter a parse tree produced by DecafParser#expr_methodCall.
    def enterExpr_methodCall(self, ctx:DecafParser.Expr_methodCallContext):
        pass

    # Exit a parse tree produced by DecafParser#expr_methodCall.
    def exitExpr_methodCall(self, ctx:DecafParser.Expr_methodCallContext):
        pass


    # Enter a parse tree produced by DecafParser#expr_not.
    def enterExpr_not(self, ctx:DecafParser.Expr_notContext):
        pass

    # Exit a parse tree produced by DecafParser#expr_not.
    def exitExpr_not(self, ctx:DecafParser.Expr_notContext):
        pass


    # Enter a parse tree produced by DecafParser#methodCall.
    def enterMethodCall(self, ctx:DecafParser.MethodCallContext):
        pass

    # Exit a parse tree produced by DecafParser#methodCall.
    def exitMethodCall(self, ctx:DecafParser.MethodCallContext):
        pass


    # Enter a parse tree produced by DecafParser#arg.
    def enterArg(self, ctx:DecafParser.ArgContext):
        pass

    # Exit a parse tree produced by DecafParser#arg.
    def exitArg(self, ctx:DecafParser.ArgContext):
        pass


    # Enter a parse tree produced by DecafParser#arith_op.
    def enterArith_op(self, ctx:DecafParser.Arith_opContext):
        pass

    # Exit a parse tree produced by DecafParser#arith_op.
    def exitArith_op(self, ctx:DecafParser.Arith_opContext):
        pass


    # Enter a parse tree produced by DecafParser#p_arith_op.
    def enterP_arith_op(self, ctx:DecafParser.P_arith_opContext):
        pass

    # Exit a parse tree produced by DecafParser#p_arith_op.
    def exitP_arith_op(self, ctx:DecafParser.P_arith_opContext):
        pass


    # Enter a parse tree produced by DecafParser#rel_op.
    def enterRel_op(self, ctx:DecafParser.Rel_opContext):
        pass

    # Exit a parse tree produced by DecafParser#rel_op.
    def exitRel_op(self, ctx:DecafParser.Rel_opContext):
        pass


    # Enter a parse tree produced by DecafParser#eq_op.
    def enterEq_op(self, ctx:DecafParser.Eq_opContext):
        pass

    # Exit a parse tree produced by DecafParser#eq_op.
    def exitEq_op(self, ctx:DecafParser.Eq_opContext):
        pass


    # Enter a parse tree produced by DecafParser#cond_op.
    def enterCond_op(self, ctx:DecafParser.Cond_opContext):
        pass

    # Exit a parse tree produced by DecafParser#cond_op.
    def exitCond_op(self, ctx:DecafParser.Cond_opContext):
        pass


    # Enter a parse tree produced by DecafParser#literal.
    def enterLiteral(self, ctx:DecafParser.LiteralContext):
        pass

    # Exit a parse tree produced by DecafParser#literal.
    def exitLiteral(self, ctx:DecafParser.LiteralContext):
        pass


    # Enter a parse tree produced by DecafParser#int_literal.
    def enterInt_literal(self, ctx:DecafParser.Int_literalContext):
        pass

    # Exit a parse tree produced by DecafParser#int_literal.
    def exitInt_literal(self, ctx:DecafParser.Int_literalContext):
        pass


    # Enter a parse tree produced by DecafParser#char_literal.
    def enterChar_literal(self, ctx:DecafParser.Char_literalContext):
        pass

    # Exit a parse tree produced by DecafParser#char_literal.
    def exitChar_literal(self, ctx:DecafParser.Char_literalContext):
        pass


    # Enter a parse tree produced by DecafParser#bool_literal.
    def enterBool_literal(self, ctx:DecafParser.Bool_literalContext):
        pass

    # Exit a parse tree produced by DecafParser#bool_literal.
    def exitBool_literal(self, ctx:DecafParser.Bool_literalContext):
        pass



del DecafParser