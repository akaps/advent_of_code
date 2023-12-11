import re

VERT_PIPE = '|'
HORIZ_PIPE = '-'
L_BEND = 'L'
J_BEND = 'J'
SEVEN_BEND = '7'
F_BEND = 'F'
GROUND = '.'
START = 'S'

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __hash__(self):
        return self.x.__hash__() + (10000 * self.y.__hash__())

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self) -> str:
        return str(self)

NORTH = Point(-1, 0)
SOUTH = Point(1, 0)
EAST = Point(0, 1)
WEST = Point(0, -1)

ADJACENTS = {
    VERT_PIPE: [NORTH, SOUTH],
    HORIZ_PIPE: [EAST, WEST],
    L_BEND: [NORTH, EAST],
    J_BEND: [NORTH, WEST],
    SEVEN_BEND: [SOUTH, WEST],
    F_BEND: [SOUTH, EAST]
}

class PipeNetwork:
    def __init__(self, file_name):
        lines = [line.strip() for line in open(file_name, encoding='utf-8').readlines()]
        self.map = {}
        self.start = None
        for row_index, row in enumerate(lines):
            for col_index, char in enumerate(row):
                current_location = Point(row_index, col_index)
                if char != GROUND:
                    self.map[current_location] = char
                if char == START:
                    self.start = current_location

    def determine_start(self):
        adjacent_to_start = []
        for dir_mod in [NORTH, SOUTH, EAST, WEST]:
            other_loc = self.start + dir_mod
            if other_loc in self.map:
                other_char = self.map[other_loc]
                for other_mod in ADJACENTS[other_char]:
                    if self.start == other_loc + other_mod:
                        adjacent_to_start.append(other_loc)
        return adjacent_to_start

    def distance_to_farthest(self):
        to_process = []
        distances = []
        for adjacent in self.determine_start():
            to_process.append(adjacent)
            distances.append(1)
        processed = {} #point, length
        processed[self.start] = 0
        while to_process:
            curr_location = to_process.pop(0)
            distance = distances.pop(0)
            if curr_location not in processed:
                processed[curr_location] = distance
                for mod in ADJACENTS[self.map[curr_location]]:
                    next_location = curr_location + mod
                    if next_location not in processed and next_location not in to_process:
                        to_process.append(next_location)
                        distances.append(distance + 1)
        return max(processed.values())

def main():
    sample1 = PipeNetwork('aoc2023/day10/sample_1.txt')
    assert sample1.distance_to_farthest() == 4
    sample2 = PipeNetwork('aoc2023/day10/sample_2.txt')
    assert sample2.distance_to_farthest() == 4
    sample3 = PipeNetwork('aoc2023/day10/sample_3.txt')
    assert sample3.distance_to_farthest() == 8
    sample4 = PipeNetwork('aoc2023/day10/sample_4.txt')
    assert sample4.distance_to_farthest() == 8

    pipes = PipeNetwork('aoc2023/day10/input.txt')
    print('Answer to Part 1:', pipes.distance_to_farthest())
    print('Answer to Part 2:', -1)

if __name__ == '__main__':
    main()
