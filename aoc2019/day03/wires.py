import re
import utils

DELIMETER = r','
INTERSECTION_DISTS = [248, 367, 1112, 1948, 2228]

def generate_points(wire):
    intersections = {}
    row = col = 0
    points = []
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
            current_distance = utils.manhattan_distance((row, col), (0, 0))
            if current_distance in INTERSECTION_DISTS:
                intersections[current_distance] = current_steps
            points.append((row, col))
    return points, intersections

INPUT = utils.read_lines('input.txt')
WIRE_A = re.split(DELIMETER, INPUT[0])
WIRE_B = re.split(DELIMETER, INPUT[1])

POINTS_A, INTERSECTIONS_A = generate_points(WIRE_A)
print('wire a done')
POINTS_B, INTERSECTIONS_B = generate_points(WIRE_B)
print('wire b done')

LOCATION = None
SHORTEST_TRIP = -1
for point in POINTS_A:
    if point in POINTS_B:
        distance = utils.manhattan_distance(point, (0, 0))
        print('match! {pt} {distance}'.format(pt=point, distance=distance))
        steps = POINTS_A.index(point) + 1 + POINTS_B.index(point) + 1
        print(steps)
        if SHORTEST_TRIP < 0 or steps < SHORTEST_TRIP:
            SHORTEST_TRIP = steps
        if not LOCATION or distance < LOCATION:
            LOCATION = distance

utils.pretty_print_answer(1, LOCATION)
utils.pretty_print_answer(2, SHORTEST_TRIP)
