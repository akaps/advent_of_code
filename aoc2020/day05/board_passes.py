import utils

F = 'F'
B = 'B'
L = 'L'
R = 'R'

def generate_seat(string):
    row_high = 127
    row_low = 0
    col_high = 7
    col_low = 0
    front_back = string[:7]
    left_right = string[7:]
    for character in front_back:
        row_mid = (row_high + row_low) // 2
        if character == F:
            row_high = row_mid
        else:
            row_low = row_mid + 1
    for character in left_right:
        col_mid = (col_high + col_low) // 2
        if character == L:
            col_high = col_mid
        else:
            col_low = col_mid + 1
    assert row_high == row_low and col_high == col_low
    return 8 * row_high + col_high

def find_gap(seats):
    for index, val in enumerate(seats):
        if seats[index + 1] != val +1:
            return seats[index] + 1

def main():
    seats = []
    lines =utils.read_lines('input.txt')
    for line in lines:
        seats.append(generate_seat(line))
    seats.sort()

    utils.pretty_print_answer(1, seats[-1])
    utils.pretty_print_answer(2, find_gap(seats))

if __name__ == "__main__":
    main()
