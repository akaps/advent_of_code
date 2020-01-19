from aoc2018.day17.water import Buckets

def test_sample():
    sample = Buckets('sample.txt')
    sample.pour()
    assert sample.count_water() == 57
