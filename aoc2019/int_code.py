import re

class IntCode:
    #address references
    NOUN = 1
    VERB = 2

    #opcodes
    ADD = 1
    MULTIPLY = 2
    SAVE_INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    STOP = 99

    def __init__(self, input_file):
        file = open(input_file, 'r')
        self.initial_state = [int(x) for x in re.split(r',', file.readline().strip())]
        file.close()
        self.reinitialize()

    def reinitialize(self):
        self.registers = [x for x in self.initial_state]
        self.output = []

    def generate_modes(self, instruction):
        modes = [int(x) for x in '{modes:03d}'.format(modes=(instruction // 100))]
        modes.reverse()
        return modes

    def parse_parameter(self, parameter, mode):
        if mode == 1:
            return parameter
        return self.registers[parameter]

    def add(self, instruction_pointer, modes):
        left, right, store = self.registers[instruction_pointer + 1: instruction_pointer + 4]
        left_mode, right_mode, _ = modes
        self.registers[store] = (self.parse_parameter(left, left_mode)
                                 + self.parse_parameter(right, right_mode))

    def multiply(self, instruction_pointer, modes):
        left, right, store = self.registers[instruction_pointer + 1: instruction_pointer + 4]
        left_mode, right_mode, _ = modes
        self.registers[store] = (self.parse_parameter(left, left_mode)
                                 * self.parse_parameter(right, right_mode))

    def run_program(self, inputs=[]):
        instruction_pointer = 0
        while self.registers[instruction_pointer] != self.STOP:
            ip_mod = 0
            instruction = self.registers[instruction_pointer]
            opcode = instruction % 100
            modes = self.generate_modes(instruction)
            if opcode == self.ADD:
                ip_mod = 4
                self.add(instruction_pointer, modes)
            elif opcode == self.MULTIPLY:
                ip_mod = 4
                self.multiply(instruction_pointer, modes)
            elif opcode == self.SAVE_INPUT:
                assert 1 not in modes, 'cannot save to an immediate {instruction}'.format(
                    instruction=(opcode, modes)
                )
                ip_mod = 2
                parameter = self.registers[instruction_pointer + 1]
                self.registers[parameter] = inputs[0]
                inputs.pop(0)
            elif opcode == self.OUTPUT:
                ip_mod = 2
                immediate, _, _ = modes
                parameter = self.registers[instruction_pointer + 1]
                self.output.append(self.parse_parameter(parameter, immediate))
            elif opcode == self.JUMP_IF_TRUE:
                non_zero, jump = self.registers[instruction_pointer + 1: instruction_pointer + 3]
                nz_mode, jmp_mode, _ = modes
                if self.parse_parameter(non_zero, nz_mode):
                    instruction_pointer = self.parse_parameter(jump, jmp_mode)
                else:
                    ip_mod = 3
            elif opcode == self.JUMP_IF_FALSE:
                non_zero, jump = self.registers[instruction_pointer + 1: instruction_pointer + 3]
                nz_mode, jmp_mode, _ = modes
                if self.parse_parameter(non_zero, nz_mode):
                    ip_mod = 3
                else:
                    instruction_pointer = self.parse_parameter(jump, jmp_mode)
            elif opcode == self.LESS_THAN:
                left, right, store = self.registers[
                    instruction_pointer + 1: instruction_pointer + 4]
                left_mode, right_mode, _ = modes
                self.registers[store] = 1 if (
                    self.parse_parameter(left, left_mode)
                    < self.parse_parameter(right, right_mode)) else 0
                ip_mod = 4
            elif opcode == self.EQUALS:
                left, right, store = self.registers[
                    instruction_pointer + 1: instruction_pointer + 4]
                left_mode, right_mode, _ = modes
                self.registers[store] = 1 if (
                    self.parse_parameter(left, left_mode)
                    == self.parse_parameter(right, right_mode)) else 0
                ip_mod = 4
            else:
                assert False, 'unsupported opcode {opcode} at position {pos}'.format(
                    opcode=opcode,
                    pos=instruction_pointer)
            instruction_pointer += ip_mod
        return self.output
