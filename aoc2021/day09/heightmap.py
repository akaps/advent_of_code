UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
DIRECTIONS = [UP, DOWN, LEFT, RIGHT]

class Heightmap:
    def __init__(self, file_name):
        self.grid = []
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                self.grid.append([int(x) for x in line.strip()])
        print(self.grid)

    def is_in_bounds(self, x_pos, y_pos):
        return 0 <= x_pos < len(self.grid) and 0 <= y_pos < len(self.grid[0])

    def get_adjacent_values(self, x_pos, y_pos):
        adjacents = []
        for x_mod, y_mod in DIRECTIONS:
            adj_x = x_pos + x_mod
            adj_y = y_pos + y_mod
            if self.is_in_bounds(adj_x, adj_y):
                adjacents.append(self.grid[adj_x][adj_y])
        return adjacents

    def find_low_points(self):
        lows = []
        for x_pos, row in enumerate(self.grid):
            for y_pos, val in enumerate(row):
                adjacents = self.get_adjacent_values(x_pos, y_pos)
                if val < min(adjacents):
                    lows.append(val)
        return lows

    def low_point_risk(self):
        low_points = self.find_low_points()
        return sum(low_points) + len(low_points)

def main():
    sample = Heightmap('aoc2021/day09/sample.txt')
    assert len(sample.find_low_points()) == 4
    assert sample.low_point_risk() == 15

    problem = Heightmap('aoc2021/day09/input.txt')
    print('Part 1:', problem.low_point_risk())

if __name__ == '__main__':
    main()
