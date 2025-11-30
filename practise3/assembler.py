from typing import Dict, List

class Assembler:
    @staticmethod
    def __translator(file_name: str) -> Dict[str, List[int]]:
        program: Dict[str, List[int]] = dict()
        for readline in open(file_name):
            line = readline.strip()

            if line.endswith(";"): line = line[:-1]

            line = line.split(";")
            program[line[0]] = [int(i) for i in line[1:]]
        return program

    @staticmethod
    def __mask(n: int):
        return 2**n - 1

    def __load_constant(self, address: int, constant: int):
        cmd = 1
        cmd |= (address & self.__mask(7)) << 4
        cmd |= (constant & self.__mask(23)) << 11

        return cmd.to_bytes(5, "little")

    def __read_from_memory(self, address_1: int, address_2: int, bias: int):
        cmd = 11
        cmd |= (address_1 & self.__mask(7)) << 4
        cmd |= (address_2 & self.__mask(7)) << 11
        cmd |= (bias & self.__mask(10)) << 18

        return cmd.to_bytes(5, "little")

    def __write_to_memory(self, address_1: int, address_2: int):
        cmd = 0
        cmd |= (address_1 & self.__mask(7)) << 4
        cmd |= (address_2 & self.__mask(7)) << 11

        return cmd.to_bytes(5, "little")

    def __sqrt(self, address_1: int, address_2: int, bias: int):
        cmd = 10
        cmd |= (address_1 & self.__mask(7)) << 4
        cmd |= (address_2 & self.__mask(7)) << 11
        cmd |= (bias & self.__mask(10)) << 18

        return cmd.to_bytes(5, "little")


    def test(self):
        assert list(self.__load_constant(54, 4)) == [0x61, 0x23, 0x0, 0x0, 0x0]
        assert list(self.__read_from_memory(3, 67, 181)) == [0x3B, 0x18, 0xD6, 0x02, 0x00]
        assert list(self.__write_to_memory(8, 126)) == [0x80, 0xF0, 0x03, 0x00, 0x00]
        assert list(self.__sqrt(85, 16, 753)) == [0x5A, 0x85, 0xC4, 0x0B, 0x00]

    def assemble_program(self, read_from: str, write_to: str = None, testing: bool = False):
        machine_code = b""
        program = self.__translator(read_from)



        for operation, args in program.items():
            match operation:
                case "LOAD":
                    if len(args) != 2:
                        raise ValueError(f"Ожидаемое аргументов для операции LOAD: 2, Получено: {len(args)}")
                    machine_code += self.__load_constant(*args)
                case "READ":
                    if len(args) != 3:
                        raise ValueError(f"Ожидаемое аргументов для операции READ: 3, Получено: {len(args)}")
                    machine_code += self.__read_from_memory(*args)
                case "WRITE":
                    if len(args) != 2:
                        raise ValueError(f"Ожидаемое аргументов для операции WRITE: 2, Получено: {len(args)}")
                    machine_code += self.__write_to_memory(*args)
                case "SQRT":
                    if len(args) != 3:
                        raise ValueError(f"Ожидаемое аргументов для операции SQRT: 3, Получено: {len(args)}")
                    machine_code += self.__sqrt(*args)
                case _:
                    raise ValueError(f"Неизвестная операция: {operation}")

        if write_to:
            with open(write_to, "wb") as f:
                f.write(machine_code)

        if testing:
            print([hex(i) for i in machine_code])

        return machine_code

