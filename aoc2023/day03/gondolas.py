SPACE = '.'

class PartNumber:
    def __init__(self, grid:list[str], value:str, row: int, start_col: int, end_col: int):
        self.value=int(value)
        self.part_type = None
        #is the symbol above?
        for j in range(start_col - 1, end_col +1):
            if self.in_range(grid, row-1, j) and grid[row - 1][j] != SPACE:
                assert not self.part_type
                self.part_type = grid[row - 1][j]
        # is it left or right?
        if self.in_range(grid, row, start_col - 1) and grid[row][start_col - 1] != SPACE:
            assert not self.part_type
            self.part_type = grid[row][start_col - 1]
        if self.in_range(grid, row, end_col) and grid[row][end_col] != SPACE:
            assert not self.part_type
            self.part_type = grid[row][end_col]
        #is it below?
        for j in range(start_col -1, end_col +1):
            if self.in_range(grid, row + 1, j) and grid[row + 1][j] != SPACE:
                assert not self.part_type
                self.part_type = grid[row + 1][j]

    def in_range(self, grid: list[str], row, col):
        return row >= 0 and row < len(grid) and col >=0 and col < len(grid[row])

    def is_part(self):
        return self.part_type is not None

class Engine:
    def __init__(self, input_file:str):
        self.part_numbers = []
        lines = [line.strip() for line in open(input_file).readlines()]
        for row_index, row in enumerate(lines):
            col_index = 0
            while col_index < len(row):
                character = row[col_index]
                if character != SPACE:
                    if character.isdigit():
                        #concatenate adjacent digits, and skip repeats
                        number = character
                        lookahead = col_index + 1
                        while lookahead < len(row) and row[lookahead].isdigit():
                            number += row[lookahead]
                            lookahead += 1
                        #know all about the number now, find the adjacent symbol
                        self.part_numbers.append(PartNumber(lines, number, row_index, col_index, lookahead))
                        #skip processed digits
                        col_index = lookahead
                col_index += 1

    def sum_of_parts(self):
        return sum([number.value for number in self.part_numbers if number.is_part()])

def main():
    sample_engine = Engine('aoc2023/day03/sample.txt')
    assert sample_engine.sum_of_parts() == 4361
    engine = Engine('aoc2023/day03/input.txt')
    print('Answer to Part 1:', engine.sum_of_parts())

if __name__ == '__main__':
    main()
