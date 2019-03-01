import math

#reminder: top-left is 1, 1. x, y notation
class Cells:
    def __init__(self, serial, size):
        self.calculate_sums(size, serial)

    def calculate_sums(self, size, serial):
        self.serial = serial
        self.cell_sums = []
        for row in range(size):
            self.cell_sums.append([])
            for col in range(size):
                self.cell_sums[row].append(self.summed_area(row, col))

    def find_most_power_for_size(self, size):
        x_max, y_max = -1, -1
        max_power = -math.inf
        for row in range(len(self.cell_sums) - size - 1):
            for col in range(len(self.cell_sums) - size - 1):
                total = self.total_power(row, col, size)
                if total > max_power:
                    x_max, y_max = row + 1, col + 1
                    max_power = total
        return x_max + 1, y_max + 1

    def find_most_power(self):
        max_sum = self.cell_sums[0][0]
        max_x = max_y = max_size = -1
        for size in range(1, 301):
            disp_row, disp_col = self.find_most_power_for_size(size)
            if self.total_power(disp_row - 1, disp_col - 1, size) > max_sum:
                max_x = row
                max_y = col
                max_size = size
        return max_x, max_y, max_size

    def total_power(self, row, col, size):
        return (self.cell_sums[row][col]
                - self.cell_sums[row + size][col]
                - self.cell_sums[row][col + size]
                + self.cell_sums[row + size][col + size])

    def summed_area(self, row, col):
        prev_col = col - 1
        prev_row = row - 1
        return (calculate(row + 1, col + 1, self.serial)
                + (self.cell_sums[row][prev_col] if prev_col >= 0 else 0)
                + (self.cell_sums[prev_row][col] if prev_row >= 0 else 0)
                - (self.cell_sums[prev_row][prev_col] if prev_row >= 0 and prev_col >= 0 else 0))

def calculate(row, col, serial):
    return ((col * (row + 10) + serial) * (row + 10) // 100 % 10) - 5

assert calculate(3, 5, 8) == 4
assert calculate(122, 79, 57) == -5
assert calculate(217, 196, 39) == 0
assert calculate(101, 153, 71) == 4

GRID_18 = Cells(18, 300)
X, Y = GRID_18.find_most_power_for_size(3)
print(X, Y)
assert X == 33
assert Y == 45

GRID_42 = Cells(42, 300)
X, Y = GRID_42.find_most_power_for_size(3)
assert X == 21
assert Y == 61

CELLS = Cells(7803, 300)
X, Y = CELLS.find_most_power_for_size(3)
print('most 3x3 power at ({x},{y})'.format(x=X, y=Y))

assert GRID_18.total_power(33, 45, 3) == 29
assert GRID_18.total_power(90, 269, 16) == 113
assert GRID_42.total_power(21, 61, 3) == 30
assert GRID_42.total_power(232, 251, 12) == 119

X, Y, SIZE = GRID_18.find_most_power()
assert X == 90
assert Y == 269
assert SIZE == 16

X, Y, SIZE = GRID_42.find_most_power()
assert X == 232
assert Y == 251
assert SIZE == 12

X, Y, SIZE = CELLS.find_most_power()
print('most power at square ({x},{y},{size})'.format(x=X, y=Y, size=SIZE))
