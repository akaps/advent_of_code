import re
from aoc_2018.computer import Computer

class Registers:
    def __init__(self, ip, instr):
        self.registers = [0] * 6
        self.registers[0] = ip
        self.instructions = instr

    def do_instruction(self, instruction):
        operation = re.split(' ', instruction)
        for i in range(1, 6):
            operation[i] = int(operation[i])
        operation[0](operation[1:])

def process_input(file_name):
    file = open(file_name, 'r')
    ip = int(re.findall('\d', file.readline())[0])
    instructions = file.readlines()
    file.close()
    computer = Computer(6, ip, instructions) 
    computer.run()
    return computer.registers[0]

answer = process_input('sample.txt')
assert answer == 7

answer = process_input('input.txt')
print('Part 1 answer: {ans}'.format(ans=answer))
