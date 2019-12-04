import re
import utils

DELIMETER = r','
ORIGIN = (0, 0)

def generate_points(wire):
    row = col = 0
    points = {}
    current_steps = 0
    for instruction in wire:
        direction, current_distance = instruction[:1], int(instruction[1:])
        for _ in range(current_distance):
            current_steps += 1
            if direction == 'D':
                col += 1
            if direction == 'U':
                col -= 1
            if direction == 'R':
                row += 1
            if direction == 'L':
                row -= 1
            current_point = (row, col)
            current_distance = utils.manhattan_distance(current_point, ORIGIN)
            if current_point not in points:
                points[(row, col)] = current_steps
    return points

INPUT = utils.read_lines('input.txt')
WIRE_A = re.split(DELIMETER, INPUT[0])
WIRE_B = re.split(DELIMETER, INPUT[1])

POINTS_A = generate_points(WIRE_A)
POINTS_B = generate_points(WIRE_B)

LOCATION = None
SHORTEST_TRIP = -1
for point in POINTS_A:
    if point in POINTS_B:
        distance = utils.manhattan_distance(point, (0, 0))
        steps = POINTS_A[point] + POINTS_B[point]
        print('match @ {pt}\tdist={distance}\tsteps={steps}'.format(pt=point,
                                                                    distance=distance,
                                                                    steps=steps))
        if SHORTEST_TRIP < 0 or steps < SHORTEST_TRIP:
            SHORTEST_TRIP = steps
        if not LOCATION or distance < LOCATION:
            LOCATION = distance

assert LOCATION == 248
assert SHORTEST_TRIP == 28580
utils.pretty_print_answer(1, LOCATION)
utils.pretty_print_answer(2, SHORTEST_TRIP)
