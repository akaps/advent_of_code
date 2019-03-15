import re

INSTRUCTIONS = {'addr' : lambda regs, a, b: regs[a] + regs[b],
                'addi' : lambda regs, a, b: regs[a] + b,
                'mulr' : lambda regs, a, b: regs[a] * regs[b],
                'muli' : lambda regs, a, b: regs[a] * b,
                'banr' : lambda regs, a, b: regs[a] & regs[b],
                'bani' : lambda regs, a, b: regs[a] & b,
                'borr' : lambda regs, a, b: regs[a] | regs[b],
                'bori' : lambda regs, a, b: regs[a] | b,
                'setr' : lambda regs, a, b: regs[a],
                'seti' : lambda regs, a, b: a,
                'gtir' : lambda regs, a, b: 1 if a > regs[b] else 0,
                'gtri' : lambda regs, a, b: 1 if regs[a] > b else 0,
                'gtrr' : lambda regs, a, b: 1 if regs[a] > regs[b] else 0,
                'eqir' : lambda regs, a, b: 1 if a == regs[b] else 0,
                'eqri' : lambda regs, a, b: 1 if regs[a] == b else 0,
                'eqrr' : lambda regs, a, b: 1 if regs[a] == regs[b] else 0}

class Program:
    def __init__(self, file_name):
        file = open(file_name)
        lines = file.readlines()
        file.close()
        self.registers = [0] * 6
        self.ip_index = determine_ip(lines.pop(0))
        self.instructions = parse_lines(lines)

    def run(self, debug=False):
        while 0 <= self.registers[self.ip_index] < len(self.instructions):
            ip = self.registers[self.ip_index]
            opcode, a, b, c = self.instructions[ip]
            output = execute(opcode, self.registers, a, b, c)
            if debug:
                print('{ip}: {input} -> {instr} -> {output}'.format(ip=ip,
                                                                    input=self.registers,
                                                                    instr=self.instructions[ip],
                                                                    output=output))
            self.registers = output
            self.registers[self.ip_index] += 1

def execute(opcode, reg, a, b, c):
    new_reg = list(reg)
    new_reg[c] = INSTRUCTIONS[opcode](reg, a, b)
    return new_reg

def determine_ip(line):
    return int(re.search(r'\d', line).group(0))

def parse_lines(lines):
    res = []
    for line in lines:
        parsed = re.split((r' '), line.strip())
        instruction = (parsed[0], int(parsed[1]), int(parsed[2]), int(parsed[3]))
        res.append(instruction)
    return res
