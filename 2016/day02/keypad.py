import utils

DIRECTIONS = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

PART_1_KEYS = (('1', '2', '3'), ('4', '5', '6'), ('7', '8', '9'))
PART_1_START = (1, 1)
PART_2_KEYS = (('0', '0', '1', '0', '0'),
               ('0', '2', '3', '4', '0'),
               ('5', '6', '7', '8', '9'),
               ('0', 'A', 'B', 'C', '0'),
               ('0', '0', 'D', '0', '0'))
PART_2_START = (2, 0)

class Keypad:
    def __init__(self, keys, start_pos):
        self.position = start_pos
        self.keys = keys

    def move(self, direction):
        direction = DIRECTIONS[direction]
        if self.in_bounds(self.position, direction):
            self.position = (self.position[0] + direction[0],
                             self.position[1] + direction[1])

    def key(self):
        return self.keys[self.position[0]][self.position[1]]

    def in_bounds(self, position, direction):
        new_pos = (position[0] + direction[0], position[1] + direction[1])
        return (0 <= new_pos[0] < len(self.keys) and
                0 <= new_pos[1] < len(self.keys)) and self.keys[new_pos[0]][new_pos[1]] != '0'

def determine_code(lines, keys, start):
    res = ''
    keypad = Keypad(keys, start)
    for line in lines:
        for instruction in line:
            keypad.move(instruction)
        res += keypad.key()
    return res

SAMPLE = utils.read_lines('sample.txt')
assert determine_code(SAMPLE, PART_1_KEYS, PART_1_START) == '1985'

PROBLEM = utils.read_lines('input.txt')
utils.pretty_print_answer(1, determine_code(PROBLEM, PART_1_KEYS, PART_1_START))

assert determine_code(SAMPLE, PART_2_KEYS, PART_2_START) == '5DB3'
utils.pretty_print_answer(2, determine_code(PROBLEM, PART_2_KEYS, PART_2_START))
