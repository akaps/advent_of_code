import utils

ROCKY = 0
WET = 1
NARROW = 2

class Maze:
    def __init__(self, depth, target):
        self.depth = depth
        self.target = target
        self.erosion_levels = {}
        self.geologic_indexes = {}

    def type(self, x, y):
        return self.erosion_level(x, y) % 3

    def erosion_level(self, x, y):
        index = (x, y)
        if index in self.erosion_levels:
            return self.erosion_levels[index]
        val = (self.geologic_index(x, y) + self.depth) % 20183
        self.erosion_levels[index] = val
        return val

    def geologic_index(self, x, y):
        index = (x, y)
        if index in self.geologic_indexes:
            return self.geologic_indexes[index]
        val = -1
        if index in [self.target, (0, 0)]:
            val = 0
        elif y == 0:
            val = x * 16807
        elif x == 0:
            val = y * 48271
        else:
            val = self.erosion_level(x - 1, y) * self.erosion_level(x, y - 1)
        self.geologic_indexes[index] = val
        return val

    def risk(self):
        total = 0
        for x in range(self.target[0] + 1):
            for y in range(self.target[1] + 1):
                total += self.type(x, y)
        return total

SAMPLE = Maze(510, (10, 10))
assert SAMPLE.geologic_index(0, 0) == 0
assert SAMPLE.erosion_level(0, 0) == 510
assert SAMPLE.type(0, 0) == ROCKY

assert SAMPLE.geologic_index(1, 0) == 16807
assert SAMPLE.erosion_level(1, 0) == 17317
assert SAMPLE.type(1, 0) == WET

assert SAMPLE.geologic_index(0, 1) == 48271
assert SAMPLE.erosion_level(0, 1) == 8415
assert SAMPLE.type(0, 1) == ROCKY

assert SAMPLE.geologic_index(1, 1) == 145722555
assert SAMPLE.erosion_level(1, 1) == 1805
assert SAMPLE.type(1, 1) == NARROW

assert SAMPLE.geologic_index(10, 10) == 0
assert SAMPLE.erosion_level(10, 10) == 510
assert SAMPLE.type(10, 10) == ROCKY
assert SAMPLE.risk() == 114

PROBLEM = Maze(6969, (9, 796))
utils.pretty_print_answer(1, PROBLEM.risk())
