import re
from collections import defaultdict
import utils

BAG = 'shiny gold'
BAG_REGEX = r'(\d+) (\w+ \w+)'
RULES_REGEX = r'(?P<container>\w+ \w+) bags contain (?P<contained>((\d) (\w+ \w+) bags?, )*(?P<tail>(\d+) (\w+ \w+)|no other) bags?)\.'

CONTAIN = ' bags contain '
BAG_SEPERATOR = ' bag, '
COMMA = ', '
NO_BAGS = 'no other bags'

def contained_bags(contained_string):
    bags = {}
    if contained_string != NO_BAGS:
        contained = contained_string.split(COMMA)
        for bag in contained:
            count, color = re.match(BAG_REGEX, bag).groups()
            bags[color] = int(count)
    return bags

class Bags:
    def __init__(self, file_name):
        self.rules = defaultdict(lambda: [])
        lines = utils.read_lines(file_name)
        for line in lines:
            groups = re.match(RULES_REGEX, line)
            self.rules[groups['container']] = contained_bags(groups['contained'])

    def contain_count(self, goal_color):
        count = 0
        to_process = [goal_color]
        visited = []
        while to_process:
            processing_color = to_process.pop(0)
            for container_color, contained in self.rules.items():
                for contained_color in contained.keys():
                    if container_color not in to_process and container_color not in visited and contained_color == processing_color:
                        count += 1
                        to_process.append(container_color)
            visited.append(processing_color)
        return count

    def count_bags(self, goal_color):
        total = -1
        to_process = [(goal_color, 1)]
        while to_process:
            processing_color, process_count = to_process.pop(0)
            total += process_count
            contained = self.rules[processing_color]
            for bag_color, count in contained.items():
                to_process.append((bag_color, process_count * count))
        return total

def main():
    rules = Bags('input.txt')
    count = rules.contain_count(BAG)
    utils.pretty_print_answer(1, count)

    total = rules.count_bags(BAG)
    utils.pretty_print_answer(2, total)

if __name__ == "__main__":
    main()
