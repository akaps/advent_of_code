import re

def generate_modes(instruction):
    modes = [int(x) for x in '{modes:03d}'.format(modes=(instruction // 100))]
    modes.reverse()
    return modes

class IntCode:
    #address references
    NOUN = 1
    VERB = 2

    #parameter modes
    ADDRESS = 0
    IMMEDIATE = 1
    RELATIVE = 2

    #opcodes
    ADD = 1
    MULTIPLY = 2
    SAVE_INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    ADJUST_REL_BASE = 9
    STOP = 99

    def __init__(self, input_file):
        file = open(input_file, 'r')
        self.initial_state = [int(x) for x in re.split(r',', file.readline().strip())]
        file.close()
        self.reinitialize()
        self.inputs = []
        self.instruction_pointer = 0

    def reinitialize(self):
        self.instruction_pointer = 0
        self.registers = {index: x for index, x in enumerate(self.initial_state)}
        self.output = []
        self.relative_base = 0

    def parse_parameter(self, parameter, mode):
        if mode == self.ADDRESS:
            if parameter not in self.registers:
                self.registers[parameter] = 0
            return self.registers[parameter]
        if mode == self.IMMEDIATE:
            return parameter
        if mode == self.RELATIVE:
            adjusted = self.relative_base + parameter
            if adjusted not in self.registers:
                self.registers[adjusted] = 0
            return self.registers[adjusted]
        assert False, 'Unexpected mode {mode}'.format(mode=mode)
        return -1

    def get_parameters(self, start, end=None):
        if end:
            return [self.registers[self.instruction_pointer + i] for i in range(start, end)]
        return self.registers[self.instruction_pointer + start]

    def store(self, store_pos, store_mode, store_val):
        assert store_mode != self.IMMEDIATE, 'cannot save to an immediate'
        if store_mode == 0:
            self.registers[store_pos] = store_val
        else:
            self.registers[self.relative_base + store_pos] = store_val

    def add(self, modes):
        left, right, store = self.get_parameters(1, 4)
        left_mode, right_mode, store_mode = modes
        self.store(store, store_mode, (self.parse_parameter(left, left_mode)
                                       + self.parse_parameter(right, right_mode)))
        return 4

    def multiply(self, modes):
        left, right, store = self.get_parameters(1, 4)
        left_mode, right_mode, store_mode = modes
        self.store(store, store_mode, (self.parse_parameter(left, left_mode)
                                       * self.parse_parameter(right, right_mode)))
        return 4

    def save_input(self, modes):
        store = self.get_parameters(1)
        self.store(store, modes[0], self.inputs[0])
        self.inputs.pop(0)
        return 2

    def write_output(self, modes):
        immediate, _, _ = modes
        parameter = self.get_parameters(1)
        self.output.append(self.parse_parameter(parameter, immediate))
        return 2

    def jump_if_true(self, modes):
        non_zero, jump = self.get_parameters(1, 3)
        nz_mode, jmp_mode, _ = modes
        if self.parse_parameter(non_zero, nz_mode):
            self.instruction_pointer = self.parse_parameter(jump, jmp_mode)
            return 0
        return 3

    def jump_if_false(self, modes):
        non_zero, jump = self.get_parameters(1, 3)
        nz_mode, jmp_mode, _ = modes
        if self.parse_parameter(non_zero, nz_mode):
            return 3
        self.instruction_pointer = self.parse_parameter(jump, jmp_mode)
        return 0

    def less_than(self, modes):
        left, right, store = self.get_parameters(1, 4)
        left_mode, right_mode, store_mode = modes
        self.store(store, store_mode, 1 if (
            self.parse_parameter(left, left_mode)
            < self.parse_parameter(right, right_mode)) else 0)
        return 4

    def equals(self, modes):
        left, right, store = self.get_parameters(1, 4)
        left_mode, right_mode, store_mode = modes
        self.store(store, store_mode, 1 if (
            self.parse_parameter(left, left_mode)
            == self.parse_parameter(right, right_mode)) else 0)
        return 4

    def adjust_relative_base(self, modes):
        parameter = self.get_parameters(1)
        mode, _, _ = modes
        self.relative_base += self.parse_parameter(parameter, mode)
        return 2

    def run_program(self, inputs=None):
        if inputs:
            self.inputs = inputs
        while self.registers[self.instruction_pointer] != self.STOP:
            ip_mod = 0
            instruction = self.registers[self.instruction_pointer]
            opcode = instruction % 100
            modes = generate_modes(instruction)
            if opcode == self.ADD:
                ip_mod = self.add(modes)
            elif opcode == self.MULTIPLY:
                ip_mod = self.multiply(modes)
            elif opcode == self.SAVE_INPUT:
                ip_mod = self.save_input(modes)
            elif opcode == self.OUTPUT:
                ip_mod = self.write_output(modes)
            elif opcode == self.JUMP_IF_TRUE:
                ip_mod = instruction_pointer = self.jump_if_true(modes)
            elif opcode == self.JUMP_IF_FALSE:
                ip_mod = instruction_pointer = self.jump_if_false(modes)
            elif opcode == self.LESS_THAN:
                ip_mod = self.less_than(modes)
            elif opcode == self.EQUALS:
                ip_mod = self.equals(modes)
            elif opcode == self.ADJUST_REL_BASE:
                ip_mod = self.adjust_relative_base(modes)
            else:
                assert False, 'unsupported opcode {opcode} at position {pos}'.format(
                    opcode=opcode,
                    pos=instruction_pointer)
            self.instruction_pointer += ip_mod
        return self.output
