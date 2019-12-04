import re
import utils

DELIMETER = r','
insersection_dists = [248, 367, 1112, 1948, 2228]

def generate_points(wire):
    intersections = {}
    x = y = 0
    points = []
    steps = 0
    for instruction in wire:
        direction, distance = instruction[:1], int(instruction[1:])
        for _ in range(distance):
            steps += 1
            if direction == 'D':
                y += 1
            if direction == 'U':
                y -= 1
            if direction == 'R':
                x += 1
            if direction == 'L':
                x -= 1
            distance = utils.manhattan_distance((x, y), (0, 0))
            if distance in insersection_dists:
                intersections[distance] = steps
            points.append((x, y))
    return points, intersections

input = utils.read_lines('input.txt')
wire_a = re.split(DELIMETER, input[0])
wire_b = re.split(DELIMETER, input[1])

points_a, intersections_a = generate_points(wire_a)
print('wire a done')
points_b, intersections_b = generate_points(wire_b)
print('wire b done')

location = None #very big number
shortest_trip = -1
for point in points_a:
    #print(point)
    if point in points_b:
        distance = utils.manhattan_distance(point, (0, 0))
        print('match! {pt} {distance}'.format(pt=point, distance=distance))
        steps = points_a.index(point) + 1 + points_b.index(point) + 1
        print(steps)
        if shortest_trip < 0 or steps < shortest_trip:
            shortest_trip = steps
        if not location or distance < location:
            location = distance

utils.pretty_print_answer(1, location)
utils.pretty_print_answer(2, shortest_trip)
