from collections import defaultdict
import re
import copy
import utils

ACC = 'acc'
JUMP = 'jmp'
NOP = 'nop'

INSTRUCTION_REGEX = r'(?P<op>acc|jmp|nop) (?P<number>(\+|-)\d+)'

def run_til_repeat(instructions, debug=False):
    instruction_pointer = 0
    accumulator = 0
    ips = defaultdict(lambda: False)
    infinite = False
    while instruction_pointer < len(instructions) and not ips[instruction_pointer]:
        ips[instruction_pointer] = True
        groups = re.match(INSTRUCTION_REGEX, instructions[instruction_pointer]).groups()
        opcode = groups[0]
        value = int(groups[1])
        if opcode == ACC:
            accumulator += value
            instruction_pointer += 1
        elif opcode == JUMP:
            instruction_pointer += value
        elif opcode == NOP:
            instruction_pointer += 1
        else:
            assert False, 'Unexpected opcode {opcode}'.format(opcode=opcode)
        if instruction_pointer in ips:
                infinite = True
                if debug:
                    print('operation caused us to repeat', opcode, value)
                    print('repetition found at ', instruction_pointer)
    if debug:
        print('furthest point reached', max(ips.keys()))
    return accumulator, infinite

def find_non_accs(instructions):
    result = []
    for index, line in enumerate(instructions):
        groups = re.match(INSTRUCTION_REGEX, line).groups()
        if groups[0] != ACC:
            result.append((index, line))
    return result

def part_2(instructions, debug=False):
    non_accs = find_non_accs(instructions)
    non_accs.reverse()
    for index, opcode in non_accs:
        modified_instructions = copy.deepcopy(instructions)
        if JUMP in opcode:
            modified_instructions[index] = opcode.replace(JUMP, NOP)
        else:
            modified_instructions[index] = opcode.replace(NOP, JUMP)
        answer, infinite = run_til_repeat(modified_instructions, debug)
        if not infinite:
            print('found solution inverting', index, opcode)
            return answer
    assert False, 'Did not find answer to parat 2'
    return -1

def main():
    instructions = utils.read_lines('input.txt')
    utils.pretty_print_answer(1, run_til_repeat(instructions)[0])
    utils.pretty_print_answer(2, part_2(instructions))

if __name__ == "__main__":
    main()
