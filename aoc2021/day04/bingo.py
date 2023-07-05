class BingoBoard:
    def __init__(self, board):
        self.played = [[False for j in range(5)] for i in range(5)]
        self.board = []
        self.coordinates = {}
        #in addition, have a dictionary of numbers mapped to xy positions
        #playing, check if in the board
        #then check if one against the x and y coordinates that match the matching number
        for row_index, row in enumerate(board):
            new_row = []
            for col_index, number in enumerate(row.strip().split()):
                number = int(number)
                new_row.append(number)
                self.coordinates[number] = (row_index, col_index)
            self.board.append(new_row)

    def play(self, number):
        if number in self.coordinates:
            coord = self.coordinates[number]
            self.played[coord[0]][coord[1]] = True
            if self.has_won(coord):
                return self.score()
        return 0

    def has_won(self, coord):
        # vertical check
        count = 0
        for row in range(5):
            if self.played[row][coord[1]]:
                count += 1
        if count == 5:
            return True
        #horizontal check
        count = 0
        for col in range(5):
            if self.played[coord[0]][col]:
                count += 1
        if count == 5:
            return True
        return False

    def score(self):
        total = 0
        for row in range(5):
            for col in range(5):
                if not self.played[row][col]:
                    total += self.board[row][col]
        return total

class Bingo:
    def __init__(self, file_name):
        with open(file_name, 'r') as file:
            #number order is the first line, with an extra padding line
            self.numbers = [int(number) for number in file.readline().split(',')]
            file.readline()

            board_lines = file.readlines()
            self.boards = []
            #boards are 5 lines long with an extra line for padding
            while board_lines:
                self.boards.append(BingoBoard(board_lines[:5]))
                board_lines = board_lines[6:]

    def first_winning_score(self):
        for number in self.numbers:
            for board in self.boards:
                score = board.play(number)
                if score > 0:
                    return number * score
        assert False, 'NotReached'
        return -1

    def last_winning_score(self):
        playing_boards = self.boards
        for number in self.numbers:
            still_playing_boards = []
            for board in playing_boards:
                score = board.play(number)
                if score == 0:
                    still_playing_boards.append(board)
            playing_boards = still_playing_boards
            if len(playing_boards) == 1:
                break

        assert len(playing_boards) == 1, 'expected final board'
        #last board, still has to win to compute score
        for number in self.numbers: #just repeat non-winning numbers for simplicity
            score = playing_boards[0].play(number)
            if score > 0:
                return number * score
        assert False, 'NotReached'
        return -1

def main():
    sample = Bingo('aoc2021/day04/sample.txt')
    assert 4512 == sample.first_winning_score()

    squid_game = Bingo('aoc2021/day04/input.txt')
    print('Part 1: ', squid_game.first_winning_score())

    assert 1924 == sample.last_winning_score()
    print('Part 2: ', squid_game.last_winning_score())

if __name__ == '__main__':
    main()
