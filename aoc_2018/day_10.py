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

    def __mul__(self, incr):
        return Point(self.x * incr, self.y * incr)

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
        prev_size = math.inf
        while self.x_range * self.y_range < prev_size:
            prev_size = self.x_range * self.y_range
            print(prev_size)
            self.update(1)
        self.update(-1)
        self.show()

    def get_bounds(self):
        xs = (self.x_min(), max(self.stars, key=lambda a: a.coord.x).coord.x)
        ys = (self.y_min(), max(self.stars, key=lambda a: a.coord.y).coord.y)
        self.bounds = Point(xs, ys)
        self.x_range = self.bounds.x[1] - self.bounds.x[0]
        self.y_range = self.bounds.y[1] - self.bounds.y[0]

    def x_min(self):
        return min(self.stars, key=lambda a: a.coord.x).coord.x

    def y_min(self):
        return min(self.stars, key=lambda a: a.coord.y).coord.y

    def show(self):
        # PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
        x_min = self.x_min()
        y_min = self.y_min()
        img = Image.new('RGB', (self.x_range + 1, self.y_range + 1), 'black') # create a new black image
        pixels = img.load() # create the pixel map
        for star in self.stars:
            pixels[star.coord.x + x_min, star.coord.y + y_min] = (254, 0, 100) # set the colour accordingly
        img.show()

    def update(self, incr):
        for star in self.stars:
            star.update(incr)
        self.get_bounds()

file = open('day_10_sample.txt')
input = file.readlines()
file.close()
stars = Constellations(input)
stars.find_letters()
