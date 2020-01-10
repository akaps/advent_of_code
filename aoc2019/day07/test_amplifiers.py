from aoc2019.day07.amplifiers import Amplifiers

def test_amplifier_sample_1():
    amplifiers = Amplifiers('sample1.txt')
    assert amplifiers.find_largest_output() == 43210

def test_amplifier_sample_2():
    amplifiers = Amplifiers('sample2.txt')
    assert amplifiers.find_largest_output() == 54321

def test_amplifier_sample_3():
    amplifiers = Amplifiers('sample3.txt')
    assert amplifiers.find_largest_output() == 65210
