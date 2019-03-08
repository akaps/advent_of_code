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

def execute(opcode, reg, a, b, c):
    new_reg = list(reg)
    new_reg[c] = INSTRUCTIONS[opcode](reg, a, b)
    return new_reg
