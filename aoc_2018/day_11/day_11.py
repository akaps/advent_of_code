#reminder: top-left is 1, 1. x, y notation
class Cells:
    def __init__(self, serial):
        self.serial = serial
        self.cells = [[0] * 300] * 300
        for x in range(1, 300):
            for y in range(1, 300):
                x_t, y_t = true_coord(x, y)
                self.cells[x_t][y_t] = calculate(x, y, self.serial)

    def find_most_power(self):
        return -1, -1

def calculate(x, y, serial):
    return ((y * (x+10) + serial) * (x+10) // 100 % 10) -5

def true_coord(x, y):
    return x-1, y-1

assert calculate(3, 5, 8) == 4
assert calculate(122, 79, 57) == -5
assert calculate(217, 196, 39) == 0
assert calculate(101, 153, 71) == 4
sample = Cells(18)
x, y = sample.find_most_power()
assert x == 33
assert y == 45
sample = Cells(42)
x, y = sample.find_most_power()
assert x == 21
assert y == 61

cells = Cells(7803)
x, y = sample.find_most_power()
print(x, y)
