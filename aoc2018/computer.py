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

class Computer:
    def __init__(self, num_registers, start_ip, program):
        self.registers = [0] * num_registers
        self.ip = start_ip
        self.process_program(program)

    def process_program(self, instructions):
        for instruction in instructions:
            instruction = instruction.split()
            for i in range(1, 4):
                instruction[i] = int(instruction[i])
            self.instructions.append(instruction)

    def run(self):
        while self.registers[0] < len(self.instructions):
            self.do_instruction(self.registers[0])
            self.registers[0] += 1

    def do_instruction(self, ip):
        command = self.instructions[ip]
        cmd = getattr(self, command[0])
        res = cmd(command, self.registers)
        self.registers = res
