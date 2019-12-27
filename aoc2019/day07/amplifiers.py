import itertools
from int_code import IntCode, MissingInputError

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

    def is_halted(self, amplifier):
        return amplifier.registers[amplifier.instruction_pointer] == 99

    def initialize_amplifiers(self, combination):
        previous_result = [0]
        for index, phase in enumerate(combination):
            previous_result.insert(0, phase)
            try:
                previous_result = self.amplifiers[index].run_program(previous_result)
            except MissingInputError:
                previous_result = self.amplifiers[index].output
                self.amplifiers[index].output = []
        return previous_result

    def run_feedback_loop(self, combination):
        self.reinitialize_amplifiers()
        previous_result = self.initialize_amplifiers(combination)
        while not self.is_halted(self.amplifiers[-1]):
            for amplifier in self.amplifiers:
                try:
                    previous_result = amplifier.run_program(previous_result)
                except MissingInputError:
                    previous_result = amplifier.output
                    amplifier.output = []
        return previous_result[0]

    def reinitialize_amplifiers(self):
        for amplifier in self.amplifiers:
            amplifier.reinitialize()

    def largest_feedback_loop(self):
        combinations = itertools.permutations(range(5, 10))
        largest_output = None
        for combination in combinations:
            output_val = self.run_feedback_loop(combination)
            if not largest_output or output_val > largest_output:
                largest_output = output_val
        return largest_output

SAMPLE1 = Amplifiers('sample1.txt')
assert SAMPLE1.find_largest_output() == 43210

SAMPLE2 = Amplifiers('sample2.txt')
assert SAMPLE2.find_largest_output() == 54321

SAMPLE3 = Amplifiers('sample3.txt')
assert SAMPLE3.find_largest_output() == 65210

PROBLEM = Amplifiers('input.txt')
print('Answer to part 1:', PROBLEM.find_largest_output())

PROBLEM.reinitialize_amplifiers()
print('Answer to part 2:', PROBLEM.largest_feedback_loop())
