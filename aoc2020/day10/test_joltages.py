from aoc2020.day10.joltages import Jolts

def test_part1_sample1():
    jolts = Jolts('sample1.txt')
    diffs = jolts.part_1()
    assert diffs[1] == 7
    assert diffs[3] == 5

def test_part1_sample2():
    jolts = Jolts('sample2.txt')
    diffs = jolts.part_1()
    assert diffs[1] == 22
    assert diffs[3] == 10

def test_part2_sample1():
    jolts = Jolts('sample1.txt')
    assert jolts.count_connections() == 8

def test_part2_sample2():
    jolts = Jolts('sample2.txt')
    assert jolts.count_connections() == 19208
