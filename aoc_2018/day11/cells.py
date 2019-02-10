import math

#reminder: top-left is 1, 1. x, y notation
class Cells:
    def __init__(self, serial, size):
        self.populate_cells(size, serial)

    def populate_cells(self, size, serial):
        self.cells = []
        self.cell_sums = []
        for _ in range(size):
            self.cells.append([0] * size)
            self.cell_sums.append([0] * size)
        for row in range(size):
            for col in range(0, size):
                self.cells[row][col] = calculate(row + 1, col + 1, serial)
                self.cell_sums[row][col] = self.summed_area(row, col)

    def find_most_power(self):
        x_max, y_max = -1, -1
        max_power = -math.inf
        for row in range(len(self.cells) - 2):
            for col in range(len(self.cells) - 2):
                total = self.total_power(row, col)
                if total > max_power:
                    x_max, y_max = row + 1, col + 1
                    max_power = total
        return x_max, y_max

    def total_power(self, row, col):
        total = 0
        for i in range(3):
            for j in range(3):
                total += self.cells[row + i][col + j]
        return total

    #2D implementation of Kadane's algorithm
    def most_power_square(self):
        max_sum = -999999999999
        max_x = max_y = max_size = -1
        for size in range(1, 300):
            for row in range(300-size):
                for col in range(300-size):
                    if self.sum_area(row, col, size) > max_sum:
                        max_x = row
                        max_y = col
                        max_size = size
        return max_x, max_y, max_size

    def sum_area(self, row, col, size):
        return (self.cell_sums[row][col] -
                self.cell_sums[row - size][col] -
                self.cell_sums[row][col - size] +
                self.cell_sums[row - size][col - size])

    def summed_area(self, row, col):
        prev_col = col - 1
        prev_row = row - 1
        bot_right = self.cells[row][col]
        bot_left = self.cell_sums[row][prev_col] if col - 1 >= 0 else 0
        top_right = self.cell_sums[prev_row][col] if row - 1 >= 0 else 0
        top_left = self.cell_sums[prev_row][prev_col] if row - 1 >= 0 and col - 1 >= 0 else 0
        return bot_right + bot_left + top_right - top_left

    def power_square(self, row, col, size):
        total = 0
        row -= 1
        col -= 1
        for i in range(row, row+size):
            for j in range(col, col+size):
                total += self.cells[i][j]
        return total

def calculate(row, col, serial):
    return ((col * (row + 10) + serial) * (row + 10) // 100 % 10) - 5

assert calculate(3, 5, 8) == 4
assert calculate(122, 79, 57) == -5
assert calculate(217, 196, 39) == 0
assert calculate(101, 153, 71) == 4

GRID__SIZE_3 = Cells(18, 2)
assert GRID__SIZE_3.cell_sums[0][0] == -2
assert GRID__SIZE_3.cell_sums[0][1] == -3
assert GRID__SIZE_3.cell_sums[1][0] == -4
assert GRID__SIZE_3.cell_sums[1][1] == -5

GRID_18 = Cells(18, 300)
X, Y = GRID_18.find_most_power()
assert X == 33
assert Y == 45
assert GRID_18.power_square(33, 45, 3) == 29

GRID_42 = Cells(42, 300)
X, Y = GRID_42.find_most_power()
assert X == 21
assert Y == 61
assert GRID_42.power_square(21, 61, 3) == 30

X, Y, SIZE = GRID_18.most_power_square()
assert GRID_18.power_square(90, 269, 16) == 113
assert X == 90
assert Y == 269
assert SIZE == 16

X, Y, SIZE = GRID_42.most_power_square()
assert GRID_42.power_square(232, 251, 12) == 119
assert X == 232
assert Y == 251
assert SIZE == 12

CELLS = Cells(7803, 300)
X, Y = CELLS.find_most_power()
print('most 3x3 power at ({x},{y})'.format(x=X, y=Y))
X, Y, SIZE = CELLS.most_power_square()
print('most power at square ({x},{y},{size})'.format(x=X, y=Y, size=SIZE))
