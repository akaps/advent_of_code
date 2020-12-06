from aoc2020.day06 import customs

def test_part_1():
    forms = customs.get_forms('sample.txt')
    assert len(forms) == 5
    assert customs.yes_answers(forms) == 11

def test_part_2():
    forms = customs.get_intersection_forms('sample.txt')
    assert len(forms) == 5
    assert customs.yes_answers(forms) == 6
