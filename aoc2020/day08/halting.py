from collections import defaultdict
import copy
import utils
from aoc2020.virtual_machine import VirtualMachine, JUMP, NOP, ACC, OPCODE

def run_til_repeat(virtual_machine):
    instruction_pointer = 0
    accumulator = 0
    ips = defaultdict(lambda: False)
    infinite = False
    while instruction_pointer < len(virtual_machine.instructions) and not ips[instruction_pointer]:
        ips[instruction_pointer] = True
        instruction = virtual_machine.instructions[instruction_pointer]
        accumulator, instruction_pointer = virtual_machine.execute(
            instruction, accumulator, instruction_pointer)
        if instruction_pointer in ips:
            infinite = True
    return accumulator, infinite

def find_non_accs(instructions):
    result = []
    for index, instruction in enumerate(instructions):
        if instruction[OPCODE] != ACC:
            result.append((index, instruction))
    return result

def part_2(virtual_machine):
    old_instructions = copy.deepcopy(virtual_machine.instructions)
    non_accs = find_non_accs(virtual_machine.instructions)
    non_accs.reverse()
    for index, instruction in non_accs:
        modified_instructions = copy.deepcopy(virtual_machine.instructions)
        if JUMP in instruction[OPCODE]:
            modified_instructions[index][OPCODE] = NOP
        elif NOP in instruction[OPCODE]:
            modified_instructions[index][OPCODE] = JUMP
        else:
            assert False, 'Unexpected opcode {op}'.format(op=instruction)
        virtual_machine.instructions = modified_instructions
        answer, infinite = run_til_repeat(virtual_machine)
        if not infinite:
            print('found solution inverting', index, instruction)
            return answer
        virtual_machine.instructions = old_instructions
    assert False, 'Did not find answer to part 2'
    return -1

def main():
    virtual_machine = VirtualMachine('aoc2020/day08/input.txt')
    utils.pretty_print_answer(1, run_til_repeat(virtual_machine)[0])
    utils.pretty_print_answer(2, part_2(virtual_machine))

if __name__ == "__main__":
    main()
