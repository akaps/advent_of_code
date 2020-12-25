import utils
from aoc2020.day06 import customs

def test_part_1():
    forms = utils.read_groups('sample.txt')
    assert len(forms) == 5
    yeses = customs.get_yes_answers(forms)
    assert (len(yeses)) == 5
    assert customs.yes_total(yeses) == 11

def test_part_2():
    forms = utils.read_groups('sample.txt')
    assert len(forms) == 5
    forms = customs.get_intersection_forms(forms)
    assert customs.yes_total(forms) == 6
