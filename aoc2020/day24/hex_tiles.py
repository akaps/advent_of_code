from collections import defaultdict
import re
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

class HexTiles:
    def __init__(self, file_name):
        self.tiles = defaultdict(lambda: False)
        lines = utils.read_lines(file_name)
        for line in lines:
            tile = np.array([0, 0, 0])
            while line:
                next_direction = line[0]
                line = line[1:]
                if next_direction in ['n', 's']:
                    next_direction += line[0]
                    line = line[1:]
                tile += DIRECTIONS[next_direction]
            destination = str(tile)
            self.tiles[destination] = not self.tiles[destination]

    def count_black_tiles(self):
        count = 0
        for tile_val in self.tiles.values():
            if tile_val:
                count += 1
        return count

    def run_simulation(self, num_iterations):
        for i in range(num_iterations):
            print(i)
            self.next_generation()

    def next_generation(self):
        processed = {}
        to_process = [x for x in self.tiles.keys()]
        while to_process:
            next_tile = to_process.pop(0)
            if next_tile not in processed:
                # print(next_tile)
                tile_neighbors = neighbors(next_tile)
                for neighbor in tile_neighbors:
                    if neighbor in self.tiles:
                        to_process.append(neighbor)
                count = self.count_neighbors(tile_neighbors)
                if self.tiles[next_tile]:
                    processed[next_tile] = not (count == 0 or count > 2)
                else:
                    processed[next_tile] = count == 2
        self.tiles = processed

    def count_neighbors(self, neighbor_list):
        count = 0
        for neighbor in neighbor_list:
            if self.tiles[str(neighbor)]:
                count += 1
        return count

def neighbors(coordinate):
    coordinates = re.findall(r'-?\d+', coordinate)
    coordinate = np.array(coordinates, dtype=int)
    result = []
    for direction in DIRECTIONS.values():
        result.append(str(coordinate + direction))
    return result

def main():
    hexes = HexTiles('input.txt')
    utils.pretty_print_answer(1, hexes.count_black_tiles())
    hexes.run_simulation(100)
    utils.pretty_print_answer(2, hexes.count_black_tiles())

if __name__ == "__main__":
    main()
