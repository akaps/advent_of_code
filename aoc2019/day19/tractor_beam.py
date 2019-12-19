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
    return '\n'.join(result)

class TractorBeam:
    def __init__(self, input_file):
        self.grid = {}
        self.computer = IntCode(input_file)
        self.fill_grid()

    def fill_grid(self):
        for y_pos in range(50):
            for x_pos in range(50):
                self.computer.reinitialize()
                computer_input = [y_pos, x_pos]
                result = self.computer.run_program(computer_input)
                self.grid[(y_pos, x_pos)] = PULLED if result[0] else STATIONARY

SAMPLE = sample_grid()
assert count_pulled(SAMPLE) == 27

PROBLEM = TractorBeam('input.txt')
ANSWER = count_pulled(PROBLEM.grid)
utils.pretty_print_answer(1, ANSWER)
