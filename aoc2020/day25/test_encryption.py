from aoc2020.day25.encryption import transform, find_loop_size, find_encryption_key

def test_transform():
    assert transform(11, 7) == 17807724
    assert transform(8, 7) == 5764801

def test_find_loop_size():
    assert find_loop_size(17807724) == 11
    assert find_loop_size(5764801) == 8

def test_evaluate_encryption_key():
    assert transform(8, 17807724) == 14897079
    assert transform(11, 5764801)

def test_find_encryption_key():
    assert find_encryption_key(5764801, 17807724) == 14897079
