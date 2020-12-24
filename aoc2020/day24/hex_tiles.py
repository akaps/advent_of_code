from collections import defaultdict
import numpy as np
import utils

DIRECTIONS = {
    'e': [1, 0, -1],
    'se': [0, 1, -1],
    'sw': [-1, 1, 0],
    'w': [-1, 0, 1],
    'nw': [0, -1, 1],
    'ne': [1, -1, 0],
}

class HexTile:
    def __init__(self):
        self.coords = np.array([0, 0, 0])

    def translate(self, direction):
        self.coords += DIRECTIONS[direction]

    def __repr__(self):
        return ','.join([str(x) for x in self.coords])

class HexTiles:
    def __init__(self, file_name):
        self.tiles = defaultdict(lambda: False)
        lines = utils.read_lines(file_name)
        for line in lines:
            tile = HexTile()
            while line:
                next_direction = line[0]
                line = line[1:]
                if next_direction in ['n', 's']:
                    next_direction += line[0]
                    line = line[1:]
                tile.translate(next_direction)
            destination = str(tile)
            self.tiles[destination] = not self.tiles[destination]
        # print(self.tiles)
        # print([x for x in self.tiles.values() if x == False])

    def count_black_tiles(self):
        count = 0
        for tile_val in self.tiles.values():
            if tile_val:
                count += 1
        return count

def main():
    hexes = HexTiles('input.txt')
    utils.pretty_print_answer(1, hexes.count_black_tiles())

if __name__ == "__main__":
    main()
