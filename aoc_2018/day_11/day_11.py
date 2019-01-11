import math

#reminder: top-left is 1, 1. x, y notation
class Cells:
    def __init__(self, serial, size):
        self.serial = serial
        self.cells = []
        for _ in range(size):
            self.cells.append([None] * size)
        for x in range(1, size + 1):
            for y in range(1, size + 1):
                x_t, y_t = true_coord(x, y)
                self.cells[x_t][y_t] = calculate(x, y, self.serial)

    def find_most_power(self):
        x_max, y_max = 0, 0
        max_power = -math.inf
        for x in range(1, len(self.cells) - 2):
            for y in range(1, len(self.cells) - 2):
                x_t, y_t = true_coord(x, y)
                total = self.total_power(x_t, y_t)
                if total > max_power:
                    x_max, y_max = x, y
                    max_power = total
        return x_max, y_max

    def total_power(self, x, y):
        total = 0
        for i in range(3):
            for j in range(3):
                total += self.cells[x + i][y + j]
        return total

def calculate(x, y, serial):
    return ((y * (x+10) + serial) * (x+10) // 100 % 10) - 5

def true_coord(x, y):
    return x-1, y-1

assert calculate(3, 5, 8) == 4
sample = Cells(8, 5)
assert sample.cells[2][4] == 4
assert calculate(122, 79, 57) == -5
assert calculate(217, 196, 39) == 0
assert calculate(101, 153, 71) == 4
sample = Cells(18, 300)
x, y = sample.find_most_power()
assert x == 33
assert y == 45
sample = Cells(42, 300)
x, y = sample.find_most_power()
assert x == 21
assert y == 61

cells = Cells(7803, 300)
x, y = sample.find_most_power()
print('most power at ({x}, {y})'.format(x=x, y=y))
