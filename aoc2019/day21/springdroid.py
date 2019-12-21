import utils
from aoc2019.springscript import SpringScript

PROBLEM = SpringScript('input.txt', 'walk_program.txt')
ANSWER = PROBLEM.run()
utils.pretty_print_answer(1, ANSWER)
