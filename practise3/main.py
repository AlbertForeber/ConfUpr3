from termcolor import cprint
import os
from assembler import Assembler
from practise3.interpreter import Interpreter

if __name__ == "__main__":
    assembler = Assembler()
    assembler.test()
    program = dict()



    a = assembler.assemble_program("test.csv", "byte_code", True)

    interpreter = Interpreter()
    interpreter.execute("byte_code")


