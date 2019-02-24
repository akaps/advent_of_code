import utils

DIRECTIONS = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

class Keypad:
    def __init__(self):
        self.position = (1, 1)
        self.keys = (('1', '2', '3'), ('4', '5', '6'), ('7', '8', '9'))

    def move(self, direction):
        direction = DIRECTIONS[direction]
        if in_bounds(self.position, direction):
            self.position = (self.position[0] + direction[0],
                             self.position[1] + direction[1])

    def key(self):
        print(self.position)
        return self.keys[self.position[0]][self.position[1]]

def in_bounds(position, direction):
    new_pos = (position[0] + direction[0], position[1] + direction[1])
    return (0 <= new_pos[0] < 3 and
            0 <= new_pos[1] < 3)

def determine_code(lines):
    res = ''
    keypad = Keypad()
    for line in lines:
        for instruction in line:
            keypad.move(instruction)
        res += keypad.key()
    return res

SAMPLE = utils.read_lines('sample.txt')
assert determine_code(SAMPLE) == '1985'

PROBLEM = utils.read_lines('input.txt')
utils.pretty_print_answer(1, determine_code(PROBLEM))
