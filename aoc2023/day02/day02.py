import re

RED = 'red'
GREEN = 'green'
BLUE = 'blue'

GAME_REGEX = r'Game (\d+): (.*)$'
CUBE_REGEX = r'(\d+) (.*)'
SUBSET_DELIMITER = '; '
SET_DELIMITER = ', '

def possible_game(subsets, count_red, count_green, count_blue):
    for subset in subsets:
        if not possible_subset(subset, count_red, count_green, count_blue):
            return False
    return True

def possible_subset(game_set, count_red, count_green, count_blue):
    cube_sets = game_set.split(SET_DELIMITER)
    counts = {RED: 0, GREEN: 0, BLUE: 0}
    for cubes in cube_sets:
        count, color = re.match(CUBE_REGEX, cubes).groups()
        counts[color] += int(count)
    return counts[RED] <= count_red and counts[GREEN] <= count_green and counts[BLUE] <= count_blue

def sum_possible_games(games, count_red, count_green, count_blue):
    sum_possible = 0
    for game in games:
        game_id, subsets = re.match(GAME_REGEX, game).groups()
        subsets = subsets.split(SUBSET_DELIMITER)
        if possible_game(subsets, count_red, count_green, count_blue):
            sum_possible += int(game_id)
    return sum_possible

def power_of_fewest(subsets):
    counts = {RED: 0, GREEN: 0, BLUE: 0}
    for subset in subsets:
        subset = subset.split(SET_DELIMITER)
        for cubes in subset:
            count, color = re.match(CUBE_REGEX, cubes).groups()
            counts[color] = max(counts[color], int(count))
    return counts[RED] * counts[GREEN] * counts[BLUE]

def fewest_possible_games(games):
    sum_fewest = 0
    for game in games:
        _, subsets = re.match(GAME_REGEX, game).groups()
        subsets = subsets.split(SUBSET_DELIMITER)
        sum_fewest += power_of_fewest(subsets)
    return sum_fewest

def main():
    sample_lines = open('aoc2023/day02/sample.txt').readlines()
    assert sum_possible_games(sample_lines, 12, 13, 14) == 8
    input_lines = open('aoc2023/day02/input.txt').readlines()
    print('Answer to Part 1: ', sum_possible_games(input_lines, 12, 13, 14))

    assert fewest_possible_games(sample_lines) == 2286
    print('Answer to Part 2: ', fewest_possible_games(input_lines))

if __name__ == '__main__':
    main()
