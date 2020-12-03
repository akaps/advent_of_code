import utils

TREE = '#'

class Map:
    def __init__(self, file_name):
        self.grid = []
        lines = utils.read_lines(file_name)
        for line in lines:
            self.grid.append(list(line))

    def traverse(self, col_mod, row_mod):
        num_trees = 0
        row = col = 0
        while row < len(self.grid):
            if self.grid[row][col] == TREE:
                num_trees += 1
            row += row_mod
            col = (col + col_mod) % len(self.grid[0])
        return num_trees

def main():
    trees = Map('input.txt')
    num_trees = trees.traverse(3, 1)
    utils.pretty_print_answer(1, num_trees)

    for col_mod, row_mod in [(1, 1), (5, 1), (7, 1), (1, 2)]:
        num_trees *=  trees.traverse(col_mod, row_mod)
    utils.pretty_print_answer(2, num_trees)

if __name__ == "__main__":
    main()
