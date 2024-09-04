from antlr4 import *
from TrigCalcLexer import TrigCalcLexer
from TrigCalcParser import TrigCalcParser

def main():
    input_stream = FileStream('expr.in')
    lexer = TrigCalcLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = TrigCalcParser(stream)
    tree = parser.expression()  # o el nombre de tu regla de inicio

    # Aquí deberías tener el código para evaluar el árbol y imprimir resultados
    print("Processing complete")

if __name__ == '__main__':
    main()
