# Generated from TrigCalc.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TrigCalcParser import TrigCalcParser
else:
    from TrigCalcParser import TrigCalcParser

# This class defines a complete listener for a parse tree produced by TrigCalcParser.
class TrigCalcListener(ParseTreeListener):

    # Enter a parse tree produced by TrigCalcParser#expr.
    def enterExpr(self, ctx:TrigCalcParser.ExprContext):
        pass

    # Exit a parse tree produced by TrigCalcParser#expr.
    def exitExpr(self, ctx:TrigCalcParser.ExprContext):
        pass


    # Enter a parse tree produced by TrigCalcParser#sin_expr.
    def enterSin_expr(self, ctx:TrigCalcParser.Sin_exprContext):
        pass

    # Exit a parse tree produced by TrigCalcParser#sin_expr.
    def exitSin_expr(self, ctx:TrigCalcParser.Sin_exprContext):
        pass


    # Enter a parse tree produced by TrigCalcParser#cos_expr.
    def enterCos_expr(self, ctx:TrigCalcParser.Cos_exprContext):
        pass

    # Exit a parse tree produced by TrigCalcParser#cos_expr.
    def exitCos_expr(self, ctx:TrigCalcParser.Cos_exprContext):
        pass


    # Enter a parse tree produced by TrigCalcParser#tan_expr.
    def enterTan_expr(self, ctx:TrigCalcParser.Tan_exprContext):
        pass

    # Exit a parse tree produced by TrigCalcParser#tan_expr.
    def exitTan_expr(self, ctx:TrigCalcParser.Tan_exprContext):
        pass


    # Enter a parse tree produced by TrigCalcParser#number.
    def enterNumber(self, ctx:TrigCalcParser.NumberContext):
        pass

    # Exit a parse tree produced by TrigCalcParser#number.
    def exitNumber(self, ctx:TrigCalcParser.NumberContext):
        pass



del TrigCalcParser