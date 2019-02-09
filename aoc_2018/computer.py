class Computer:
    def __init__(self, num_registers, start_ip, instructions):
        self.registers = [0] * num_registers
        self.ip = start_ip
        self.process_instructions(instructions)

    def process_instructions(self, instructions):
        self.instructions=[]
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
        # print('ip={ip} {reg} {cmd} {after}'.format(
        #     ip=ip,
        #     reg=self.registers,
        #     cmd=command,
        #     after=res
        # ))
        self.registers = res

    @staticmethod
    def addr(command, reg):
        res = list(reg)
        res[command[3]] = res[command[1]] + res[command[2]]
        return res

    @staticmethod
    def addi(command, reg):
        res = list(reg)
        res[command[3]] = res[command[1]] + command[2]
        return res

    @staticmethod
    def mulr(command, reg):
        res = list(reg)
        res[command[3]] = res[command[1]] * res[command[2]]
        return res

    @staticmethod
    def muli(command, reg):
        res = list(reg)
        res[command[3]] = res[command[1]] * command[2]
        return res

    @staticmethod
    def banr(command, reg):
        res = list(reg)
        res[command[3]] = res[command[1]] & res[command[2]]
        return res

    @staticmethod
    def bani(command, reg):
        res = list(reg)
        res[command[3]] = res[command[1]] & command[2]
        return res

    @staticmethod
    def borr(command, reg):
        res = list(reg)
        res[command[3]] = res[command[1]] | res[command[2]]
        return res

    @staticmethod
    def bori(command, reg):
        res = list(reg)
        res[command[3]] = res[command[1]] | command[2]
        return res

    @staticmethod
    def setr(command, reg):
        res = list(reg)
        res[command[3]] = res[command[1]]
        return res

    @staticmethod
    def seti(command, reg):
        res = list(reg)
        res[command[3]] = command[1]
        return res

    @staticmethod
    def gtir(command, reg):
        res = list(reg)
        res[command[3]] = 1 if command[1] > res[command[2]] else 0
        return res

    @staticmethod
    def gtri(command, reg):
        res = list(reg)
        res[command[3]] = 1 if res[command[1]] > command[2] else 0
        return res

    @staticmethod
    def gtrr(command, reg):
        res = list(reg)
        res[command[3]] = 1 if res[command[1]] > res[command[2]] else 0
        return res

    @staticmethod
    def eqir(command, reg):
        res = list(reg)
        res[command[3]] = 1 if command[1] == res[command[2]] else 0
        return res

    @staticmethod
    def eqri(command, reg):
        res = list(reg)
        res[command[3]] = 1 if res[command[1]] == command[2] else 0
        return res

    @staticmethod
    def eqrr(command, reg):
        res = list(reg)
        res[command[3]] = 1 if res[command[1]] == res[command[2]] else 0
        return res
