from aoc2015.day05.nice_strings import (is_nice,
                                        has_duplicate_letter,
                                        has_forbidden_pair,
                                        has_three_vowels,
                                        letter_sandwich)

def test_is_nice1():
    assert is_nice('ugknbfddgicrmopn')
    assert is_nice('aaa')
    assert not is_nice('jchzalrnumimnmhp')
    assert not has_duplicate_letter('jchzalrnumimnmhp')
    assert not has_forbidden_pair('jchzalrnumimnmhp')
    assert has_three_vowels('jchzalrnumimnmhp')

def test_is_nice2():
    assert not is_nice('haegwjzuvuyypxyu')
    assert has_forbidden_pair('haegwjzuvuyypxyu')
    assert has_duplicate_letter('haegwjzuvuyypxyu')
    assert has_three_vowels('haegwjzuvuyypxyu')

def test_is_nice_3():
    assert not is_nice('dvszwmarrgswjxmb')
    assert not has_three_vowels('dvszwmarrgswjxmb')
    assert not has_forbidden_pair('dvszwmarrgswjxmb')
    assert has_duplicate_letter('dvszwmarrgswjxmb')
    assert is_nice('ugknbfddgicrmopn')
    assert is_nice('aaa')
    assert not is_nice('jchzalrnumimnmhp')
    assert not has_duplicate_letter('jchzalrnumimnmhp')
    assert not has_forbidden_pair('jchzalrnumimnmhp')
    assert has_three_vowels('jchzalrnumimnmhp')

def test_is_nice4():
    assert not is_nice('haegwjzuvuyypxyu')
    assert has_forbidden_pair('haegwjzuvuyypxyu')
    assert has_duplicate_letter('haegwjzuvuyypxyu')
    assert has_three_vowels('haegwjzuvuyypxyu')

def test_is_nice5():
    assert not is_nice('dvszwmarrgswjxmb')
    assert not has_three_vowels('dvszwmarrgswjxmb')
    assert not has_forbidden_pair('dvszwmarrgswjxmb')
    assert has_duplicate_letter('dvszwmarrgswjxmb')

def test_letter_sandwich():
    assert letter_sandwich('qjhvhtzxzqqjkmpb')
    assert letter_sandwich('xxyxx')
    assert not letter_sandwich('uurcxstgmygtbstg')
    assert letter_sandwich('ieodomkazucvgmuy')
