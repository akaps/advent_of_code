import re

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return str((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Star:
    def __init__(self, x, y, dx, dy):
        self.coord = Point(x, y)
        self.delta_coord = Point(dx, dy)

    def update(self):
        self.coord = self.coord + self.delta_coord

    def __repr__(self):
        return str(self.coord)

    def __eq__(self, other):
        return self.coord == other.coord

class Constellations:
    def __init__(self, input):
        self.parse_stars(input)

    def parse_stars(self, input):
        self.stars = []
        for line in input:
            line = re.split('^position=<|,|> velocity=<|>$', line.strip())
            self.stars.append(Star(
                (int)(line[1]),
                (int)(line[2]),
                (int)(line[3]),
                (int)(line[4])))

    def __repr__(self):
        x_min = min(self.stars, key=lambda a: a.coord.x).coord.x
        x_max = max(self.stars, key=lambda a: a.coord.x).coord.x
        y_min = min(self.stars, key=lambda a: a.coord.y).coord.y
        y_max = max(self.stars, key=lambda a: a.coord.y).coord.y
        res = ''
        for y in range(y_min, y_max + 1):
            for x in range(x_min, x_max + 1):
                if Star(x, y, 0, 0) in self.stars:
                    res += '#'
                else:
                    res += '.'
            res += '\n'
        return res

    def update(self):
        for star in self.stars:
            star.update()

file = open('day_10_sample.txt')
input = file.readlines()
file.close()
stars = Constellations(input)
for i in range(0, 5):
    print('step {i}'.format(i=i))
    print('-----')
    print(stars)
    stars.update()
