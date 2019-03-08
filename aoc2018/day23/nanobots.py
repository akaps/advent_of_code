import re
import utils

class Nanobot:
    def __init__(self, loc, radius):
        self.position = loc
        self.radius = radius

class Nanobots:
    def __init__(self, file_name):
        file = open(file_name, 'r')
        lines = file.readlines()
        file.close()
        self.nanobots = []
        for line in lines:
            x, y, z, rad = map(int, re.findall('-?\d+', line))
            self.nanobots.append(Nanobot((x, y, z), rad))

    def bot_with_largest_radius(self):
        bot_with_largest_radius = self.nanobots[0]
        for bot in self.nanobots:
            if bot.radius > bot_with_largest_radius.radius:
                bot_with_largest_radius = bot
        return bot_with_largest_radius

    def nanobots_in_range(self, nanobot):
        total = 0
        for bot in self.nanobots:
            if utils.manhattan_distance(bot.position, nanobot.position) <= nanobot.radius:
                total += 1
        return total

def solve_part_1(bots):
    return bots.nanobots_in_range(bots.bot_with_largest_radius())

SAMPLE = Nanobots('sample.txt')
assert solve_part_1(SAMPLE) == 7
PROBLEM = Nanobots('input.txt')
print('Answer to part 1: {ans}'.format(ans=solve_part_1(PROBLEM)))
