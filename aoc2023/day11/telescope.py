import re
GALAXY = '#'

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

class Telescope:
    def __init__(self, file_name):
        self.galaxies = []
        self.blank_rows = []
        self.blank_columns = []
        lines = [line.strip() for line in open(file_name, encoding='utf-8').readlines()]
        for row_index, row in enumerate(lines):
            empty_row = True
            for col_index, char in enumerate(row):
                if char == GALAXY:
                    self.galaxies.append(Point(row_index, col_index))
                    empty_row = False
            if empty_row:
                self.blank_rows.append(row_index)
        self.find_empty_columns(lines)
        self.expand_galaxy()

    def find_empty_columns(self, lines):
        for col_index in range(len(lines[0])):
            empty_col = True
            for row_index , row in enumerate(lines):
                if row[col_index] == GALAXY:
                    empty_col = False
            if empty_col:
                self.blank_columns.append(col_index)

    def expand_galaxy(self):
        for galaxy in self.galaxies:
            for blank_row in self.blank_rows[::-1]:
                if galaxy.x > blank_row:
                    galaxy.x += 1
            for blank_col in self.blank_columns[::-1]:
                if galaxy.y > blank_col:
                    galaxy.y += 1

    def sum_of_distances(self):
        total = 0
        for gal_index, galaxy in enumerate(self.galaxies):
            for other_index in range(gal_index + 1, len(self.galaxies)):
                total += galaxy.manhattan_distance(self.galaxies[other_index])
        return total

def main():
    sample = Telescope('aoc2023/day11/sample.txt')
    assert sample.blank_rows == [3, 7]
    assert sample.blank_columns == [2, 5, 8]
    assert sample.sum_of_distances() ==  374

    telescope = Telescope('aoc2023/day11/input.txt')
    print('Answer to Part 1:', telescope.sum_of_distances())
    print('Answer to Part 2:', -1)

if __name__ == '__main__':
    main()
