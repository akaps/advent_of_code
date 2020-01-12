from aoc2019.day14.fuel import Equations

def test_sample1():
    equations = Equations('sample1.txt')
    assert equations.minimum_ore() == 31

def test_sample2():
    reactions = Equations('sample2.txt')
    assert reactions.minimum_ore() == 165

def test_sample3():
    reactions = Equations('sample3.txt')
    assert reactions.minimum_ore() == 13312

def test_sample4():
    reactions = Equations('sample4.txt')
    #off by one reaction of MNCFX
    assert reactions.minimum_ore() == 180697

def test_sample5():
    reactions = Equations('sample5.txt')
    #off by one reaction of BHXH
    assert reactions.minimum_ore() == 2210736

def test_hint1():
    reactions = Equations('hint1.txt')
    assert reactions.minimum_ore() == 1

def test_hint2():
    reactions = Equations('hint2.txt')
    assert reactions.minimum_ore() == 20
