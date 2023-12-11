import re
GALAXY = '#'

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def copy(self):
        return Point(self.x, self.y)

class Telescope:
    def __init__(self, file_name):
        self.universe = []
        self.blank_rows = []
        self.blank_columns = []
        lines = [line.strip() for line in open(file_name, encoding='utf-8').readlines()]
        for row_index, row in enumerate(lines):
            empty_row = True
            for col_index, char in enumerate(row):
                if char == GALAXY:
                    self.universe.append(Point(row_index, col_index))
                    empty_row = False
            if empty_row:
                self.blank_rows.append(row_index)
        self.find_empty_columns(lines)

    def find_empty_columns(self, lines):
        for col_index in range(len(lines[0])):
            empty_col = True
            for row_index , row in enumerate(lines):
                if row[col_index] == GALAXY:
                    empty_col = False
            if empty_col:
                self.blank_columns.append(col_index)

    def expand_universe(self, expansion_amt):
        expansion_amt -= 1
        new_universe = []
        for galaxy in self.universe:
            new_galaxy = galaxy.copy()
            for blank_row in self.blank_rows[::-1]:
                if new_galaxy.x > blank_row:
                    new_galaxy.x += expansion_amt
            for blank_col in self.blank_columns[::-1]:
                if new_galaxy.y > blank_col:
                    new_galaxy.y += expansion_amt
            new_universe.append(new_galaxy)
        return new_universe

    def sum_of_distances(self, expansion_amt=2):
        total = 0
        universe = self.expand_universe(expansion_amt)
        for gal_index, galaxy in enumerate(universe):
            for other_index in range(gal_index + 1, len(universe)):
                total += galaxy.manhattan_distance(universe[other_index])
        return total

def main():
    sample = Telescope('aoc2023/day11/sample.txt')
    assert sample.blank_rows == [3, 7]
    assert sample.blank_columns == [2, 5, 8]
    assert sample.sum_of_distances() ==  374

    telescope = Telescope('aoc2023/day11/input.txt')
    print('Answer to Part 1:', telescope.sum_of_distances())

    assert sample.sum_of_distances(10) == 1030
    assert sample.sum_of_distances(100) == 8410
    print('Answer to Part 2:', telescope.sum_of_distances(1000000))

if __name__ == '__main__':
    main()
