import math
import re
import numpy
import utils

MIN = 'min'
MAX = 'max'

STILL = '~'
RUNNING = '|'
WALL = '#'
EMPTY = '.'
ROW = 'y'
COL = 'x'

class Buckets:
    def __init__(self, file_name):
        file = open(file_name)
        lines = file.readlines()
        file.close()
        self.bounds = find_bounds(lines)
        self.dims = {
            ROW: self.bounds[ROW][MAX] - self.bounds[ROW][MIN] + 1,
            COL: self.bounds[COL][MAX] - self.bounds[COL][MIN] + 1
        }
        self.cells = numpy.full((self.dims[ROW], self.dims[COL]), EMPTY)
        self.process_lines(lines)

    def process_lines(self, lines):
        for line in lines:
            coords = generate_coordinates(line)
            for row, col in coords:
                row -= self.bounds[ROW][MIN]
                col -= self.bounds[COL][MIN]
                self.cells[row][col] = WALL

    def pour(self):
        spills = [(0, 500 - self.bounds[COL][MIN])]
        while spills:
            spill_row, spill_col = spills.pop()
            if self.cells[spill_row][spill_col] == EMPTY:
                print('waterfalling on col', spill_col)
                spills.append(self.waterfall(spill_row, spill_col))
            elif spill_row + 1 < self.dims[ROW]:
                print('filling row', spill_row)
                spills.extend(self.fill_row(spill_row, spill_col))

    def fill_row(self, row, col):
        spills = []
        for new_col in [self.fill_in_direction(row, col, direction) for direction in [-1, 1]]:
            if self.cells[row + 1][new_col] == EMPTY:
                spills.append((row, new_col))
        if not spills:
            spills.append((row - 1, col))
        return spills

    def fill_in_direction(self, row, col, direction):
        while self.cells[row][col] != WALL and self.cells[row + 1][col] != EMPTY:
            self.cells[row][col] = STILL
            col += direction
        return col

    def waterfall(self, row, col):
        while row + 1 < len(self.cells) and self.cells[row + 1][col] == EMPTY:
            self.cells[row][col] = RUNNING
            row += 1
        self.cells[row][col] = RUNNING
        return (row, col)

    def count_water(self):
        total = 0
        for row in self.cells:
            for cell in row:
                if cell in [RUNNING, STILL]:
                    total += 1
        return total

    def __repr__(self):
        res = []
        for row in self.cells:
            res_row = []
            for cell in row:
                res_row.append(cell)
            res.append(''.join(res_row))
        return '\n'.join(res)

def normalize_line(line):
    regex = r'(\w)=(\d+), (\w)=(\d+)(?=..(\d+))?'
    match = re.search(regex, line)
    normalized = (
        [int(d) if d.isdigit() else d for d in match.groups()])
    return normalized

def generate_coordinates(line):
    res = []
    point, point_val, _, dir_start, dir_end = normalize_line(line)
    for i in range(dir_start, dir_end + 1):
        if point == ROW:
            res.append((point_val, i))
        else:
            res.append((i, point_val))
    return res

def find_bounds(lines):
    res = {
        ROW: {
            MIN: math.inf,
            MAX: -math.inf},
        COL: {
            MIN: math.inf,
            MAX: -math.inf}
        }
    for line in lines:
        point, point_val, direction, dir_start, dir_end = normalize_line(line)
        res[point][MIN] = min(res[point][MIN], point_val)
        res[point][MAX] = max(res[point][MAX], point_val)
        res[direction][MIN] = min(res[direction][MIN], dir_start)
        res[direction][MAX] = max(res[direction][MAX], dir_end)
    res[COL][MIN] -= 1
    res[COL][MAX] += 1
    return res

SAMPLE = Buckets('sample.txt')
SAMPLE.pour()
print(SAMPLE)
assert SAMPLE.count_water() == 57
PROBLEM = Buckets('input.txt')
PROBLEM.pour()
print(PROBLEM)
utils.pretty_print_answer(1, PROBLEM.count_water())
