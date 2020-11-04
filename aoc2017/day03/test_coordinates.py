from aoc2017.day03.coordinates import distance_for_number

def test_origin():
    assert distance_for_number(1) == 0

def test_down_left():
    assert distance_for_number(12) == 3

def test_up():
    assert distance_for_number(23) == 2

def test_1024():
    assert distance_for_number(1024) == 31
