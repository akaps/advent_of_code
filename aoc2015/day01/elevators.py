import utils

OPEN_PAREN = '('
CLOSE_PAREN = ')'

class Elevators:
    def __init__(self):
        self.first = 0
        self.bottom = False

    def calculate_floors(self, line):
        floor = 0
        for paren in line:
            if not self.bottom:
                self.first += 1
            if paren == OPEN_PAREN:
                floor += 1
            elif paren == CLOSE_PAREN:
                floor -= 1
            if floor == -1:
                self.bottom = True
        return floor

ELEVATORS = Elevators()
LINES = utils.read_lines('input.txt')
utils.pretty_print_answer(1, ELEVATORS.calculate_floors(LINES[0]))
utils.pretty_print_answer(2, ELEVATORS.first)
