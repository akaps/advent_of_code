import utils
from aoc2019.int_code import IntCode

SCAFFOLD = '#'

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Scaffold:
    def __init__(self, input_file):
        self.computer = IntCode(input_file)
        self.generate_map()

    def generate_map(self):
        self.map = []
        row = []
        for val in [chr(x) for x in self.computer.run_program()]:
            if val != '\n':
                row.append(val)
            elif row:
                self.map.append(row)
                row = []

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

    def __repr__(self):
        result = []
        for row in self.map:
            row_result = []
            for val in row:
                row_result.append(val)
            result.append(''.join(row_result))
        return '\n'.join(result)

PROBLEM = Scaffold('input.txt')
print(PROBLEM)
utils.pretty_print_answer(1, PROBLEM.find_intersections())
