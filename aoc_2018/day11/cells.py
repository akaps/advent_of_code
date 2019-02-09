import math

#reminder: top-left is 1, 1. x, y notation
class Cells:
    def __init__(self, serial, size):
        self.serial = serial
        self.cells = []
        self.cell_sums = []
        for _ in range(size):
            self.cells.append([None] * size)
            self.cell_sums.append([None] * size)
        for x in range(size):
            for y in range(0, size):
                self.cells[x][y] = calculate(x + 1, y + 1, self.serial)

    def find_most_power(self):
        x_max, y_max = -1, -1
        max_power = -math.inf
        for x in range(len(self.cells) - 2):
            for y in range(len(self.cells) - 2):
                total = self.total_power(x, y)
                if total > max_power:
                    x_max, y_max = x + 1, y + 1
                    max_power = total
        return x_max, y_max

    def total_power(self, x, y):
        total = 0
        for i in range(3):
            for j in range(3):
                total += self.cells[x + i][y + j]
        return total

    def most_power_square(self):
        self.summed_areas()
        max_ending = max_so_far = self.cell_sums[0][0]
        for x in range(1, len(self.cell_sums)):
            for y in range(1, len(self.cell_sums[x])):
                max_ending = max(self.cell_sums[x][y], self.cell_sums[x][y] + max_ending)
                max_so_far = max(max_so_far, max_ending)
        print(max_so_far)
        return -1, -1, -1

    def summed_areas(self):
        for x in range(len(self.cells)):
            for y in range(len(self.cells[x])):
                self.cell_sums[x][y] = self.summed_area(x, y)

    def summed_area(self, x, y):
        return (self.cells[x][y] +
                self.cell_sums[x][y - 1] if y - 1 >= 0 else 0 +
                self.cell_sums[x - 1][y] if x - 1 >= 0 else 0 -
                self.cell_sums[x - 1][y - 1] if x - 1 >=0 and y - 1 >= 0 else 0)

    def power_square(self, x, y, size):
        total = 0
        x -= 1
        y -= 1
        for i in range(x, x+size):
            for j in range(y, y+size):
                total += self.cells[i][j]
        return total


def calculate(x, y, serial):
    return ((y * (x + 10) + serial) * (x + 10) // 100 % 10) - 5

assert calculate(3, 5, 8) == 4
assert calculate(122, 79, 57) == -5
assert calculate(217, 196, 39) == 0
assert calculate(101, 153, 71) == 4

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
