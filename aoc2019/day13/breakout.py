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

NEUTRAL = 0
LEFT = -1
RIGHT = 1

SCREEN_WIDTH = 43
SCREEN_HEIGHT = 21

def parse_results(result):
    return [(result[i], result[i + 1], result[i + 2]) for i in range(0, len(result), 3)]

class Breakout:
    def __init__(self, input_file):
        self.tiles = {}
        self.model = IntCode(input_file)
        self.score = 0
        self.moved = False
        self.ball_pos_curr = None
        self.paddle_pos = None

    def update_tile(self, left_right, up_down, tile):
        if left_right == -1:
            self.score = tile
        else:
            if tile == HORIZ_PADDLE:
                self.paddle_pos = (left_right, up_down)
            elif tile == BALL:
                self.ball_pos_curr = (left_right, up_down)
            self.tiles[(left_right, up_down)] = tile

    def generate_next_move(self):
        if not self.moved:
            self.moved = True
            return NEUTRAL
        if self.paddle_pos > self.ball_pos_curr:
            return LEFT
        return RIGHT

    def run(self, debug=False):
        program = self.model.load_program()
        result = program.send(None)
        while isinstance(result, list):
            self.update_tiles(result)
            next_move = None
            if debug:
                print(self)
                next_move = int(input('next_move'))
            else:
                next_move = self.generate_next_move()
            result = program.send(next_move)

    def update_tiles(self, results):
        for left_right, up_down, tile in parse_results(results):
            self.update_tile(left_right, up_down, tile)

    def count_tiles(self, tile_type):
        count = 0
        for tile in self.tiles.values():
            if tile == tile_type:
                count += 1
        return count

    def __repr__(self):
        rows = []
        for up_down in range(SCREEN_HEIGHT):
            current_row = []
            for left_right in range(SCREEN_WIDTH):
                coord = (left_right, up_down)
                tile = EMPTY
                if coord in self.tiles:
                    tile = self.tiles[coord]
                current_row.append(TILE_REPS[tile])
            rows.append(''.join(current_row))
        rows.append('score: {score}'.format(score=self.score))
        return '\n'.join(rows)

PROBLEM = Breakout('input.txt')
PROBLEM.run()
utils.pretty_print_answer(1, PROBLEM.count_tiles(BLOCK))

PROBLEM = Breakout('input.txt')
PROBLEM.model.initial_state[0] = 2
PROBLEM.run()
assert PROBLEM.count_tiles(BLOCK) == 0
assert PROBLEM.score == 13581
utils.pretty_print_answer(2, PROBLEM.score)
