import utils
from aoc2019.int_code import IntCode

def find_noun_verb(computer, target):
    for noun in range(100):
        for verb in range(100):
            COMPUTER.reinitialize()
            COMPUTER.registers[1] = noun
            COMPUTER.registers[2] = verb
            computer.run_program()
            if computer.registers[0] == target:
                return 100 * noun + verb
    assert False, 'Unreachable'
    return -1

COMPUTER = IntCode('input.txt')
COMPUTER.registers[1] = 12
COMPUTER.registers[2] = 2
COMPUTER.run_program()
ANSWER = COMPUTER.registers[0]
assert ANSWER == 2692315
utils.pretty_print_answer(1, ANSWER)

ANSWER = find_noun_verb(COMPUTER, 19690720)
assert ANSWER == 9507
utils.pretty_print_answer(2, ANSWER)
