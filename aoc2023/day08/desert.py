import re
import math

NAME_REGEX = r'[A-Z0-9]{3}'

LEFT = 'L'
RIGHT = 'R'
START = 'AAA'
END = 'ZZZ'

GHOST_START = r'[A-Z0-9]{2}A'
GHOST_END = r'[A-Z0-9]{2}Z'

def simultaneous(steps: list[int]):
    result = (steps[0] * steps[1]) // math.gcd(steps[0], steps[1])
    for i in range(2, len(steps)):
        result = (result * steps[i]) // math.gcd(result, steps[i])
    return result

class Desert:
    def __init__(self, file_name):
        lines = open(file_name, encoding='utf-8').readlines()
        self.directions = lines[0].strip()

        self.map = {}
        for index in range(2, len(lines)):
            line = lines[index].strip()
            source, left, right = re.findall(NAME_REGEX, line)
            self.map[source] = {LEFT: left, RIGHT: right}

    def walk(self, start:str=START, ends:list[str]=[END]):
        count = 0
        position = start
        while position not in ends:
            next_dir = self.directions[count % len(self.directions)]
            position = self.map[position][next_dir]
            count += 1
        return count

    def ghost_walk(self):
        starts = [location for location in self.map.keys() if re.match(GHOST_START, location)]
        ends = [location for location in self.map.keys() if re.match(GHOST_END, location)]
        distances = []
        for start in starts:
            distances.append(self.walk(start, ends))
        return simultaneous(distances)

def main():
    sample = Desert('aoc2023/day08/sample.txt')
    assert sample.walk() == 2

    sample2 = Desert('aoc2023/day08/sample2.txt')
    assert sample2.walk() == 6

    desert = Desert('aoc2023/day08/input.txt')
    print('Answer to part 1: ', desert.walk())
    print('Hello World!')

    sample3 = Desert('aoc2023/day08/sample3.txt')
    assert sample3.ghost_walk() == 6
    print('Answer to part 2: ', desert.ghost_walk())

if __name__ == '__main__':
    main()
