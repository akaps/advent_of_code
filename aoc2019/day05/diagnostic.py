import utils
from aoc2019.int_code import IntCode

INPUTS = [1]
COMPUTER = IntCode('input.txt')
OUTPUT = COMPUTER.run_program(INPUTS)
print(OUTPUT)
