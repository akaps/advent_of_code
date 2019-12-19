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

def sample_grid():
    grid = {}
    grid[(0, 0)] = PULLED
    grid[(1, 0)] = STATIONARY

    grid[(1, 1)] = PULLED

    grid[(2, 2)] = PULLED
    grid[(3, 2)] = PULLED

    grid[(3, 3)] = PULLED
    grid[(4, 3)] = PULLED
    grid[(5, 3)] = PULLED

    grid[(4, 4)] = PULLED
    grid[(5, 4)] = PULLED
    grid[(6, 4)] = PULLED

    grid[(5, 5)] = PULLED
    grid[(6, 5)] = PULLED
    grid[(7, 5)] = PULLED
    grid[(8, 5)] = PULLED

    grid[(6, 6)] = PULLED
    grid[(7, 6)] = PULLED
    grid[(8, 6)] = PULLED
    grid[(9, 6)] = PULLED

    grid[(6, 7)] = PULLED
    grid[(7, 7)] = PULLED
    grid[(8, 7)] = PULLED
    grid[(9, 7)] = PULLED

    grid[(7, 8)] = PULLED
    grid[(8, 8)] = PULLED
    grid[(9, 8)] = PULLED

    grid[(8, 9)] = PULLED
    grid[(9, 9)] = PULLED
    return grid

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
        self.computer.reinitialize()
        computer_input = [y_pos, x_pos]
        is_pulled =  self.computer.run_program(computer_input).pop(0)
        self.grid[(y_pos, x_pos)] = PULLED if is_pulled else STATIONARY
        return is_pulled

    def find_gap(self, size):
        return -1

SAMPLE = sample_grid()
assert count_pulled(SAMPLE) == 27

PROBLEM = TractorBeam('input.txt')
PROBLEM.project_beam(50)
ANSWER = count_pulled(PROBLEM.grid)
assert ANSWER == 206
utils.pretty_print_answer(1, ANSWER)
utils.pretty_print_answer(2, PROBLEM.find_gap(100))
