import math
import numpy

#reminder: top-left is 1, 1. x, y notation
class Cells:
    def __init__(self, serial, size):
        self.serial = serial
        self.cells = numpy.fromfunction(self.cell_val, (size, size), dtype=int)

    def cell_val(self, row, col):
        return calculate_cell(row, col, self.serial)

    def find_most_power_for_size(self, size):
        sums = sum(self.cells[x:x - size + 1 or None, y:y - size + 1 or None]
                  for x in range(size) for y in range(size))
        maximum = sums.max()
        indexes = numpy.where(sums == maximum)
        max_row, max_col = indexes[0][0], indexes[1][0]
        return max_row, max_col, maximum

    def find_most_power(self):
        max_x, max_y, max_power, max_size = -1, -1, -math.inf, -1
        for size in range(1, 50):
            row, col, power = self.find_most_power_for_size(size)
            if power > max_power:
                max_x, max_y, max_power, max_size = row, col, power, size
        return max_x, max_y, max_power, max_size

    def __repr__(self):
        result = []
        for row in self.cells:
            result.append(' '.join([str(x) for x in row]))
        return '\n'.join(result)

def calculate_cell(row, col, serial):
    return ((col * (row + 10) + serial) * (row + 10) // 100 % 10) - 5

assert calculate_cell(3, 5, 8) == 4
assert calculate_cell(122, 79, 57) == -5
assert calculate_cell(217, 196, 39) == 0
assert calculate_cell(101, 153, 71) == 4

GRID_18 = Cells(18, 300)
X, Y, POWER = GRID_18.find_most_power_for_size(3)
assert X == 33
assert Y == 45
assert POWER == 29

GRID_42 = Cells(42, 300)
X, Y, POWER = GRID_42.find_most_power_for_size(3)
assert X == 21
assert Y == 61
assert POWER == 30

CELLS = Cells(7803, 300)
X, Y, POWER = CELLS.find_most_power_for_size(3)
print('most 3x3 power is {pow} at {x},{y}'.format(pow=POWER, x=X, y=Y))

X, Y, POWER, SIZE = GRID_18.find_most_power()
assert X == 90
assert Y == 269
assert POWER == 113
assert SIZE == 16

X, Y, POWER, SIZE = GRID_42.find_most_power()
assert X == 232
assert Y == 251
assert POWER == 119
assert SIZE == 12

X, Y, POWER, SIZE = CELLS.find_most_power()
print('most power is {pow} at square {x},{y},{size}'.format(pow=POWER, x=X, y=Y, size=SIZE))
