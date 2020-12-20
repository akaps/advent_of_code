import re
from collections import defaultdict
import utils

UP = 'north'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

ID_REGEX = r'(\d+)'

class Tile:
    def __init__(self, matrix_lines):
        self.matrix = []
        for row in matrix_lines:
            self.matrix.append(list(row))
        self.borders = self.get_border_keys()
        self.connections = []

    def get_border_keys(self):
        keys = {}
        #up
        keys[UP] = ''.join(self.matrix[0])
        #down
        keys[DOWN] = ''.join(reversed(self.matrix[-1]))
        #left
        keys[LEFT] = ''.join(reversed([self.matrix[i][0] for i in range(10)]))
        #right
        keys[RIGHT] = ''.join([self.matrix[i][9] for i in range(10)])
        return keys

    def add_connection(self, adj_tile_id):
        self.connections.append(adj_tile_id)

    def rotate(self, num_times):
        assert False, 'Unimplemented'

    def flip(self, axis):
        assert False, 'Unimplemented'

    def __repr__(self):
        return ' '.join([str(x) for x in self.connections])

class Tiles:
    def __init__(self, file_name):
        groups = utils.read_groups(file_name)
        self.tiles = {}
        for group in groups:
            id_num = int(re.findall(ID_REGEX, group[0])[0])
            self.tiles[id_num] = Tile(group[1:])
        self.connections = self.find_connections()

    def find_connections(self):
        connections = {}
        for tile_id, tile in self.tiles.items():
            for border in tile.borders.values():
                reverse = border[::-1]
                border_id = -1
                if border in connections:
                    border_id = connections[border][0]
                    connections[border].append(tile_id)
                elif reverse in connections:
                    border_id = connections[reverse][0]
                    connections[reverse].append(tile_id)
                else:
                    connections[border] = [tile_id]
                if border_id > -1:
                    self.tiles[border_id].add_connection(tile_id)
                    self.tiles[tile_id].add_connection(border_id)
        return connections

    def find_corners(self):
        print(self.tiles)
        corners = []
        for tile_id, tile in self.tiles.items():
            print(tile.connections)
            if len(tile.connections) == 2:
                corners.append(tile_id)
        return corners

    def product_of_corners(self):
        product = 1
        corner_ids = self.find_corners()
        for corner_id in corner_ids:
            product *= corner_id
        return product

def main():
    tiles = Tiles('aoc2020/day20/input.txt')
    utils.pretty_print_answer(1, tiles.product_of_corners())

if __name__ == "__main__":
    main()
