from aoc2019.day13 import breakout

def test_grid_alignment():
    result = [1, 2, 3, 6, 5, 4]
    parsed = breakout.parse_results(result)
    assert len(parsed) == 2
    assert parsed[0] == (1, 2, 3)
    assert parsed[1] == (6, 5, 4)

def test_initial_state():
    game = breakout.Breakout('day13/input.txt')
    result = [1, 2, 3, 6, 5, 4]
    parsed = breakout.parse_results(result)
    for x, y, z in parsed:
        game.update_tile(x, y, z)
    assert game.count_tiles(breakout.BALL) == 1
    assert game.count_tiles(breakout.HORIZ_PADDLE) == 1
