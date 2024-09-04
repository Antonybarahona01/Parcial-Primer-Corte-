# Generated from Trig.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\t")
        buf.write("\65\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\4\b\t\b\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\6\3\7\6\7#\n\7\r\7\16\7$\3\7\3\7\6")
        buf.write("\7)\n\7\r\7\16\7*\5\7-\n\7\3\b\6\b\60\n\b\r\b\16\b\61")
        buf.write("\3\b\3\b\2\2\t\3\3\5\4\7\5\t\6\13\7\r\b\17\t\3\2\4\3\2")
        buf.write("\62;\5\2\13\f\17\17\"\"\28\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\3\21\3\2\2\2\5\23\3\2\2\2\7\25\3\2\2\2\t\31\3\2\2")
        buf.write("\2\13\35\3\2\2\2\r\"\3\2\2\2\17/\3\2\2\2\21\22\7*\2\2")
        buf.write("\22\4\3\2\2\2\23\24\7+\2\2\24\6\3\2\2\2\25\26\7U\2\2\26")
        buf.write("\27\7k\2\2\27\30\7p\2\2\30\b\3\2\2\2\31\32\7E\2\2\32\33")
        buf.write("\7q\2\2\33\34\7u\2\2\34\n\3\2\2\2\35\36\7V\2\2\36\37\7")
        buf.write("c\2\2\37 \7p\2\2 \f\3\2\2\2!#\t\2\2\2\"!\3\2\2\2#$\3\2")
        buf.write("\2\2$\"\3\2\2\2$%\3\2\2\2%,\3\2\2\2&(\7\60\2\2\')\t\2")
        buf.write("\2\2(\'\3\2\2\2)*\3\2\2\2*(\3\2\2\2*+\3\2\2\2+-\3\2\2")
        buf.write("\2,&\3\2\2\2,-\3\2\2\2-\16\3\2\2\2.\60\t\3\2\2/.\3\2\2")
        buf.write("\2\60\61\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2\62\63\3\2\2")
        buf.write("\2\63\64\b\b\2\2\64\20\3\2\2\2\7\2$*,\61\3\b\2\2")
        return buf.getvalue()


class TrigLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    SIN = 3
    COS = 4
    TAN = 5
    NUM = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'Sin'", "'Cos'", "'Tan'" ]

    symbolicNames = [ "<INVALID>",
            "SIN", "COS", "TAN", "NUM", "WS" ]

    ruleNames = [ "T__0", "T__1", "SIN", "COS", "TAN", "NUM", "WS" ]

    grammarFileName = "Trig.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


