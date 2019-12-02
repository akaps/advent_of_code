import re

class Intcode:
    #address references
    NOUN = 1
    VERB = 2

    #opcodes
    ADD = 1
    MULTIPLY = 2
    STOP = 99

    def __init__(self, input_file):
        file = open(input_file, 'r')
        self.initial_state = [int(x) for x in re.split(r',', file.readline().strip())]
        file.close()
        self.reinitialize()

    def reinitialize(self):
        self.registers = [x for x in self.initial_state]

    def run_program(self, noun, verb):
        self.registers[self.NOUN] = noun
        self.registers[self.VERB] = verb
        instruction_pointer = 0
        while self.registers[instruction_pointer] != self.STOP:
            ip_mod = 1
            next_instr = self.registers[instruction_pointer]
            if next_instr == self.ADD:
                ip_mod = 4
                parameters = self.registers[instruction_pointer + 1: instruction_pointer + ip_mod]
                self.registers[parameters[2]] = self.registers[parameters[0]] + self.registers[parameters[1]]
            elif next_instr == self.MULTIPLY:
                ip_mod = 4
                parameters = self.registers[instruction_pointer + 1: instruction_pointer + ip_mod]
                self.registers[parameters[2]] = self.registers[parameters[0]] * self.registers[parameters[1]]
            instruction_pointer += ip_mod
        return self.registers[0]
