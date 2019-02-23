import re

class ComplexPoint:
    def __init__(self):
        self.position = 0j
        self.direction = 1j #facing north, or 1j

    def turn(self, turn):
        self.direction *= turn

    def move(self, dist):
        self.position += dist * self.direction

def walk(moves):
    moves = re.split(', ', moves.strip())
    point = ComplexPoint()
    for move in moves:
        turn, dist = move[0], int(move[1:])
        if turn == 'L':
            point.turn(-1j)
        if turn == 'R':
            point.turn(1j)
        point.move(dist)
    return abs(point.position.real) + abs(point.position.imag)

def first_repeat(moves):
    moves = re.split(', ', moves.strip())
    point = ComplexPoint()
    visited = [point.position]
    for move in moves:
        turn, dist = move[0], int(move[1:])
        if turn == 'L':
            point.turn(-1j)
        if turn == 'R':
            point.turn(1j)
        for _ in range(dist):
            point.move(1)
            if point.position in visited:
                return abs(point.position.real) + abs(point.position.imag)
            visited.append(point.position)
    return -1

assert walk('R2, L3') == 5
assert walk('R2, R2, R2') == 2
assert walk('R5, L5, R5, R3') == 12

FILE = open('input.txt', 'r')
MOVES = FILE.read().strip()
FILE.close()
DIST = walk(MOVES)
print('Answer to part 1: {ans}'.format(ans=DIST))

assert first_repeat('R8, R4, R4, R8') == 4
print('Answer to part 2: {ans}'.format(ans=first_repeat(MOVES)))
