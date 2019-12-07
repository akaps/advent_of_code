import itertools
import utils
from aoc2019.int_code import IntCode

class Amplifiers:
    NUM_AMPLIFIERS = 5

    def __init__(self, file_name):
        self.amplifiers = [IntCode(file_name) for _ in range(self.NUM_AMPLIFIERS)]

    def find_largest_output(self):
        combinations = itertools.permutations(range(5), 5)
        largest_output = None
        for combination in combinations:
            output = 0
            for index, amplifier in enumerate(self.amplifiers):
                phase_setting = combination[index]
                amplifier.reinitialize()
                output = amplifier.run_program([phase_setting, output])[0]
            if not largest_output or output > largest_output:
                largest_output = output
        return largest_output

SAMPLE1 = Amplifiers('sample1.txt')
assert SAMPLE1.find_largest_output() == 43210

SAMPLE2 = Amplifiers('sample2.txt')
assert SAMPLE2.find_largest_output() == 54321

SAMPLE3 = Amplifiers('sample3.txt')
assert SAMPLE3.find_largest_output() == 65210

PROBLEM = Amplifiers('input.txt')
utils.pretty_print_answer(1, PROBLEM.find_largest_output())
