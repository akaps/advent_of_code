import re
from copy import deepcopy
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
        return sum(memory.values())

    def run_v2(self):
        memory = {}
        mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
        for instruction in self.instructions:
            if re.match(SET_REGEX, instruction):
                groups = re.match(SET_REGEX, instruction).groups()
                memory_addresses = apply_mask_v2(int(groups[0]), mask)
                value = int(groups[1])
                for address in memory_addresses:
                    memory[address] = value
            elif re.match(MASK_REGEX, instruction):
                mask = re.match(MASK_REGEX, instruction).groups()[0]
            else:
                assert False, 'Unsupported instruction {instr}'.format(instr=instruction)
        return sum(memory.values())

def apply_mask_v2(value, mask):
    addresses = [list('{val:036b}'.format(val=value))]
    for i in range(36):
        if mask[i] == '1':
            for address in addresses:
                address[i] = '1'
        elif mask[i] == 'X':
            new_addresses = []
            for address in addresses:
                address[i] = '1'
                dupe_address = deepcopy(address)
                dupe_address[i] = '0'
                new_addresses.append(dupe_address)
            addresses.extend(new_addresses)
        else:
            assert mask[i] == '0', 'unexpected val {val}'.format(val=mask[i])
    result = []
    for address in addresses:
        result.append(int(''.join(address), 2))
    return result

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
    utils.pretty_print_answer(2, mask.run_v2())

if __name__ == "__main__":
    main()
