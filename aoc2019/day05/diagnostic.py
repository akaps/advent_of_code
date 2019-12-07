import utils
from aoc2019.int_code import IntCode

INPUTS = [1]
COMPUTER = IntCode('input.txt')
OUTPUT = COMPUTER.run_program(INPUTS)
print('diagnostic expects all zeroes followed by answer')
assert OUTPUT[-1] == 15259545
utils.pretty_print_answer(1, OUTPUT)

BRANCH_SAMPLE = IntCode('branch_sample1.txt')
assert BRANCH_SAMPLE.run_program([8])[0] == 1
BRANCH_SAMPLE.reinitialize()
assert BRANCH_SAMPLE.run_program([12])[0] == 0

BRANCH_SAMPLE = IntCode('branch_sample2.txt')
assert BRANCH_SAMPLE.run_program([4])[0] == 1
BRANCH_SAMPLE.reinitialize()
assert BRANCH_SAMPLE.run_program([12])[0] == 0

BRANCH_SAMPLE = IntCode('branch_sample3.txt')
assert BRANCH_SAMPLE.run_program([8])[0] == 1
BRANCH_SAMPLE.reinitialize()
assert BRANCH_SAMPLE.run_program([20])[0] == 0

BRANCH_SAMPLE = IntCode('branch_sample4.txt')
assert BRANCH_SAMPLE.run_program([-13])[0] == 1
BRANCH_SAMPLE.reinitialize()
assert BRANCH_SAMPLE.run_program([26])[0] == 0

JUMP_SAMPLE = IntCode('jump_sample1.txt')
assert JUMP_SAMPLE.run_program([31])[0] == 1
JUMP_SAMPLE.reinitialize()
assert JUMP_SAMPLE.run_program([0])[0] == 0

JUMP_SAMPLE = IntCode('jump_sample2.txt')
assert JUMP_SAMPLE.run_program([96])[0] == 1
JUMP_SAMPLE.reinitialize()
assert JUMP_SAMPLE.run_program([0])[0] == 0

COMPUTER.reinitialize()
INPUTS = [5]
OUTPUT = COMPUTER.run_program(INPUTS)
assert OUTPUT[0] == 7616021
utils.pretty_print_answer(2, OUTPUT)
