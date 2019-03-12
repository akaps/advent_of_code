import copy

class Automata:
    def __init__(self, file_name, states, rules):
        file = open(file_name)
        lines = file.readlines()
        file.close()
        self.states = states
        self.rules = rules
        self.cells = []
        for line in lines:
            self.cells.append(list(line.strip()))
        self.generations = []

    def count_adj(self, row, col):
        res = dict((key, 0) for key in self.states)
        for row_mod in range(-1, 2):
            for col_mod in range(-1, 2):
                if (not (row_mod == 0 and col_mod == 0) and
                    0 <= row + row_mod < len(self.cells) and
                    0 <= col + col_mod < len(self.cells)):
                    val = self.cells[row + row_mod][col + col_mod]
                    res[val] += 1
        return res

    def count(self, check):
        total = 0
        for row in self.cells:
            for val in row:
                if val == check:
                    total += 1
        return total

    def next_generation(self):
        if self.cells not in self.generations:
            next_gen = []
            for row_index, row in enumerate(self.cells):
                next_row = []
                for col_index, val in enumerate(row):
                    next_val = self.rules[val](self.count_adj(row_index, col_index))
                    next_row.append(next_val)
                next_gen.append(next_row)
            self.generations.append(copy.deepcopy(self.cells))
            self.cells = next_gen
        else:
            index = self.generations.index(self.cells)
            self.cells = self.generations[index]
