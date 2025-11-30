from typing import Dict, List

class Assembler:
    @staticmethod
    def __translator(file_name: str) -> Dict[str, List[int]]:
        program: Dict[str, List[int]] = dict()
        for readline in open(file_name):
            line = readline.strip()[:-1]
            line = line.split(";")
            program[line[0]] = [int(i) for i in line[1:]]
        return program



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

