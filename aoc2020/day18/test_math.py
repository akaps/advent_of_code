from aoc2020.day18.math import calculate
def test_sample1():
    assert calculate('1 + 2 * 3 + 4 * 5 + 6') == 71

def test_sample2():
    assert calculate('1 + (2 * 3) + (4 * (5 + 6))') == 51

def test_sample3():
    assert calculate('2 * 3 + (4 * 5)') == 26

def test_sample4():
    assert calculate('5 + (8 * 3 + 9 + 3 * 4 * 3)') == 437

def test_sample5():
    assert calculate('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))') == 12240

def test_sample6():
    assert calculate('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == 13632
