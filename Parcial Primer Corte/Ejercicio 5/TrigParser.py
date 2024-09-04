# Generated from Trig.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t")
        buf.write("\32\4\2\t\2\4\3\t\3\3\2\6\2\b\n\2\r\2\16\2\t\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\30\n\3\3\3")
        buf.write("\2\2\4\2\4\2\2\2\32\2\7\3\2\2\2\4\27\3\2\2\2\6\b\5\4\3")
        buf.write("\2\7\6\3\2\2\2\b\t\3\2\2\2\t\7\3\2\2\2\t\n\3\2\2\2\n\3")
        buf.write("\3\2\2\2\13\f\7\5\2\2\f\r\7\3\2\2\r\16\7\b\2\2\16\30\7")
        buf.write("\4\2\2\17\20\7\6\2\2\20\21\7\3\2\2\21\22\7\b\2\2\22\30")
        buf.write("\7\4\2\2\23\24\7\7\2\2\24\25\7\3\2\2\25\26\7\b\2\2\26")
        buf.write("\30\7\4\2\2\27\13\3\2\2\2\27\17\3\2\2\2\27\23\3\2\2\2")
        buf.write("\30\5\3\2\2\2\4\t\27")
        return buf.getvalue()


class TrigParser ( Parser ):

    grammarFileName = "Trig.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'Sin'", "'Cos'", "'Tan'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "SIN", "COS", 
                      "TAN", "NUM", "WS" ]

    RULE_prog = 0
    RULE_expr = 1

    ruleNames =  [ "prog", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    SIN=3
    COS=4
    TAN=5
    NUM=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TrigParser.ExprContext)
            else:
                return self.getTypedRuleContext(TrigParser.ExprContext,i)


        def getRuleIndex(self):
            return TrigParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = TrigParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 5 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 4
                self.expr()
                self.state = 7 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TrigParser.SIN) | (1 << TrigParser.COS) | (1 << TrigParser.TAN))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TrigParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CosExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TrigParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def COS(self):
            return self.getToken(TrigParser.COS, 0)
        def NUM(self):
            return self.getToken(TrigParser.NUM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCosExpr" ):
                listener.enterCosExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCosExpr" ):
                listener.exitCosExpr(self)


    class SinExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TrigParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SIN(self):
            return self.getToken(TrigParser.SIN, 0)
        def NUM(self):
            return self.getToken(TrigParser.NUM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSinExpr" ):
                listener.enterSinExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSinExpr" ):
                listener.exitSinExpr(self)


    class TanExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TrigParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TAN(self):
            return self.getToken(TrigParser.TAN, 0)
        def NUM(self):
            return self.getToken(TrigParser.NUM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTanExpr" ):
                listener.enterTanExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTanExpr" ):
                listener.exitTanExpr(self)



    def expr(self):

        localctx = TrigParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TrigParser.SIN]:
                localctx = TrigParser.SinExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 9
                self.match(TrigParser.SIN)
                self.state = 10
                self.match(TrigParser.T__0)
                self.state = 11
                self.match(TrigParser.NUM)
                self.state = 12
                self.match(TrigParser.T__1)
                pass
            elif token in [TrigParser.COS]:
                localctx = TrigParser.CosExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 13
                self.match(TrigParser.COS)
                self.state = 14
                self.match(TrigParser.T__0)
                self.state = 15
                self.match(TrigParser.NUM)
                self.state = 16
                self.match(TrigParser.T__1)
                pass
            elif token in [TrigParser.TAN]:
                localctx = TrigParser.TanExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 17
                self.match(TrigParser.TAN)
                self.state = 18
                self.match(TrigParser.T__0)
                self.state = 19
                self.match(TrigParser.NUM)
                self.state = 20
                self.match(TrigParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





