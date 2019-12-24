from aoc2015.day03 import presents

def test_part_1():
    assert presents.travel_pt1('>') == 2
    assert presents.travel_pt1('^>v<') == 4
    assert presents.travel_pt1('^v^v^v^v^v') == 2

def test_part_2():
    assert presents.travel_pt2('^v') == 3
    assert presents.travel_pt2('^>v<') == 3
    assert presents.travel_pt2('^v^v^v^v^v') == 11
