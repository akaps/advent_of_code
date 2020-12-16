from aoc2020.day13.bus_stops import chinese_remainder

def test_chinese_remainder_1():
    lines = '7,13,x,x,59,x,31,19'
    assert chinese_remainder(lines) == 1068781

def test_chinese_remainder_2():
    lines = '17,x,13,19'
    assert chinese_remainder(lines) == 3417

def test_chinese_remainder_3():
    lines = '67,7,59,61'
    assert chinese_remainder(lines) == 754018

def test_chinese_remainder_4():
    lines = '67,x,7,59,61'
    assert chinese_remainder(lines) == 779210

def test_chinese_remainder_5():
    lines = '67,7,x,59,61'
    assert chinese_remainder(lines) == 1261476

def test_chinese_remainder_6():
    lines = '1789,37,47,1889'
    assert chinese_remainder(lines) == 1202161486
