from aoc2015.day07.wires import Wires

def test_sample():
    sample = Wires('sample.txt')
    assert sample.registers['d'] == 72
    assert sample.registers['e'] == 507
    assert sample.registers['f'] == 492
    assert sample.registers['g'] == 114
    assert sample.registers['h'] == 65412
    assert sample.registers['i'] == 65079
    assert sample.registers['x'] == 123
    assert sample.registers['y'] == 456
