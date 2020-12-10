import aoc2020.day10.joltages as jolts

def test_part1_sample1():
    joltages = jolts.read_joltages('sample1.txt')
    diffs = jolts.part_1(joltages)
    assert diffs[1] == 7
    assert diffs[3] == 5

def test_part1_sample2():
    joltages = jolts.read_joltages('sample2.txt')
    diffs = jolts.part_1(joltages)
    assert diffs[1] == 22
    assert diffs[3] == 10

def test_part2_sample1():
    joltages = jolts.read_joltages('sample1.txt')
    connections = jolts.all_connections(joltages)
    assert jolts.count_connections(connections, 0) == 8

def test_part2_sample2():
    joltages = jolts.read_joltages('sample2.txt')
    connections = jolts.all_connections(joltages)
    assert jolts.count_connections(connections, 0) == 19208
