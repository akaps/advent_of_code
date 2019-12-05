import utils
from aoc2019.int_code import Intcode

def find_noun_verb(computer, target):
    for noun in range(100):
        for verb in range(100):
            COMPUTER.reinitialize()
            COMPUTER.registers[1] = noun
            COMPUTER.registers[2] = verb
            if computer.run_program() == target:
                return 100 * noun + verb
    assert False, 'Unreachable'
    return -1

COMPUTER = Intcode('input.txt')
COMPUTER.registers[1] = 12
COMPUTER.registers[2] = 2
ANSWER = COMPUTER.run_program()
assert ANSWER == 2692315
utils.pretty_print_answer(1, ANSWER)

ANSWER = find_noun_verb(COMPUTER, 19690720)
assert ANSWER == 9507
utils.pretty_print_answer(2, ANSWER)
