import re

ROUND = 'O'
CUBE = '#'
EMPTY = '.'

class Abacus:
    def __init__(self, file_name):
        lines = open(file_name, encoding='utf-8').readlines()
        self.map = []
        for line in lines:
            self.map.append(list(line.strip()))

    def tilt_north(self):
        for col_index in range(0, len(self.map[0])):
            empty = 0
            for row_index, row in enumerate(self.map):
                if row[col_index] == CUBE:
                    empty = row_index + 1
                elif row[col_index] == ROUND:
                    if row_index != empty:
                        self.map[empty][col_index] = ROUND
                        row[col_index] = EMPTY
                    empty += 1

    def score(self):
        total = 0
        for index, row in enumerate(self.map):
            for char in row:
                if char == ROUND:
                    total += len(self.map) - index
        return total

    def __repr__(self):
        result = []
        for row in self.map:
            result.append(''.join(row))
        return '\n'.join(result)

def main():
    sample = Abacus('aoc2023/day14/sample.txt')
    print(sample.map)
    print('---')
    print(sample.tilt_north())
    print('---')
    print(sample.map)
    assert sample.score() == 136

    problem = Abacus('aoc2023/day14/input.txt')
    problem.tilt_north()
    print('Answer to Part 1:', problem.score())
    print('Answer to Part 2:', -1)

if __name__ == '__main__':
    main()
