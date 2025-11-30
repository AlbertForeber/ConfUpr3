from typing import List

class Interpreter:
    def __init__(self):
        self.memory: List[int] = [0] * 200
        self.registers: List[int] = [0] * 200

    @staticmethod
    def __mask(n):
        return 2**n - 1

    def __load_constant(self, address: int, constant: int):
        self.registers[address] = constant

    def __read(self, address_1: int, address_2: int, bias: int):
        self.registers[address_2] = self.memory[address_1 + bias]
        self.memory[address_1 + bias] = 0

    def __write(self, address_1: int, address_2: int):
        self.memory[self.registers[address_1]] = self.registers[address_2]
        self.registers[address_2] = 0

    def __dump_memory(self, file_name: str = "memory_dump.csv"):
        with open(file_name, "w") as f:
            for i in self.memory:
                f.write(f"{i};")

    def test(self):
        # Новые индексы массива
        self.__load_constant(0, 3)
        self.__load_constant(1, 4)
        self.__load_constant(2, 5)

        # Элементы массива
        self.memory[0] = 56
        self.memory[1] = 78
        self.memory[2] = 89

        # До копирования
        print(self.memory[:10])

        # Считываем массив
        self.__read(0, 3, 0)
        self.__read(1, 4, 0)
        self.__read(2, 5, 0)

        # Пишем массив на новое место
        self.__write(0, 3)
        self.__write(1, 4)
        self.__write(2, 5)

        # После копирования
        print(self.memory[:10])
        self.__dump_memory()



    def execute(self, file_name: str):
        f = open(file_name, "rb")
        byte_code = f.read().__bytes__()

        for i in range(0, len(byte_code), 5):
            command = int.from_bytes(byte_code[i:i+5], "little")
            operation = command & 0b1111

            match operation:
                case 1:
                    address = (command >> 4) & self.__mask(7)
                    constant = (command >> 11) & self.__mask(11)
                    self.__load_constant(address, constant)
                case 11:
                    address_1 = (command >> 4) & self.__mask(7)
                    address_2 = (command >> 11) & self.__mask(7)
                    bias = (command >> 18) & self.__mask(10)
                    self.__read(address_1, address_2, bias)
                case 0:
                    address_1 = (command >> 4) & self.__mask(7)
                    address_2 = (command >> 11) & self.__mask(7)
                    self.__write(address_1, address_2)
                case 10:
                    pass
                case _:
                    raise ValueError("Неизвестная команда")
        self.__dump_memory()



