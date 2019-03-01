class Jumps:
    def __init__(self, file_name):
        file = open(file_name)
        self.instructions = [int(x.strip()) for x in file.readlines()]
        file.close()

def run(jumps, is_part2=False):
    instructions = list(jumps.instructions)
    instruction_pointer = 0
    steps = 0
    while 0 <= instruction_pointer < len(instructions):
        jump = instructions[instruction_pointer]
        if is_part2 and jump >= 3:
            instructions[instruction_pointer] -= 1
        else:
            instructions[instruction_pointer] += 1
        instruction_pointer += jump
        steps += 1
    return steps

SAMPLE = Jumps('sample.txt')
assert run(SAMPLE, False) == 5
assert run(SAMPLE, True) == 10

PROBLEM = Jumps('input.txt')
print('Answer to part 1: {ans}'.format(ans=run(PROBLEM, False)))
print('Answer to part 2: {ans}'.format(ans=run(PROBLEM, True)))
