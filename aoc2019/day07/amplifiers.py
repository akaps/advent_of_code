import itertools
from collections import defaultdict
from aoc2019.int_code import IntCode

class Amplifiers:
    NUM_AMPLIFIERS = 5
    LAST = 4

    def __init__(self, file_name):
        self.amplifiers = [IntCode(file_name) for _ in range(self.NUM_AMPLIFIERS)]

    def find_largest_output(self):
        combinations = itertools.permutations(range(5), 5)
        largest_output = None
        for combination in combinations:
            output = 0
            for index, amplifier in enumerate(self.amplifiers):
                phase_setting = combination[index]
                program = amplifier.load_program()
                program.send(None)
                program.send(phase_setting)
                output = program.send(output)[0]
            if not largest_output or output > largest_output:
                largest_output = output
        return largest_output

    def initialize_programs(self, combination):
        programs = []
        for index, amplifier in enumerate(self.amplifiers):
            next_program = amplifier.load_program()
            next_program.send(None)
            next_program.send(combination[index])
            programs.append(next_program)
        return programs

    def run_feedback_loop(self, combination):
        programs = self.initialize_programs(combination)
        results = defaultdict(lambda: [0])
        while True:
            try:
                for index, program in enumerate(programs):
                    prev_index = (index + self.NUM_AMPLIFIERS - 1) % self.NUM_AMPLIFIERS
                    result = None
                    for result_val in results[prev_index]:
                        result = program.send(result_val)
                    assert result
                    results[index] = result
            except StopIteration:
                break
        return results[self.LAST][0]

    def largest_feedback_loop(self):
        combinations = itertools.permutations(range(5, 10))
        largest_output = None
        for combination in combinations:
            output_val = self.run_feedback_loop(combination)
            if not largest_output or output_val > largest_output:
                largest_output = output_val
        return largest_output

def main():
    problem = Amplifiers('input.txt')
    print('Answer to part 1:', problem.find_largest_output())
    print('Answer to part 2:', problem.largest_feedback_loop())

if __name__ == '__main__':
    main()
