import re

def generate_modes(instruction):
    modes = [int(x) for x in '{modes:03d}'.format(modes=(instruction // 100))]
    modes.reverse()
    return modes

class IntCodeState:
    def __init__(self, initial_state):
        self.registers = {index: x for index, x in enumerate(initial_state)}
        self.relative_base = 0
        self.instruction_pointer = 0
        self.output = []

    def clear_output(self):
        self.output = []

class IntCode:
    COMMA = r','

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
    STORE_INPUT = 3
    SEND_OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    ADJUST_REL_BASE = 9
    STOP = 99

    def __init__(self, input_file):
        file = open(input_file, 'r')
        self.initial_state = [int(x) for x in re.split(self.COMMA, file.readline().strip())]
        file.close()

    def parse_parameter(self, state, parameter, mode):
        if mode == self.ADDRESS:
            if parameter not in state.registers:
                state.registers[parameter] = 0
            return state.registers[parameter]
        if mode == self.IMMEDIATE:
            return parameter
        if mode == self.RELATIVE:
            adjusted = state.relative_base + parameter
            if adjusted not in state.registers:
                state.registers[adjusted] = 0
            return state.registers[adjusted]
        assert False, 'Unexpected mode {mode}'.format(mode=mode)
        return -1

    def get_parameters(self, state, start, end=None):
        if end:
            return [state.registers[state.instruction_pointer + i] for i in range(start, end)]
        return state.registers[state.instruction_pointer + start]

    def store(self, state, store_pos, store_mode, store_val):
        assert store_mode != self.IMMEDIATE, 'cannot save to an immediate'
        if store_mode == 0:
            state.registers[store_pos] = store_val
        else:
            state.registers[state.relative_base + store_pos] = store_val

    def add(self, state, modes):
        left, right, store = self.get_parameters(state, 1, 4)
        left_mode, right_mode, store_mode = modes
        self.store(state, store, store_mode, (self.parse_parameter(state, left, left_mode)
                                              + self.parse_parameter(state, right, right_mode)))
        return 4

    def multiply(self, state, modes):
        left, right, store = self.get_parameters(state, 1, 4)
        left_mode, right_mode, store_mode = modes
        self.store(state, store, store_mode, (self.parse_parameter(state, left, left_mode)
                                              * self.parse_parameter(state, right, right_mode)))
        return 4

    def store_input(self, state, input_val, modes):
        store = self.get_parameters(state, 1)
        self.store(state, store, modes[0], input_val)
        return 2

    def send_output(self, state, modes):
        immediate, _, _ = modes
        parameter = self.get_parameters(state, 1)
        state.output.append(self.parse_parameter(state, parameter, immediate))
        return 2

    def jump_if_true(self, state, modes):
        non_zero, jump = self.get_parameters(state, 1, 3)
        nz_mode, jmp_mode, _ = modes
        if self.parse_parameter(state, non_zero, nz_mode):
            state.instruction_pointer = self.parse_parameter(state, jump, jmp_mode)
            return 0
        return 3

    def jump_if_false(self, state, modes):
        non_zero, jump = self.get_parameters(state, 1, 3)
        nz_mode, jmp_mode, _ = modes
        if self.parse_parameter(state, non_zero, nz_mode):
            return 3
        state.instruction_pointer = self.parse_parameter(state, jump, jmp_mode)
        return 0

    def less_than(self, state, modes):
        left, right, store = self.get_parameters(state, 1, 4)
        left_mode, right_mode, store_mode = modes
        self.store(state, store, store_mode, 1 if (
            self.parse_parameter(state, left, left_mode)
            < self.parse_parameter(state, right, right_mode)) else 0)
        return 4

    def equals(self, state, modes):
        left, right, store = self.get_parameters(state, 1, 4)
        left_mode, right_mode, store_mode = modes
        self.store(state, store, store_mode, 1 if (
            self.parse_parameter(state, left, left_mode)
            == self.parse_parameter(state, right, right_mode)) else 0)
        return 4

    def adjust_relative_base(self, state, modes):
        parameter = self.get_parameters(state, 1)
        mode, _, _ = modes
        state.relative_base += self.parse_parameter(state, parameter, mode)
        return 2

    def load_program(self):
        state = IntCodeState(self.initial_state)

        while state.registers[state.instruction_pointer] != self.STOP:
            ip_mod = 0
            instruction = state.registers[state.instruction_pointer]
            opcode = instruction % 100
            modes = generate_modes(instruction)
            if opcode == self.ADD:
                ip_mod = self.add(state, modes)
            elif opcode == self.MULTIPLY:
                ip_mod = self.multiply(state, modes)
            elif opcode == self.STORE_INPUT:
                input_val = (yield state.output)
                state.clear_output()
                ip_mod = self.store_input(state, input_val, modes)
            elif opcode == self.SEND_OUTPUT:
                ip_mod = self.send_output(state, modes)
            elif opcode == self.JUMP_IF_TRUE:
                ip_mod = instruction_pointer = self.jump_if_true(state, modes)
            elif opcode == self.JUMP_IF_FALSE:
                ip_mod = instruction_pointer = self.jump_if_false(state, modes)
            elif opcode == self.LESS_THAN:
                ip_mod = self.less_than(state, modes)
            elif opcode == self.EQUALS:
                ip_mod = self.equals(state, modes)
            elif opcode == self.ADJUST_REL_BASE:
                ip_mod = self.adjust_relative_base(state, modes)
            else:
                assert False, 'unsupported opcode {opcode} at position {pos}'.format(
                    opcode=opcode,
                    pos=instruction_pointer)
            state.instruction_pointer += ip_mod
        yield state.output
        yield state.registers
