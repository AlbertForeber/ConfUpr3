from termcolor import cprint
import os
from assembler import Assembler
from practise3.interpreter import Interpreter

if __name__ == "__main__":
    assembler = Assembler()
    assembler.test()
    program = dict()

    print("Введите путь к файлу с исходным кодом\n>> ", end='')
    read_from = input()
    print("Введите путь для файла с машинным кодом\n>> ", end='')
    write_to = input()
    assembler.assemble_program(read_from, write_to)

    interpreter = Interpreter()
    interpreter.sqrt_test()

    interpreter.execute(write_to)

