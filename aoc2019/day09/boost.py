import utils
from aoc2019.int_code import IntCode

COMPUTER = IntCode('input.txt')
PROGRAM = COMPUTER.load_program()
PROGRAM.send(None)
RESULT = PROGRAM.send(1)
assert len(RESULT) == 1, 'opcodes failed according to results {res}'.format(res=RESULT)
utils.pretty_print_answer(1, RESULT[0])

PROGRAM = COMPUTER.load_program()
PROGRAM.send(None)
RESULT = PROGRAM.send(2)
assert len(RESULT) == 1, 'unexpected additional output {res}'.format(res=RESULT)
utils.pretty_print_answer(2, RESULT[0])
