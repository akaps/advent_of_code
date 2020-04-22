from aoc2015.day12.json_parser import read, parse_obj

def test_sample1():
    obj = read('[1,2,3]')
    assert parse_obj(obj) == 6
    obj = read('{"a":2,"b":4}')
    assert parse_obj(obj) == 6

def test_sample2():
    obj = read('[[[3]]]')
    assert parse_obj(obj) == 3
    obj = read('{"a":{"b":4},"c":-1}')
    assert parse_obj(obj) == 3

def test_sample3():
    obj = read('{"a":[-1,1]}')
    assert parse_obj(obj) == 0
    obj = read('[-1,{"a":1}]')
    assert parse_obj(obj) == 0

def test_sample4():
    obj = read('[]')
    assert parse_obj(obj) == 0
    obj = read('{}')
    assert parse_obj(obj) == 0

def test_ignore_red1():
    obj = read('[1,2,3]')
    assert parse_obj(obj, True) == 6

def test_ignore_red2():
    obj = read('[1,{"c":"red","b":2},3]')
    assert parse_obj(obj, True) == 4

def test_ignore_red3():
    obj = read('{"d":"red","e":[1,2,3,4],"f":5}')
    assert parse_obj(obj, True) == 0

def test_ignore_red4():
    obj = read('[1,"red",5]')
    assert parse_obj(obj, True) == 6
