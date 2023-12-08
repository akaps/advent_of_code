import re

MAP_TITLE_REGEX = r'(?P<source>.*)-to-(?P<destination>.*) map'
MAPPING_REGEX = r'(?P<dest_start>\d+) (?P<source_start>\d+) (?P<range_length>\d+)'

class MapRange:
    def __init__(self, range_details: str):
        match = re.match(MAPPING_REGEX, range_details)
        assert match
        self.destination_start = int(match.group('dest_start'))
        self.source_start = int(match.group('source_start'))
        self.range_length = int(match.group('range_length'))

    def in_source_range(self, value):
        upper = self.source_start + self.range_length
        return self.source_start <= value < upper

    def in_dest_range(self, value):
        upper = self.destination_start + self.range_length
        return self.destination_start <= value < upper

    def mapping(self, value):
        return self.destination_start + (value - self.source_start)

class SeedMap:
    def __init__(self, destination):
        self.ranges = []
        self.destination = destination

    def add_range(self, range_details):
        self.ranges.append(MapRange(range_details))

    def map_value(self, value):
        for map_range in self.ranges:
            if map_range.in_source_range(value):
                return map_range.mapping(value)
        return value

class SeedMaps:
    def __init__(self, file_name):
        file = open(file_name, encoding='utf-8')
        self.seeds = [int(x) for x in re.findall(r'\d+', file.readline().strip())]
        file.readline()
        line = file.readline().strip()

        self.maps = {} #source name, maps(containing range and destination)
        while line:
            match = re.match(MAP_TITLE_REGEX, line)
            if match:
                next_map = SeedMap(match.group('destination'))
                next_line = file.readline().strip()
                while next_line:
                    next_map.add_range(next_line)
                    next_line = file.readline().strip()
                self.maps[match.group('source')] = next_map
            line = file.readline().strip()
        file.close()

    def seed_to_location(self, value):
        stage = 'seed'
        while stage != 'location':
            value = self.maps[stage].map_value(value)
            stage = self.maps[stage].destination
        assert value, 'values must map to a range'
        return value

    def lowest_location(self):
        minimum = self.seed_to_location(self.seeds[0])
        for seed in self.seeds[1:]:
            value = self.seed_to_location(seed)
            if value < minimum:
                minimum = value
        return minimum

    def lowest_by_ranges(self):
        #each seed range is a possible candidate because they map non-linearly;
        # a range within a seed range may produce smaller values than the upper or lower bound
        # we can check if there is a disconinuity if a range's slope is not 1
        # if so, we have to find the find the boundary, and keep searching with those results
        seeds = self.seeds[::2]
        ranges = self.seeds[1::2]
        minimum = self.seed_to_location(seeds[0])
        for i, seed in enumerate(seeds):
            print('next range')
            seed_range = ranges[i]
            minimum_location = self.seed_to_location(seed)
            for i in range(seed, seed + seed_range):
                if i % 1000000 == 0:
                    print(f'{i/(seed+seed_range):.2f} to go')
                candidate = self.seed_to_location(i)
                if candidate < minimum_location:
                    print(i)
                    minimum_location = candidate
            if minimum_location < minimum:
                print(seed)
                minimum = minimum_location
        return minimum

def main():
    sample = SeedMaps('aoc2023/day05/sample.txt')
    seeds = SeedMaps('aoc2023/day05/input.txt')
    assert sample.lowest_location() == 35
    print('Answer to Part 1: ', seeds.lowest_location())

    assert sample.lowest_by_ranges() == 46
    print('Answer to Part 2: ', seeds.lowest_by_ranges())

if __name__ == '__main__':
    main()
