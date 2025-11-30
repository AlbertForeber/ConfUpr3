from termcolor import cprint

from assembler import Assembler



if __name__ == "__main__":
    assembler = Assembler()
    program = dict()

    print("Введите путь к файлу с исходным кодом\n>> ", end='')
    read_from = input()
    print("Введите путь для файла с машинным кодом\n>> ", end='')
    write_to = input()
    assembler.assemble_program(read_from, write_to, testing=True)


