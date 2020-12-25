from aoc2020.day24.hex_tiles import HexTiles

def test_round_1():
    tiles = HexTiles('sample.txt')
    assert tiles.count_black_tiles() == 10
    tiles.next_generation()
    assert tiles.count_black_tiles() == 15

def test_round_10():
    tiles = HexTiles('sample.txt')
    assert tiles.count_black_tiles() == 10
    tiles.next_generation()
    assert tiles.count_black_tiles() == 15
    tiles.next_generation()
    assert tiles.count_black_tiles() == 12
    tiles.next_generation()
    assert tiles.count_black_tiles() == 25
    tiles.next_generation()
    assert tiles.count_black_tiles() == 14
    tiles.next_generation()
    assert tiles.count_black_tiles() == 23
    tiles.next_generation()
    assert tiles.count_black_tiles() == 28
    tiles.next_generation()
    assert tiles.count_black_tiles() == 41
    tiles.next_generation()
    assert tiles.count_black_tiles() == 37
    tiles.next_generation()
    assert tiles.count_black_tiles() == 49
    tiles.next_generation()
    assert tiles.count_black_tiles() == 37

def test_round_100():
    tiles = HexTiles('sample.txt')
    assert tiles.count_black_tiles() == 10
    tiles.run_simulation(20)
    assert tiles.count_black_tiles() == 132
    tiles.run_simulation(10)
    assert tiles.count_black_tiles() == 259
    tiles.run_simulation(10)
    assert tiles.count_black_tiles() == 406
    tiles.run_simulation(10)
    assert tiles.count_black_tiles() == 566
    tiles.run_simulation(10)
    assert tiles.count_black_tiles() == 788
    tiles.run_simulation(10)
    assert tiles.count_black_tiles() == 1106
    tiles.run_simulation(10)
    assert tiles.count_black_tiles() == 1373
    tiles.run_simulation(10)
    assert tiles.count_black_tiles() == 1844
    tiles.run_simulation(10)
    assert tiles.count_black_tiles() == 2208
