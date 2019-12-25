BUG = '#'
EMPTY = '.'
DIM = 5

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

def in_bounds(row, col):
    return 0 <= row < DIM and 0 <= col < DIM

def score_index(row_index, col_index):
    return 2 ** (row_index * DIM + col_index)

def pretty_print(grid):
    result = []
    for row in grid:
        next_row = []
        for val in row:
            next_row.append(val)
        result.append(''.join(next_row))
    print('\n'.join(result))

class Ants:
    def __init__(self, file_name):
        file = open(file_name)
        lines = [string.strip() for string in file.readlines()]
        file.close()
        self.cells = []
        for line in lines:
            self.cells.append(list(line))

    def count_adjacent(self, row, col):
        total = 0
        for row_mod, col_mod in [UP, DOWN, LEFT, RIGHT]:
            neighbor_row = row + row_mod
            neighbor_col = col + col_mod
            if (in_bounds(neighbor_row, neighbor_col)
                and self.cells[neighbor_row][neighbor_col] == BUG):
                total += 1
        return total

    def score(self):
        score = 0
        for row_index, row in enumerate(self.cells):
            for col_index, val in enumerate(row):
                score += score_index(row_index, col_index) if val == BUG else 0
        return score

    def update(self):
        score = 0
        next_generation = []
        for row_index, row in enumerate(self.cells):
            next_row = []
            for col_index, val in enumerate(row):
                next_val = None
                neighbors = self.count_adjacent(row_index, col_index)
                if val == BUG:
                    next_val = BUG if neighbors == 1 else EMPTY
                elif val == EMPTY:
                    next_val = BUG if 0 < neighbors <= 2 else EMPTY
                if next_val == BUG:
                    score += score_index(row_index, col_index)
                next_row.append(next_val)
            next_generation.append(next_row)
        self.cells = next_generation
        return score

    def find_first_repeat_score(self):
        previous_scores = []
        score = self.score()
        while score not in previous_scores:
            previous_scores.append(score)
            score = self.update()
        return score

assert score_index(0, 0) == 1
assert score_index(0, 1) == 2
assert score_index(0, 2) == 4
assert score_index(0, 3) == 8
assert score_index(0, 4) == 16
assert score_index(1, 0) == 32
assert score_index(1, 1) == 64
assert score_index(3, 0) == 32768
assert score_index(4, 1) == 2097152

SAMPLE = Ants('sample.txt')
SCORE = SAMPLE.find_first_repeat_score()
assert SCORE == 2129920

PROBLEM = Ants('input.txt')
print('Answer to part 1: {ans}'.format(ans=PROBLEM.find_first_repeat_score()))
