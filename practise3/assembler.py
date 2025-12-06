from typing import Dict, List
import argparse

class Assembler:
    def __init__(self):
        self.testing = False
        self.read_from = None
        self.write_to = None
        self.args = vars(self.__parse_args())


    @staticmethod
    def __translator(file_name: str) -> Dict[str, List[int]]:
        program: Dict[str, List[int]] = dict()
        for readline in open(file_name):
            line = readline.strip()[:-1]
            line = line.split(";")
            program[line[0]] = [int(i) for i in line[1:]]
        return program


    @staticmethod
    def __parse_args():
        parser = argparse.ArgumentParser(description="Assembler argument parser")
        parser.add_argument(
            "--read_from",
            type=str,
            required=True,
            help="Source code"
        )

        parser.add_argument(
            "--write_to",
            type=str,
            required=True,
            help="Path to output bytecode file"
        )

        parser.add_argument(
            "--testing",
            action="store_true",
            required=False,
            help="Activate test mode"
        )
        return parser.parse_args()



    def assemble_program(self, read_from: str, write_to: str = None, testing: bool = False):
        machine_code = b""
        program = self.__translator(read_from)

        if testing:
            print(program)
            return

        if write_to:
            with open(write_to, "wb") as f:
                f.write(machine_code)

        return machine_code

if __name__ == "__main__":
    assembler = Assembler()
    assembler.assemble_program(**assembler.args)