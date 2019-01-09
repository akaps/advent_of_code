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

    def find_letters(self):
        x_range, y_range = self.get_bounds()
        prev_size = math.inf
        while x_range * y_range < prev_size:
            prev_size = x_range * y_range
            print(prev_size)
            prev = copy.deepcopy(self.stars)
            self.update()
            x_range, y_range = self.get_bounds()
        self.stars = prev
        self.show()

    def get_bounds(self):
        x_min = self.x_min()
        x_max = max(self.stars, key=lambda a: a.coord.x).coord.x
        y_min = self.y_min()
        y_max = max(self.stars, key=lambda a: a.coord.y).coord.y
        x_range = x_max - x_min + 1
        y_range = y_max - y_min + 1
        return x_range, y_range

    def x_min(self):
        return min(self.stars, key=lambda a: a.coord.x).coord.x

    def y_min(self):
        return min(self.stars, key=lambda a: a.coord.y).coord.y

    def show(self):
        # PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
        x_range, y_range = self.get_bounds()
        x_min = self.x_min()
        y_min = self.y_min()
        img = Image.new('RGB', (x_range, y_range), 'black') # create a new black image
        pixels = img.load() # create the pixel map
        for star in self.stars:
            pixels[star.coord.x + x_min, star.coord.y + y_min] = (255, 0, 100) # set the colour accordingly
        img.show()

    def update(self):
        for star in self.stars:
            star.update()

file = open('day_10_input.txt')
input = file.readlines()
file.close()
stars = Constellations(input)
stars.find_letters()
