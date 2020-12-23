from aoc2020.day23.cups import Cups

def test_initial_state():
    cups = Cups('389125467')
    assert cups.cup_order() == '25467389'

def test_round1():
    cups = Cups('389125467')
    cups.play_round()
    assert cups.cup_order() == '54673289'

def test_round10():
    cups = Cups('389125467')
    cups.play_game(10)
    assert cups.cup_order() == '92658374'

def test_round100():
    cups = Cups('389125467')
    cups.play_game(100)
    assert cups.cup_order() == '67384529'

def test_cup_hash_start():
    cups = Cups('389125467')
    assert cups.cup_hash() == 10

def test_cup_hash_1_round():
    cups = Cups('389125467')
    cups.play_round()
    assert cups.cup_hash() == 20

def test_cup_hash_10_rounds():
    cups = Cups('389125467')
    cups.play_game(10)
    assert cups.cup_hash() == 18

def test_cup_hash_100_rounds():
    cups = Cups('389125467')
    cups.play_game(100)
    assert cups.cup_hash() == 42

def test_big_sample():
    cups = Cups('389125467', is_big=True)
    cups.play_game(10000000)
    assert cups.cup_hash() == '149245887792'
