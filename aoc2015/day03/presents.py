import utils

def get_mods(direction):
    if direction == '>':
        return 0, 1
    elif direction == '<':
        return 0, -1
    elif direction == '^':
        return -1, 0
    elif direction == 'v':
        return 1, 0
    else:
        print('ERROR: Unknown direction {dir}'.format(dir=direction))
        return 0, 0

def update_location(loc, direction):
    x_mod, y_mod = get_mods(direction)
    return (loc[0] + x_mod, loc[1] + y_mod)

def process_location(loc, houses):
    if loc in houses:
        houses.update({loc: houses[loc] + 1})
    else:
        houses[loc] = 1

def travel_pt1(directions):
    location = (0, 0)
    houses = {location: 1}
    for direction in directions:
        location = update_location(location, direction)
        process_location(location, houses)
    return len(houses)

def travel_pt2(directions):
    location_even = (0, 0)
    location_odd = (0, 0)
    houses = {location_even: 2}
    for direction in enumerate(directions):
        if direction[0] % 2:
            location_even = update_location(location_even, direction[1])
            process_location(location_even, houses)
        else:
            location_odd = update_location(location_odd, direction[1])
            process_location(location_odd, houses)
    return len(houses)

def test_part_1():
    assert travel_pt1('>') == 2
    assert travel_pt1('^>v<') == 4
    assert travel_pt1('^v^v^v^v^v') == 2

def test_part_2():
    assert travel_pt2('^v') == 3
    assert travel_pt2('^>v<') == 3
    assert travel_pt2('^v^v^v^v^v') == 11

FILE = open('input.txt')
DIRECTIONS = FILE.readline().strip()
FILE.close()
utils.pretty_print_answer(1, travel_pt1(DIRECTIONS))
utils.pretty_print_answer(2, travel_pt2(DIRECTIONS))
