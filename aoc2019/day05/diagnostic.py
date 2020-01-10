import utils
from aoc2019.int_code import IntCode

COMPUTER = IntCode('input.txt')
PROGRAM = COMPUTER.load_program()
PROGRAM.send(None)
OUTPUT = PROGRAM.send(1)
print('diagnostic expects all zeroes followed by answer')
assert OUTPUT[-1] == 15259545
utils.pretty_print_answer(1, OUTPUT)

PROGRAM = COMPUTER.load_program()
PROGRAM.send(None)
OUTPUT = PROGRAM.send(5)
assert OUTPUT[0] == 7616021
utils.pretty_print_answer(2, OUTPUT)
