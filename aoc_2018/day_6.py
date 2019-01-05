import re

class Coordinates:

    def __init__(self, coordinates):
        self.coordinates = []
        self.generate_coordinates(coordinates)

    def generate_coordinates(self, coordinates):
        #infinite grid is bounded by border points.
        #they can be ignored OR used to define the rectangle you want to look in
        for coord in coordinates:
            (x, y) = re.split(', ', coord.strip())
            self.coordinates.append(((int)(x), (int)(y)))
        xs = lambda a: a[0]
        ys = lambda a: a[1]
        self.x_min = min(self.coordinates, key=xs)[0]
        self.x_max = max(self.coordinates, key=xs)[0]
        self.y_min = min(self.coordinates, key=ys)[1]
        self.y_max = max(self.coordinates, key=ys)[1]

    def bounded(self, coordinate):
        return (self.x_min != coordinate[0] or
                self.x_max != coordinate[0] or
                self.y_min != coordinate[1] or
                self.y_max != coordinate[1])

    def calculate_areas(self):
        res = {}
        for coord in self.coordinates:
            res[coord] = 0
        for x in range(self.x_min, self.x_max):
            for y in range(self.y_min, self.y_max):
                dist = {}
                for coordinate in self.coordinates:
                    dist[coordinate] = manhattan_distance(coordinate, (x, y))
                closest = min(dist, key=lambda key: dist[key])
                if self.bounded(closest):
                    res.update({closest: res[closest] + 1})
        winner = max(res, key=lambda key: res[key])
        return (winner, res[winner])

    def find_safest_area(self):
        total = 0
        for x in range(self.x_min, self.x_max):
            for y in range(self.y_min, self.y_max):
                dist = []
                for coordinate in self.coordinates:
                    dist.append(manhattan_distance(coordinate, (x,y )))
                total_dist = sum(dist)
                if total_dist < 10000:
                    total += 1
        return total

def manhattan_distance(origin, dest):
    return abs(origin[0] - dest[0]) + abs(origin[1] - dest[1])

file = open('day_6_input.txt')
origins = file.readlines()
file.close()
res = Coordinates(origins)
point, area = res.calculate_areas()
print('largest area at {point}, totals {area}'.format(point=point, area=area))
print('safest region is {area} units large'.format(area=res.find_safest_area()))
