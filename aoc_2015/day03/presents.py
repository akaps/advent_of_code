def travel_pt1(directions):
    location = (0, 0)
    houses = {location: 1}
    for dir in directions:
        x_mod=0
        y_mod=0
        if dir == '>':
            y_mod = 1
        elif dir == '<':
            y_mod = -1
        elif dir == '^':
            x_mod = -1
        elif dir == 'v':
            x_mod = 1
        else:
            print('ERROR: Unknown direction {dir}'.format(dir=dir))
        location = (location[0] + x_mod, location[1] + y_mod)
        if location in houses:
            houses.update({location: houses[location] + 1})
        else:
            houses[location] = 1
    return len(houses)

assert travel_pt1('>') == 2
assert travel_pt1('^>v<') == 4
assert travel_pt1('^v^v^v^v^v') == 2
file = open('input.txt')
directions = file.readline().strip()
file.close()
print(travel_pt1(directions))
