import re
from copy import deepcopy
import utils

INT_WIDTH = 36
DEFAULT_MASK = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
SET_REGEX = r'mem\[(\d+)\] = (\d+)'
MASK_REGEX = r'mask = ([01X]*)'

class Masker:
    def __init__(self, file_name):
        self.instructions = utils.read_lines(file_name)

    def run(self):
        memory = {}
        mask = DEFAULT_MASK
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
        mask = DEFAULT_MASK
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
    addresses = [list(convert_to_binary(value))]
    for i in range(INT_WIDTH):
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
        result.append(convert_to_int(address))
    return result

def apply_mask(value, mask):
    binary = convert_to_binary(value)
    for i in range(INT_WIDTH):
        if mask[i] != 'X':
            binary[i] = mask[i]
        else:
            assert mask[i] == 'X' or mask[i] == '1', (
                'unexpected mask value {val}'.format(val=mask[i]))
    return convert_to_int(binary)

def convert_to_binary(value):
    return list('{val:036b}'.format(val=value))

def convert_to_int(value):
    return int(''.join(value), 2)

def main():
    mask = Masker('input.txt')
    utils.pretty_print_answer(1, mask.run())
    utils.pretty_print_answer(2, mask.run_v2())

if __name__ == "__main__":
    main()
