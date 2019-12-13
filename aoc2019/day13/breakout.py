import utils
from aoc2019.int_code import IntCode

EMPTY = 0
WALL = 1
BLOCK = 2
HORIZ_PADDLE = 3
BALL = 4

def parse_results(result):
    return [(result[i], result[i + 1], result[i + 2]) for i in range(0, len(result), 3)]

class Breakout:
    def __init__(self, input_file):
        self.tiles = {}
        self.model = IntCode(input_file)

    def add_tile(self, x, y, tile):
        self.tiles[(x, y)] = tile

    def run(self):
        result = self.model.run_program()
        for x, y, z in parse_results(result):
            self.add_tile(x, y, z)

    def count_tiles(self, tile_type):
        count = 0
        for tile in self.tiles.values():
            print(tile)
            if tile == tile_type:
                count += 1
        print(count)
        return count

RESULT = [1, 2, 3, 6, 5, 4]
PARSED = parse_results(RESULT)
assert len(PARSED) == 2
assert PARSED[0] == (1, 2, 3)
assert PARSED[1] == (6, 5, 4)

SAMPLE = Breakout('input.txt')
for x, y, z in PARSED:
    SAMPLE.add_tile(x, y, z)
assert SAMPLE.count_tiles(BALL) == 1
assert SAMPLE.count_tiles(HORIZ_PADDLE) == 1

PROBLEM = Breakout('input.txt')
PROBLEM.run()
utils.pretty_print_answer(1, PROBLEM.count_tiles(BLOCK))
