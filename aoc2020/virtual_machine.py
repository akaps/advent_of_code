import re
import utils

ACC = 'acc'
JUMP = 'jmp'
NOP = 'nop'

OPCODE = 'opcode'
ARGUMENT = 'value'

INSTRUCTION_REGEX = r'(?P<op>acc|jmp|nop) (?P<number>(\+|-)\d+)'

def execute(instruction, vm_state):
    opcode = instruction[OPCODE]
    value = instruction[ARGUMENT]
    if opcode == ACC:
        vm_state.accumulator += value
        vm_state.instruction_pointer += 1
    elif opcode == JUMP:
        vm_state.instruction_pointer += value
    elif opcode == NOP:
        vm_state.instruction_pointer += 1
    else:
        assert False, 'Unexpected opcode {opcode}'.format(opcode=opcode)
    return vm_state

class VmState:
    def __init__(self, accumulator=0, instruction_pointer=0):
        self.accumulator = accumulator
        self.instruction_pointer = instruction_pointer

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

    def run(self, accumulator=0, start_ip=0):
        vm_state = VmState(accumulator, start_ip)
        while vm_state.instruction_pointer < len(self.instructions):
            next_instruction = self.instructions[vm_state.instruction_pointer]
            vm_state = execute(next_instruction, vm_state)
        return vm_state.accumulator
