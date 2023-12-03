SPACE = '.'
GEAR = '*'

def in_bounds(grid: list[str], row: int, col: int):
    return row >= 0 and row < len(grid) and col >=0 and col < len(grid[row])

class Part:
    def __init__(self, part_type:str):
        self.part_type = part_type
        self.numbers = []

    def add_number(self, part_number: str):
        self.numbers.append(int(part_number))

class Engine:
    def __init__(self, input_file:str):
        self.parts = {} #key: position, value, part type and associated numbers
        grid = [line.strip() for line in open(input_file).readlines()]
        for row_index, row in enumerate(grid):
            col_index = 0
            while col_index < len(row):
                character = grid[row_index][col_index]
                if character.isdigit():
                    number = self.find_number(grid, row_index, col_index)
                    part_location, part_type = self.find_part(grid, row_index, col_index, len(number))
                    if part_location:
                        if part_location not in self.parts:
                            self.parts[part_location] = Part(part_type)
                        self.parts[part_location].add_number(number)
                    col_index += len(number)
                else:
                    col_index += 1

    def find_number(self, grid: list[str], row_index: int, col_index: int):
        end_index = col_index
        while in_bounds(grid, row_index, end_index) and grid[row_index][end_index].isdigit():
            end_index += 1
        return grid[row_index][col_index:end_index]

    def find_part(self, grid: list[str], row_index: int, col_index: int, number_width: int):
        #is the symbol above?
        candidates = []
        candidates.extend([(row_index - 1, j) \
                           for j in range(col_index - 1, col_index + number_width + 1)])
        candidates.append((row_index, col_index - 1))
        candidates.append((row_index, col_index + number_width))
        candidates.extend([(row_index + 1, j) \
                           for j in range(col_index - 1, col_index + number_width + 1)])
        for x_pos, y_pos in candidates:
                if in_bounds(grid, x_pos, y_pos) and grid[x_pos][y_pos] != SPACE:
                    return (x_pos, y_pos), grid[x_pos][y_pos]
        return None, None

    def sum_of_parts(self):
        total = 0
        for part in self.parts.values():
            total += sum(part.numbers)
        return total

    def sum_of_gear_ratios(self):
        total = 0
        for part in self.parts.values():
            if part.part_type == GEAR and len(part.numbers) == 2:
                total += part.numbers[0] * part.numbers[1]
        return total

def main():
    sample_engine = Engine('aoc2023/day03/sample.txt')
    assert sample_engine.sum_of_parts() == 4361
    engine = Engine('aoc2023/day03/input.txt')
    print('Answer to Part 1:', engine.sum_of_parts())

    assert sample_engine.sum_of_gear_ratios() == 467835
    print('Answer to Part 2: ', engine.sum_of_gear_ratios())

if __name__ == '__main__':
    main()
