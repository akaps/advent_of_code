import utils

OPEN = '.'
TREE = '|'
YARD = '#'

class Forest:
    def __init__(self, file_name):
        file = open(file_name)
        lines = file.readlines()
        file.close()
        self.acres = []
        for line in lines:
            self.acres.append(list(line.strip()))

    def num_open(self):
        return self.num_type(OPEN)

    def num_trees(self):
        return self.num_type(TREE)

    def num_yards(self):
        return self.num_type(YARD)

    def num_type(self, type_val):
        total = 0
        for row in self.acres:
            for val in row:
                if val == type_val:
                    total += 1
        return total

    def score(self):
        return self.num_trees() * self.num_yards()

    def next_generation(self):
        new_gen = []
        for row_index, row in enumerate(self.acres):
            next_row = []
            for col_index, val in enumerate(row):
                adj_tree, adj_yard = self.adjacencies(row_index, col_index)
                if val == OPEN:
                    next_row.append(open_rule(adj_tree))
                if val == TREE:
                    next_row.append(tree_rule(adj_yard))
                if val == YARD:
                    next_row.append(yard_rule(adj_yard, adj_tree))
            new_gen.append(next_row)
        self.acres = new_gen

    def adjacencies(self, row, col):
        adj_tree = 0
        adj_yard = 0
        for row_mod in range(-1, 2):
            for col_mod in range(-1, 2):
                if (
                        0 <= row + row_mod < len(self.acres) and
                        0 <= col + col_mod < len(self.acres) and
                        not (row_mod == col_mod == 0)):
                    if self.acres[row + row_mod][col + col_mod] == TREE:
                        adj_tree += 1
                    if self.acres[row + row_mod][col + col_mod] == YARD:
                        adj_yard += 1
        return adj_tree, adj_yard

    def __repr__(self):
        res = []
        for row in self.acres:
            res.append(''.join(row))
            res.append('\n')
        return ''.join(res)

def open_rule(adj_tree):
    if adj_tree >= 3:
        return TREE
    return OPEN

def tree_rule(adj_yard):
    if adj_yard >= 3:
        return YARD
    return TREE

def yard_rule(adj_yard, adj_tree):
    if adj_yard >= 1 and adj_tree >= 1:
        return YARD
    return OPEN

SAMPLE = Forest('sample.txt')
assert SAMPLE.num_trees() == 27
assert SAMPLE.num_yards() == 17
assert SAMPLE.num_open() == 56
SAMPLE.next_generation()
assert SAMPLE.num_trees() == 40
assert SAMPLE.num_yards() == 12
assert SAMPLE.num_open() == 48

for _ in range(9):
    SAMPLE.next_generation()
assert SAMPLE.num_trees() == 37
assert SAMPLE.num_yards() == 31
assert SAMPLE.num_open() == 32
assert SAMPLE.score() == 1147

PROBLEM = Forest('input.txt')
for _ in range(10):
    PROBLEM.next_generation()
utils.pretty_print_answer(1, PROBLEM.score())

for _ in range(1000000000 - 10):
    PROBLEM.next_generation()
utils.pretty_print_answer(2, PROBLEM.score())
