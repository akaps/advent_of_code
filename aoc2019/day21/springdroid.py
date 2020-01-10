import utils
from aoc2019.springscript import SpringScript

PROBLEM = SpringScript('input.txt', 'walk_program.txt')
ANSWER = PROBLEM.run()
assert ANSWER == 19354173
utils.pretty_print_answer(1, ANSWER)

PROBLEM = SpringScript('input.txt', 'run_program.txt')
ANSWER = PROBLEM.run()
assert ANSWER == 1145849660
utils.pretty_print_answer(2, ANSWER)
