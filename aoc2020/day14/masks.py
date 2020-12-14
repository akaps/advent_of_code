import re
import utils

SET_REGEX = r'mem\[(\d+)\] = (\d+)'
MASK_REGEX = r'mask = ([01X]*)'

class Masker:
    def __init__(self, file_name):
        self.instructions = utils.read_lines(file_name)

    def run(self):
        memory = {}
        mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
        for instruction in self.instructions:
            if re.match(SET_REGEX, instruction):
                groups = re.match(SET_REGEX, instruction).groups()
                memory_address = int(groups[0])
                value = apply_mask(int(groups[1]), mask)
                memory[memory_address] = value
            elif re.match(MASK_REGEX, instruction):
                mask = re.match(MASK_REGEX, instruction).groups()[0]
            else:
                assert False, 'Unsupported instruction {instr}'.format(instr=instruction)
        print(memory)
        return sum(memory.values())

def apply_mask(value, mask):
    binary = list('{val:036b}'.format(val=value))
    for i in range(36):
        if mask[i] != 'X':
            binary[i] = mask[i]
        else:
            assert mask[i] == 'X' or mask[i] == '1', (
                'unexpected mask value {val}'.format(val=mask[i]))
    return int(''.join(binary), 2)

def main():
    mask = Masker('input.txt')
    utils.pretty_print_answer(1, mask.run())

if __name__ == "__main__":
    main()
