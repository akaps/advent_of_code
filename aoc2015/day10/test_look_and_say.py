from aoc2015.day10.look_and_say import run_length_encode

def test_sample_1():
    assert run_length_encode('1') == '11'

def test_sample_2():
    assert run_length_encode('11') == '21'

def test_sample_3():
    assert run_length_encode('21') == '1211'

def test_sample_4():
    assert run_length_encode('1211') == '111221'

def test_sample_5():
    assert run_length_encode('111221') == '312211'
