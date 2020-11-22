from aoc2017.day09 import stream

def test_remove_garbage_1():
    assert stream.remove_garbage('<>') == ''

def test_remove_garbage_2():
    assert stream.remove_garbage('<random characters>') == ''

def test_remove_garbage_3():
    assert stream.remove_garbage('<<<<>') == ''

def test_remove_garbage_4():
    assert stream.remove_garbage('<{!>}>') == ''

def test_remove_garbage_5():
    assert stream.remove_garbage('<!!>') == ''

def test_remove_garbage_6():
    assert stream.remove_garbage('<!!!>>') == ''

def test_remove_garbage_7():
    assert stream.remove_garbage('<{o"i!a,<{i<a>') == ''

def test_score_1():
    assert stream.score('{}') == 1

def test_score_2():
    assert stream.score('{{{}}}') == 6

def test_score_3():
    assert stream.score('{{},{}}') == 5

def test_score_4():
    assert stream.score('{{{},{},{{}}}}') == 16

def test_score_5():
    assert stream.score('{<a>,<a>,<a>,<a>}') == 1

def test_score_6():
    assert stream.score('{{<ab>},{<ab>},{<ab>},{<ab>}}') == 9

def test_score_7():
    assert stream.score('{{<!!>},{<!!>},{<!!>},{<!!>}}') == 9

def test_score_8():
    assert stream.score('{{<a!>},{<a!>},{<a!>},{<ab>}}') == 3