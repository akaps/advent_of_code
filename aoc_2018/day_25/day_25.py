import re
import aoc_2018.utils as utils

class Constellations:
    def __init__(self, points):
        self.clusters = []
        for point in points:
            belongs_to = None
            point = list(map(int, point))
            for cluster in self.clusters:
                for star in cluster:
                    if utils.manhattan_distance(point, star) <= 3:
                        if not belongs_to:
                            belongs_to = cluster
                            break
                        else:
                            print('have to join {A} and {B}'.format(A=belongs_to, B=cluster))
                            self.clusters.remove(cluster)
                            belongs_to.extend(cluster)
                            break
            if belongs_to:
                belongs_to.append(point)
            else:
                self.clusters.append([point])

def number_of_constellations(file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    file.close()
    lines = [re.findall('-?\d+', line) for line in lines]
    constellations = Constellations(lines)
    return len(constellations.clusters)

assert number_of_constellations('2_constellations.txt') == 2
assert number_of_constellations('3_constellations.txt') == 3
assert number_of_constellations('4_constellations.txt') == 4
assert number_of_constellations('8_constellations.txt') == 8

ANSWER = number_of_constellations('day_25_input.txt')
print('Answer to part 1: {ans}'.format(ans=ANSWER))
