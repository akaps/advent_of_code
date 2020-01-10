import utils
from aoc2019.int_code import IntCode

PULLED = '#'
STATIONARY = '.'

def count_pulled(grid):
    total = 0
    for val in grid.values():
        if val == PULLED:
            total += 1
    return total

def pretty_print_grid(grid):
    x_max = max([key[0] for key in grid])
    y_max = max([key[0] for key in grid])
    result = []
    for y_pos in range(y_max):
        row = []
        for x_pos in range(x_max):
            point = (y_pos, x_pos)
            if point in grid:
                row.append(grid[point])
            else:
                row.append(STATIONARY)
        result.append(''.join(row))
    print('\n'.join(result))

class TractorBeam:
    def __init__(self, input_file):
        self.grid = {}
        self.computer = IntCode(input_file)

    def project_beam(self, distance):
        y_top = 0
        for x_pos in range(distance):
            while not self.evaluate_position(y_top, x_pos) and y_top < x_pos:
                y_top += 1
            y_runner = y_top + 1
            while self.evaluate_position(y_runner, x_pos):
                y_runner += 1

    def evaluate_position(self, y_pos, x_pos):
        program = self.computer.load_program()
        program.send(None)
        program.send(y_pos)
        is_pulled = program.send(x_pos)[0]
        self.grid[(y_pos, x_pos)] = PULLED if is_pulled else STATIONARY
        return is_pulled

    def find_gap(self, size):
        return -1

def main():
    problem = TractorBeam('input.txt')
    problem.project_beam(50)
    answer = count_pulled(problem.grid)
    assert answer == 206
    utils.pretty_print_answer(1, answer)
    utils.pretty_print_answer(2, problem.find_gap(100))

if __name__ == '__main__':
    main()
