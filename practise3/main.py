from termcolor import cprint

from assembler import Assembler



if __name__ == "__main__":
    assembler = Assembler()
    assembler.test()
    program = dict()



    assembler.assemble_program(program, "byte_code")


