# Generated from Trig.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TrigParser import TrigParser
else:
    from TrigParser import TrigParser

# This class defines a complete listener for a parse tree produced by TrigParser.
class TrigListener(ParseTreeListener):

    # Enter a parse tree produced by TrigParser#prog.
    def enterProg(self, ctx:TrigParser.ProgContext):
        pass

    # Exit a parse tree produced by TrigParser#prog.
    def exitProg(self, ctx:TrigParser.ProgContext):
        pass


    # Enter a parse tree produced by TrigParser#sinExpr.
    def enterSinExpr(self, ctx:TrigParser.SinExprContext):
        pass

    # Exit a parse tree produced by TrigParser#sinExpr.
    def exitSinExpr(self, ctx:TrigParser.SinExprContext):
        pass


    # Enter a parse tree produced by TrigParser#cosExpr.
    def enterCosExpr(self, ctx:TrigParser.CosExprContext):
        pass

    # Exit a parse tree produced by TrigParser#cosExpr.
    def exitCosExpr(self, ctx:TrigParser.CosExprContext):
        pass


    # Enter a parse tree produced by TrigParser#tanExpr.
    def enterTanExpr(self, ctx:TrigParser.TanExprContext):
        pass

    # Exit a parse tree produced by TrigParser#tanExpr.
    def exitTanExpr(self, ctx:TrigParser.TanExprContext):
        pass



del TrigParser