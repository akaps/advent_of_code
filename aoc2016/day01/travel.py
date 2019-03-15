import re
from complex_vector import ComplexVector

def walk(moves):
    moves = re.split(', ', moves.strip())
    point = ComplexVector()
    for move in moves:
        turn, dist = parse_move(move)
        handle_turn(turn, point)
        point.translate(dist)
    return manhattan_distance(point)

def parse_move(move):
    return move[0], int(move[1:])

def manhattan_distance(point):
    return abs(point.magnitude.real) + abs(point.magnitude.imag)

def handle_turn(turn, point):
    if turn == 'L':
        point.rotate(-1j)
    if turn == 'R':
        point.rotate(1j)

def first_repeat(moves):
    moves = re.split(', ', moves.strip())
    point = ComplexVector()
    visited = [point.magnitude]
    for move in moves:
        turn, dist = parse_move(move)
        handle_turn(turn, point)
        for _ in range(dist):
            point.translate(1)
            if point.magnitude in visited:
                return manhattan_distance(point)
            visited.append(point.magnitude)
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
