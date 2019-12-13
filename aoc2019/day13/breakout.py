import utils
from aoc2019.int_code import IntCode

EMPTY = 0
WALL = 1
BLOCK = 2
HORIZ_PADDLE = 3
BALL = 4

TILE_REPS = {
    EMPTY: ' ',
    WALL: '#',
    BLOCK: 'X',
    HORIZ_PADDLE: '_',
    BALL: 'O'
}

SCREEN_WIDTH = 43
SCREEN_HEIGHT = 21

def parse_results(result):
    return [(result[i], result[i + 1], result[i + 2]) for i in range(0, len(result), 3)]

class Breakout:
    def __init__(self, input_file):
        self.tiles = {}
        self.model = IntCode(input_file)
        self.score = 0

    def update_tile(self, x, y, tile):
        if x == -1:
            self.score = tile
        else:
            self.tiles[(x, y)] = tile

    def run(self):
        result = self.model.run_program()
        for x, y, z in parse_results(result):
            self.update_tile(x, y, z)

    def count_tiles(self, tile_type):
        count = 0
        for tile in self.tiles.values():
            if tile == tile_type:
                count += 1
        return count

    def __repr__(self):
        rows = []
        for y in range(SCREEN_HEIGHT):
            current_row = []
            for x in range(SCREEN_WIDTH):
                coord = (x, y)
                tile = EMPTY
                if coord in self.tiles:
                    tile = self.tiles[coord]
                current_row.append(TILE_REPS[tile])
            rows.append(''.join(current_row))
        rows.append('score: {score}'.format(score=self.score))
        return '\n'.join(rows)

RESULT = [1, 2, 3, 6, 5, 4]
PARSED = parse_results(RESULT)
assert len(PARSED) == 2
assert PARSED[0] == (1, 2, 3)
assert PARSED[1] == (6, 5, 4)

SAMPLE = Breakout('input.txt')
for x, y, z in PARSED:
    SAMPLE.update_tile(x, y, z)
assert SAMPLE.count_tiles(BALL) == 1
assert SAMPLE.count_tiles(HORIZ_PADDLE) == 1

PROBLEM = Breakout('input.txt')
PROBLEM.run()
utils.pretty_print_answer(1, PROBLEM.count_tiles(BLOCK))
