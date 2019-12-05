import re

class Intcode:
    #address references
    NOUN = 1
    VERB = 2

    #opcodes
    ADD = 1
    MULTIPLY = 2
    WRITE = 3
    READ = 4
    STOP = 99

    def __init__(self, input_file):
        file = open(input_file, 'r')
        self.initial_state = [int(x) for x in re.split(r',', file.readline().strip())]
        file.close()
        self.reinitialize()

    def reinitialize(self):
        self.registers = [x for x in self.initial_state]

    def add(self, instruction_pointer, modes):
        parameters = self.registers[instruction_pointer + 1: instruction_pointer + 4]
        self.registers[parameters[2]] = (self.registers[parameters[0]]
                                        + self.registers[parameters[1]])

    def multiply(self, instruction_pointer, modes):
        parameters = self.registers[instruction_pointer + 1: instruction_pointer + 4]
        self.registers[parameters[2]] = (self.registers[parameters[0]]
                                         * self.registers[parameters[1]])

    def read(self, instruction_pointer, modes):
        parameter = self.registers[instruction_pointer + 1]
        print(self.registers[parameter])

    def run_program(self, program_input=0):
        instruction_pointer = 0
        while self.registers[instruction_pointer] != self.STOP:
            ip_mod = 1
            instruction = self.registers[instruction_pointer]
            opcode = instruction % 100
            modes = instruction // 100
            if opcode == self.ADD:
                ip_mod = 4
                self.add(instruction_pointer, modes)
            elif opcode == self.MULTIPLY:
                ip_mod = 4
                self.multiply(instruction_pointer, modes)
            elif opcode == self.WRITE:
                ip_mod = 2
                parameter = self.registers[instruction_pointer + 1]
                self.registers[parameter] = program_input
            elif opcode == self.READ:
                ip_mod = 2
                self.read(instruction_pointer, modes)
            else:
                assert False, 'unsupported opcode {opcode} at position {pos}'.format(opcode=opcode, pos=instruction_pointer)
            instruction_pointer += ip_mod
        return self.registers[0]
