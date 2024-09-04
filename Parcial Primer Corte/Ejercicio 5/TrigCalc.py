import sys
import math
from antlr4 import *
from TrigLexer import TrigLexer
from TrigParser import TrigParser
from TrigListener import TrigListener

class TrigCalcListener(TrigListener):
    def enterSinExpr(self, ctx):
        num = float(ctx.NUM().getText())
        rad = math.radians(num)
        result = math.sin(rad)
        print(f'Sin({num}) = {result}')

    def enterCosExpr(self, ctx):
        num = float(ctx.NUM().getText())
        rad = math.radians(num)
        result = math.cos(rad)
        print(f'Cos({num}) = {result}')

    def enterTanExpr(self, ctx):
        num = float(ctx.NUM().getText())
        rad = math.radians(num)
        result = math.tan(rad)
        print(f'Tan({num}) = {result}')

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = TrigLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = TrigParser(stream)
    tree = parser.prog()

    listener = TrigCalcListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main(sys.argv)
