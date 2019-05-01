import utils

class Dancing:
    def __init__(self, initial_state):
        self.programs = list(initial_state)

    def spin(self, number):
        pivot = len(self.programs) - number
        self.programs = self.programs[pivot:] + self.programs[:pivot]

    def exchange(self, index_a, index_b):
        swap = self.programs[index_a]
        self.programs[index_a] = self.programs[index_b]
        self.programs[index_b] = swap

    def partner(self, program_a, program_b):
        index_a = self.programs.index(program_a)
        index_b = self.programs.index(program_b)
        self.exchange(index_a, index_b)

    def __repr__(self):
        return ''.join(self.programs)

    def perform_dance(self, moves):
        for move in moves:
            action = move[0]
            move = move[1:]
            if action == 's':
                number = int(move)
                self.spin(number)
            elif action == 'x':
                a, b = [int(x) for x in move.split('/')]
                self.exchange(a, b)
            elif action == 'p':
                a, b = move.split('/')
                self.partner(a, b)

DANCE = Dancing('abcde')
DANCE.spin(1)
assert str(DANCE) == 'eabcd'
DANCE.exchange(3, 4)
assert str(DANCE) == 'eabdc'
DANCE.partner('e', 'b')
assert str(DANCE) == 'baedc'

FILE = open('input.txt')
MOVES = FILE.readline().strip().split(',')
FILE.close()

DANCE = Dancing('abcdefghijklmnop')
DANCE.perform_dance(MOVES)
utils.pretty_print_answer(1, DANCE)

DANCE = Dancing('abcdefghijklmnop')
PREVIOUS_MOVES = []
loop_start = -1
for t in range(1000000000):
    if str(DANCE) in PREVIOUS_MOVES:
        if loop_start < 1:
            loop_start = t
        break
    else:
        PREVIOUS_MOVES.append(str(DANCE))
        DANCE.perform_dance(MOVES)

RES_OFFSET = 1000000000 % loop_start
PREV_INDEX = PREVIOUS_MOVES.index(str(DANCE))
NEXT_INDEX = (PREV_INDEX + RES_OFFSET) % len(PREVIOUS_MOVES)
DANCE.programs = PREVIOUS_MOVES[NEXT_INDEX]
utils.pretty_print_answer(2, DANCE)
