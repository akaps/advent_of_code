import utils

OCCUPIED = '#'
EMPTY = 'L'
FLOOR = '.'

class Seats:
    def __init__(self, file_name):
        self.seats = utils.read_matrix(file_name)
        self.states = []

    def generate_stable(self):
        count = self.count_occupied()
        while count not in self.states:
            self.states.append(count)
            self.seats, count = self.next_generation()


    def in_bounds_not_identity(self, row, col):
        return 0 <= row < len(self.seats) and 0 <= col < len(self.seats[0])


    def count_adj(self, row, col):
        count = 0
        for row_mod in range(-1, 2):
            for col_mod in range(-1, 2):
                if not row_mod == col_mod == 0:
                    next_row = row + row_mod
                    next_col = col + col_mod
                    if (self.in_bounds_not_identity(next_row, next_col)
                            and self.seats[next_row][next_col] == OCCUPIED):
                        count += 1
        return count

    def next_generation(self):
        generation = []
        num_occupied = 0
        for row_index, row in enumerate(self.seats):
            generation_row = []
            for col_index, seat in enumerate(row):
                if seat == FLOOR:
                    generation_row.append(FLOOR)
                    continue
                count = self.count_adj(row_index, col_index)
                if seat == OCCUPIED and count >= 4:
                    generation_row.append(EMPTY)
                elif seat == EMPTY and count == 0:
                    generation_row.append(OCCUPIED)
                    num_occupied += 1
                else:
                    generation_row.append(seat)
                    if seat == OCCUPIED:
                        num_occupied += 1
            generation.append(generation_row)
        return generation, num_occupied

    def count_occupied(self):
        total = 0
        for row in self.seats:
            for seat in row:
                if seat == OCCUPIED:
                    total += 1
        return total

    def __repr__(self):
        result = []
        for row in self.seats:
            result.append(''.join(row))
        return '\n'.join(result)

def main():
    seats = Seats('input.txt')
    seats.generate_stable()
    utils.pretty_print_answer(1, seats.count_occupied())

if __name__ == "__main__":
    main()
