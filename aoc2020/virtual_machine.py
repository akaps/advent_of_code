import re
import utils

ACC = 'acc'
JUMP = 'jmp'
NOP = 'nop'

OPCODE = 'opcode'
ARGUMENT = 'value'

INSTRUCTION_REGEX = r'(?P<op>acc|jmp|nop) (?P<number>(\+|-)\d+)'

class VirtualMachine:
    def __init__(self, file_name):
        lines = utils.read_lines(file_name)
        self.instructions = []
        for line in lines:
            match = re.match(INSTRUCTION_REGEX, line)
            assert match
            opcode = match.groups()[0]
            value = int(match.groups()[1])
            self.instructions.append({OPCODE: opcode, ARGUMENT: value})

    def execute(self, instruction, accumulator, instruction_pointer):
        opcode = instruction[OPCODE]
        value = instruction[ARGUMENT]
        if opcode == ACC:
            accumulator += value
            instruction_pointer += 1
        elif opcode == JUMP:
            instruction_pointer += value
        elif opcode == NOP:
            instruction_pointer += 1
        else:
            assert False, 'Unexpected opcode {opcode}'.format(opcode=opcode)
        return accumulator, instruction_pointer

    def run(self, accumulator=0, start_ip=0):
        instruction_pointer = start_ip
        while instruction_pointer < len(self.instructions):
            next_instruction = self.instructions[instruction_pointer]
            accumulator, instruction_pointer = self.execute(
                next_instruction, accumulator, instruction_pointer)
        return accumulator
