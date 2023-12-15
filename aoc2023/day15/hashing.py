import re

EQUALS = '='
DASH = '-'

INSTRUCTION_REGEX = r'([a-z]*)(-|=\d+)'

def determine_hash(input:str) -> int:
    current = 0
    for char in input:
        current += ord(char)
        current *= 17
        current %= 256
    return current

class Lens:
    def __init__(self, label, focal_length):
        self.label = label
        self.focal_length = focal_length

class InitializationSequence:
    def __init__(self, file_name):
        line = open(file_name, encoding='utf-8').readline().strip()
        self.instructions = line.split(',')

    def sum_hashes(self):
        total = 0
        for instruction in self.instructions:
            total += determine_hash(instruction)
        return total

    def map_hashes(self):
        boxes = [[] for i in range(256)]
        for instruction in self.instructions:
            label, operand = re.match(INSTRUCTION_REGEX, instruction).groups()
            box = boxes[determine_hash(label)]
            if EQUALS in operand:
                focal_length = int(operand[1:])
                if label not in [lens.label for lens in box]:
                    box.append(Lens(label, focal_length))
                else:
                    for lens in box:
                        if lens.label == label:
                            lens.focal_length = focal_length
                            break
            elif operand == DASH and label in [lens.label for lens in box]:
                index = [lens.label for lens in box].index(label)
                box.pop(index)
        return boxes

    def focusing_power(self):
        boxes = self.map_hashes()
        total = 0
        for box_index, box in enumerate(boxes):
            for lens_index, lens in enumerate(box):
                total += (box_index + 1) * (lens_index + 1) * lens.focal_length
        return total

def main():
    assert determine_hash('HASH') == 52
    sample = InitializationSequence('aoc2023/day15/sample.txt')
    assert sample.sum_hashes() == 1320

    problem = InitializationSequence('aoc2023/day15/input.txt')
    print('Answer to Part 1:', problem.sum_hashes())

    assert determine_hash('rn') == 0
    assert sample.focusing_power() == 145
    print('Answer to Part 2:', problem.focusing_power())

if __name__ == '__main__':
    main()
