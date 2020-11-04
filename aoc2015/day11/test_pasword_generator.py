from aoc2015.day11.password_generator import (has_consecutive_letters,
                                              has_ambiguous_letters,
                                              has_two_pairs,
                                              generate_next_password)

def test_sample_1():
    sample = 'hijklmmn'
    assert has_consecutive_letters(sample)
    assert has_ambiguous_letters(sample)
    assert not has_two_pairs(sample)

def test_sample_2():
    sample = 'abbceffg'
    assert not has_consecutive_letters(sample)
    assert not has_ambiguous_letters(sample)
    assert has_two_pairs(sample)

def test_sample_3():
    sample = 'abbcegjk'
    assert not has_consecutive_letters(sample)
    assert not has_ambiguous_letters(sample)
    assert not has_two_pairs(sample)

def test_generate_sample_1():
    result = generate_next_password('abcdefgh')
    assert result == 'abcdffaa'

def test_generate_sample_2():
    result = generate_next_password('ghijklmn')
    assert result == 'ghjaabcc'
