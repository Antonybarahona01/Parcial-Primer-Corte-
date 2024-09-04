# Generated from TrigCalc.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\n")
        buf.write(".\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\5\2\20\n\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\6\6\6\"\n\6\r\6\16\6#\3\6\3\6\6\6")
        buf.write("(\n\6\r\6\16\6)\5\6,\n\6\3\6\2\2\7\2\4\6\b\n\2\2\2-\2")
        buf.write("\17\3\2\2\2\4\21\3\2\2\2\6\26\3\2\2\2\b\33\3\2\2\2\n!")
        buf.write("\3\2\2\2\f\20\5\4\3\2\r\20\5\6\4\2\16\20\5\b\5\2\17\f")
        buf.write("\3\2\2\2\17\r\3\2\2\2\17\16\3\2\2\2\20\3\3\2\2\2\21\22")
        buf.write("\7\3\2\2\22\23\7\4\2\2\23\24\5\n\6\2\24\25\7\5\2\2\25")
        buf.write("\5\3\2\2\2\26\27\7\6\2\2\27\30\7\4\2\2\30\31\5\n\6\2\31")
        buf.write("\32\7\5\2\2\32\7\3\2\2\2\33\34\7\7\2\2\34\35\7\4\2\2\35")
        buf.write("\36\5\n\6\2\36\37\7\5\2\2\37\t\3\2\2\2 \"\7\n\2\2! \3")
        buf.write("\2\2\2\"#\3\2\2\2#!\3\2\2\2#$\3\2\2\2$+\3\2\2\2%\'\7\b")
        buf.write("\2\2&(\7\n\2\2\'&\3\2\2\2()\3\2\2\2)\'\3\2\2\2)*\3\2\2")
        buf.write("\2*,\3\2\2\2+%\3\2\2\2+,\3\2\2\2,\13\3\2\2\2\6\17#)+")
        return buf.getvalue()


class TrigCalcParser ( Parser ):

    grammarFileName = "TrigCalc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Sin'", "'('", "')'", "'Cos'", "'Tan'", 
                     "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "WS", "DIGIT" ]

    RULE_expr = 0
    RULE_sin_expr = 1
    RULE_cos_expr = 2
    RULE_tan_expr = 3
    RULE_number = 4

    ruleNames =  [ "expr", "sin_expr", "cos_expr", "tan_expr", "number" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    WS=7
    DIGIT=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sin_expr(self):
            return self.getTypedRuleContext(TrigCalcParser.Sin_exprContext,0)


        def cos_expr(self):
            return self.getTypedRuleContext(TrigCalcParser.Cos_exprContext,0)


        def tan_expr(self):
            return self.getTypedRuleContext(TrigCalcParser.Tan_exprContext,0)


        def getRuleIndex(self):
            return TrigCalcParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = TrigCalcParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expr)
        try:
            self.state = 13
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TrigCalcParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 10
                self.sin_expr()
                pass
            elif token in [TrigCalcParser.T__3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 11
                self.cos_expr()
                pass
            elif token in [TrigCalcParser.T__4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 12
                self.tan_expr()
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

    class Sin_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(TrigCalcParser.NumberContext,0)


        def getRuleIndex(self):
            return TrigCalcParser.RULE_sin_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSin_expr" ):
                listener.enterSin_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSin_expr" ):
                listener.exitSin_expr(self)




    def sin_expr(self):

        localctx = TrigCalcParser.Sin_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sin_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.match(TrigCalcParser.T__0)
            self.state = 16
            self.match(TrigCalcParser.T__1)
            self.state = 17
            self.number()
            self.state = 18
            self.match(TrigCalcParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Cos_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(TrigCalcParser.NumberContext,0)


        def getRuleIndex(self):
            return TrigCalcParser.RULE_cos_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCos_expr" ):
                listener.enterCos_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCos_expr" ):
                listener.exitCos_expr(self)




    def cos_expr(self):

        localctx = TrigCalcParser.Cos_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_cos_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(TrigCalcParser.T__3)
            self.state = 21
            self.match(TrigCalcParser.T__1)
            self.state = 22
            self.number()
            self.state = 23
            self.match(TrigCalcParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Tan_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(TrigCalcParser.NumberContext,0)


        def getRuleIndex(self):
            return TrigCalcParser.RULE_tan_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTan_expr" ):
                listener.enterTan_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTan_expr" ):
                listener.exitTan_expr(self)




    def tan_expr(self):

        localctx = TrigCalcParser.Tan_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_tan_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(TrigCalcParser.T__4)
            self.state = 26
            self.match(TrigCalcParser.T__1)
            self.state = 27
            self.number()
            self.state = 28
            self.match(TrigCalcParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(TrigCalcParser.DIGIT)
            else:
                return self.getToken(TrigCalcParser.DIGIT, i)

        def getRuleIndex(self):
            return TrigCalcParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = TrigCalcParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 30
                self.match(TrigCalcParser.DIGIT)
                self.state = 33 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==TrigCalcParser.DIGIT):
                    break

            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TrigCalcParser.T__5:
                self.state = 35
                self.match(TrigCalcParser.T__5)
                self.state = 37 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 36
                    self.match(TrigCalcParser.DIGIT)
                    self.state = 39 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==TrigCalcParser.DIGIT):
                        break



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





