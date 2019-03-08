import re
import utils
import aoc2018.computer as comp

class Program:
    def __init__(self, file_name):
        file = open(file_name)
        lines = file.readlines()
        file.close()
        self.registers = [0] * 6
        self.ip_index = determine_ip(lines.pop(0))
        self.instructions = parse_lines(lines)

    def run(self):
        while 0 <= self.registers[self.ip_index] < len(self.instructions):
            ip = self.registers[self.ip_index]
            opcode, a, b, c = self.instructions[ip]
            output = comp.execute(opcode, self.registers, a, b, c)
            self.registers = output
            self.registers[self.ip_index] += 1

def determine_ip(line):
    return int(re.search('\d', line).group(0))

def parse_lines(lines):
    res = []
    for line in lines:
        parsed = re.split((r' '), line.strip())
        instruction = (parsed[0], int(parsed[1]), int(parsed[2]), int(parsed[3]))
        res.append(instruction)
    return res

SAMPLE = Program('sample.txt')
SAMPLE.run()
assert SAMPLE.registers[0] == 7

PROBLEM = Program('input.txt')
PROBLEM.run()
utils.pretty_print_answer(1, PROBLEM.registers[0])
