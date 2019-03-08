import utils
import aoc2018.processor as processor

SAMPLE = processor.Program('sample.txt')
SAMPLE.run()
assert SAMPLE.registers[0] == 7

PROBLEM = processor.Program('input.txt')
PROBLEM.run()
utils.pretty_print_answer(1, PROBLEM.registers[0])

PROBLEM.registers = [1, 0, 0, 0, 0, 0]
PROBLEM.run()
utils.pretty_print_answer(2, PROBLEM.registers[0])
