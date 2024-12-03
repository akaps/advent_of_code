import re

MUL_REGEX = r'mul\((?P<multiplier>\d+),(?P<multiplicand>\d+)\)'
DO_REGEX = r'do\(\)'
DONT_REGEX = r'don\'t\(\)'
INSTRUCTION_REGEX = r'('+MUL_REGEX+'|'+DO_REGEX+'|'+DONT_REGEX+')'

class Instructions:
    def __init__(self, file_name):
        self.memory = open(file_name, encoding='utf-8').readlines()

    def sum_mult(self):
        total = 0
        for line in self.memory:
            for multiplier, multiplicand in re.findall(MUL_REGEX, line):
                total += int(multiplier) * int(multiplicand)
        return total

    def sum_mult_2(self):
        total = 0
        enabled = True
        for line in self.memory:
            for instruction in re.findall(INSTRUCTION_REGEX, line):
                if 'mul' in instruction[0]:
                    total += int(instruction[1]) * int(instruction[2]) if enabled else 0
                elif 'do()' in instruction[0]:
                    enabled = True
                elif 'don\'t()' in instruction[0]:
                    enabled = False
                else:
                    assert False
        return total

def main():
    sample = Instructions('aoc2024/day03/sample.txt')
    problem = Instructions('aoc2024/day03/input.txt')

    assert sample.sum_mult() == 161
    print('Part 1:', problem.sum_mult())

    sample = Instructions('aoc2024/day03/sample2.txt')
    assert sample.sum_mult_2() == 48
    print('Part 2:', problem.sum_mult_2())

if __name__ == '__main__':
    main()
