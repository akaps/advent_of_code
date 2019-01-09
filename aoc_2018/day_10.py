import re
from PIL import Image
import copy
import math

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

    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)

class Star:
    def __init__(self, x, y, dx, dy):
        self.coord = Point(x, y)
        self.delta_coord = Point(dx, dy)

    def update(self, incr):
        self.coord = self.coord + (self.delta_coord * incr)

    def __repr__(self):
        return str(self.coord)

    def __eq__(self, other):
        return self.coord == other.coord

class Constellations:
    def __init__(self, input):
        self.parse_stars(input)
        self.get_bounds()

    def parse_stars(self, input):
        self.stars = []
        for line in input:
            line = re.split('^position=<|,|> velocity=<|>$', line.strip())
            self.stars.append(Star(
                (int)(line[1]),
                (int)(line[2]),
                (int)(line[3]),
                (int)(line[4])))

    def find_letters(self):
        i=0
        prev_size = math.inf
        curr = self.ranges.x * self.ranges.y
        while curr < prev_size:
            i+=1
            prev_size = self.ranges.x * self.ranges.y
            self.update(1)
            curr = self.ranges.x * self.ranges.y
        print(i-1)
        self.update(-1)
        self.show()

    def get_bounds(self):
        xs = (self.x_min(), max(self.stars, key=lambda a: a.coord.x).coord.x)
        ys = (self.y_min(), max(self.stars, key=lambda a: a.coord.y).coord.y)
        self.bounds = Point(xs, ys)
        self.ranges = Point(self.bounds.x[1] - self.bounds.x[0],
                            self.bounds.y[1] - self.bounds.y[0])

    def x_min(self):
        return min(self.stars, key=lambda a: a.coord.x).coord.x

    def y_min(self):
        return min(self.stars, key=lambda a: a.coord.y).coord.y

    def show(self):
        # PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
        img = Image.new('RGB', (1000, 1000), 'black') # create a new black image
        pixels = img.load() # create the pixel map
        print('image bounds = {x}, {y}'.format(x=self.ranges.x + 1, y=self.ranges.y + 1))
        print('offsets = {x}, {y}'.format(x=self.bounds.x[0], y=self.bounds.y[0]))
        for star in self.stars:
            print('coords = {x}, {y}'.format(x=star.coord.x, y=star.coord.y))
            print('adjusted coords = ({x}, {y})'.format(x=star.coord.x + self.bounds.x[0], y=star.coord.y + self.bounds.y[0]))
            pixels[star.coord.x, star.coord.y] = (254, 0, 100) # set the colour accordingly
        img.show()

    def update(self, incr):
        for star in self.stars:
            star.update(incr)
        self.get_bounds()

file = open('day_10_input.txt')
input = file.readlines()
file.close()
stars = Constellations(input)
stars.find_letters()
