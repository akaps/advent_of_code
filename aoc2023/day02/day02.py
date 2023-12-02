import re

RED = 'red'
GREEN = 'green'
BLUE = 'blue'

game_regex = r'Game (\\d+)'
cube_count_regex = r'(\d+) (.*)'
game_delimiter = ': '
subset_delimiter = '; '
set_delimiter = ', '
cube_delimiter = ' '

def possible_game(subsets, count_red, count_green, count_blue):
    for subset in subsets:
        if not possible_subset(subset, count_red, count_green, count_blue):
            return False
    return True

def possible_subset(game_set, count_red, count_green, count_blue):
    cube_counts = game_set.split(set_delimiter)
    counts = {RED: 0, GREEN: 0, BLUE: 0}
    for cubes in cube_counts:
        count, color = cubes.split(cube_delimiter)
        counts[color] += int(count)
    return counts[RED] <= count_red and counts[GREEN] <= count_green and counts[BLUE] <= count_blue

def sum_possible_games(games, count_red, count_green, count_blue):
    sum_possible = 0
    for game in games:
        game_id, subsets = game.split(game_delimiter)
        subsets = subsets.strip().split(subset_delimiter)
        if possible_game(subsets, count_red, count_green, count_blue):
            _, id = game_id.split(' ')
            sum_possible += int(id)
    return sum_possible

def power_of_fewest(subsets):
    counts = {RED: 0, GREEN: 0, BLUE: 0}
    for subset in subsets:
        subset = subset.split(set_delimiter)
        for cubes in subset:
            count, color = cubes.split(cube_delimiter)
            counts[color] = max(counts[color], int(count))
    return counts[RED] * counts[GREEN] * counts[BLUE]

def fewest_possible_games(games):
    sum_fewest = 0
    for game in games:
        game_id, subsets = game.split(game_delimiter)
        subsets = subsets.strip().split(subset_delimiter)
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
