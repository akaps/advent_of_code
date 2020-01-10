import utils
from aoc2019.int_code import IntCode

SCAFFOLD = '#'

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def generate_grid(char_map):
    grid = []
    row = []
    for val in [chr(x) for x in char_map]:
        if val != '\n':
            row.append(val)
        elif row:
            grid.append(row)
            row = []
    return grid

def pretty_print_grid(grid):
    result = []
    for row in grid:
        row_result = []
        for val in row:
            row_result.append(val)
        result.append(''.join(row_result))
    print('\n'.join(result))

class Scaffold:
    def __init__(self, input_file):
        self.computer = IntCode(input_file)
        program = self.computer.load_program()
        self.map = generate_grid(program.send(None))

    def in_bounds(self, x_index, y_index):
        return (0 <= y_index < len(self.map)
                and 0 <= x_index < len(self.map[0]))

    def is_intersection(self, x_index, y_index):
        directions = [UP, DOWN, LEFT, RIGHT]
        for delta_x, delta_y in directions:
            adj_x = x_index + delta_x
            adj_y = y_index + delta_y
            if not self.in_bounds(adj_x, adj_y) or self.map[adj_y][adj_x] != SCAFFOLD:
                return False
        return True

    def find_intersections(self):
        total = 0
        for y_index, row in enumerate(self.map):
            for x_index, val in enumerate(row):
                if val == SCAFFOLD and self.is_intersection(x_index, y_index):
                    total += y_index * x_index
        return total

PROBLEM = Scaffold('input.txt')
ANSWER = PROBLEM.find_intersections()
assert ANSWER == 4408
utils.pretty_print_answer(1, ANSWER)

#waking up robot
assert PROBLEM.computer.initial_state[0] == 1
PROBLEM.computer.initial_state[0] = 2

#answers from robot_program.txt
MAIN = 'C,B,B,C,A,C,C,A,B,A\n'
SUBROUTINE_A = 'R,8,L,8,L,8,R,8,R,10\n'
SUBROUTINE_B = 'R,12,L,8,R,10\n'
SUBROUTINE_C = 'R,8,L,12,R,8\n'
CONTINUOUS_MODE = 'n\n'
INPUT = MAIN + SUBROUTINE_A + SUBROUTINE_B + SUBROUTINE_C + CONTINUOUS_MODE
PROGRAM = PROBLEM.computer.load_program()
GRID = PROGRAM.send(None)
for char in INPUT:
    GRID = PROGRAM.send(ord(char))
pretty_print_grid(generate_grid(GRID))
utils.pretty_print_answer(2, GRID[-1])
