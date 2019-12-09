import utils
from aoc2019.int_code import IntCode

SAMPLE_1 = IntCode('sample1.txt')
assert SAMPLE_1.run_program() == [109,
                                  1,
                                  204,
                                  -1,
                                  1001,
                                  100,
                                  1,
                                  100,
                                  1008,
                                  100,
                                  16,
                                  101,
                                  1006,
                                  101,
                                  0,
                                  99]

SAMPLE_2 = IntCode('sample2.txt')
NUMBER = SAMPLE_2.run_program()[0]
assert len(str(NUMBER)) == 16

SAMPLE_3 = IntCode('sample3.txt')
assert SAMPLE_3.run_program()[0] == 1125899906842624

PROBLEM = IntCode('input.txt')
RESULT = PROBLEM.run_program([1])
assert len(RESULT) == 1, 'opcodes failed according to results {res}'.format(res=RESULT)
utils.pretty_print_answer(1, RESULT[0])

PROBLEM.reinitialize()
RESULT = PROBLEM.run_program([2])
assert len(RESULT) == 1, 'unexpected additional output {res}'.format(res=RESULT)
utils.pretty_print_answer(2, RESULT[0])
