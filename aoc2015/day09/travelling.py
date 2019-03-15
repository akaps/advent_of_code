import re
import math
import operator
import utils

class Cities:
    def __init__(self, file_name):
        file = open(file_name)
        lines = file.readlines()
        file.close()
        self.cities = {}
        self.populate_cities(lines)

    def populate_cities(self, lines):
        for line in lines:
            start, end, dist = re.findall(r'(\w+) to (\w+) = (\d+)', line)[0]
            dist = int(dist)
            if start not in self.cities:
                self.cities[start] = {}
            if end not in self.cities:
                self.cities[end] = {}
            self.cities[start].update({end: dist})
            self.cities[end].update({start: dist})

    def solve_distance(self, longest=False):
        curr_dist = -math.inf if longest else math.inf
        for city in self.cities:
            dist = self.total_distance(city, longest)
            if not longest and dist < curr_dist:
                curr_dist = dist
            if longest and dist > curr_dist:
                curr_dist = dist
        return curr_dist

    def total_distance(self, city, longest=False):
        dist = 0
        to_process = city
        processed = [to_process]
        while len(processed) != len(self.cities):
            #pick closest city that hasn't already been visited
            next_cities = [item for item in self.cities[to_process].items() if item[0] not in processed]
            closest = sorted(next_cities, key=operator.itemgetter(1), reverse=longest)[0]
            dist += closest[1]
            to_process = closest[0]
            processed.append(to_process)
        return dist

SAMPLE = Cities('sample.txt')
assert SAMPLE.solve_distance() == 605

PROBLEM = Cities('input.txt')
utils.pretty_print_answer(1, PROBLEM.solve_distance())

assert SAMPLE.solve_distance(True) == 982
utils.pretty_print_answer(2, PROBLEM.solve_distance(True))
