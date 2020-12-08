from collections import defaultdict
import re
import utils

ACC = 'acc'
JUMP = 'jmp'
NOP = 'nop'

INSTRUCTION_REGEX = r'(?P<op>acc|jmp|nop) (?P<number>(\+|-)\d+)'
class VM:
    def __init__(self, file_name):
        self.instructions = utils.read_lines(file_name)

    def run_til_repeat(self):
        instruction_pointer = 0
        accumulator = 0
        ips = defaultdict(lambda: False)
        infinite = False
        while instruction_pointer < len(self.instructions) and not ips[instruction_pointer]:
            ips[instruction_pointer] = True
            groups = re.match(INSTRUCTION_REGEX, self.instructions[instruction_pointer]).groups()
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
                    print('operation caused us to repeat', opcode, value)
                    print('repetition found at ', instruction_pointer)
                    infinite = True
        print('furthest point reached', max(ips.keys()))
        return accumulator, infinite

    def find_non_accs(self):
        result = []
        for index, line in enumerate(self.instructions):
            groups = re.match(INSTRUCTION_REGEX, line).groups()
            if groups[0] != ACC:
                result.append((index, line))
        return result

def part_2(virtual_machine):
    non_accs = virtual_machine.find_non_accs()
    non_accs.reverse()
    for index, op in non_accs:
        negation = None
        if JUMP in op:
            negation = op.replace(JUMP, NOP)
        else:
            negation = op.replace(NOP, JUMP)
        virtual_machine.instructions[index] = negation
        answer, infinite = virtual_machine.run_til_repeat()
        if not infinite:
            print('found solution inverting', index, op)
            return answer
        virtual_machine.instructions[index] = op
    return -1

def main():
    virtual_machine = VM('input.txt')
    utils.pretty_print_answer(1, virtual_machine.run_til_repeat()[0])
    utils.pretty_print_answer(2, part_2(virtual_machine))

if __name__ == "__main__":
    main()
