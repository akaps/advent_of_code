from aoc2020.day17.cubic_life import CubicLife, get_adj

def test_initial_state():
    life = CubicLife('sample.txt')
    assert life.count_live() == 5

def test_get_adj():
    adj = get_adj((1, 2, 3, 0))
    assert len(adj) == 26

def test_cycle_1():
    life = CubicLife('sample.txt')
    life.run_cycle()
    print(life.cells)
    assert life.count_live() == 11

def test_sample():
    life = CubicLife('sample.txt')
    for _ in range(6):
        life.run_cycle()
    assert life.count_live() == 112

def test_sample_pt2():
    life = CubicLife('sample.txt')
    for _ in range(6):
        life.run_cycle(is_4d=True)
    assert life.count_live() == 848
