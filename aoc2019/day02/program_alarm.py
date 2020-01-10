import utils
from aoc2019.int_code import IntCode

def find_noun_verb(computer, target):
    for noun in range(100):
        for verb in range(100):
            computer.initial_state[1] = noun
            computer.initial_state[2] = verb
            generator = computer.load_program()
            generator.send(None)
            if computer.final_state[0] == target:
                return 100 * noun + verb
    assert False, 'Unreachable'
    return -1

COMPUTER = IntCode('input.txt')
COMPUTER.initial_state[1] = 12
COMPUTER.initial_state[2] = 2
GENERATOR = COMPUTER.load_program()
GENERATOR.send(None)
ANSWER = COMPUTER.final_state[0]
assert ANSWER == 2692315
utils.pretty_print_answer(1, ANSWER)

ANSWER = find_noun_verb(COMPUTER, 19690720)
assert ANSWER == 9507
utils.pretty_print_answer(2, ANSWER)
