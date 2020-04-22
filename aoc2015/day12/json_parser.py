import json
import utils

RED = 'red'

def read(json_file):
    return json.loads(json_file)

def parse_obj(json_obj, ignore_red=False):
    if isinstance(json_obj, dict):
        return parse_dict(json_obj, ignore_red)
    if isinstance(json_obj, list):
        return parse_list(json_obj, ignore_red)
    raise Exception('input was not proper JSON format', json_obj)

def parse_dict(json_obj, ignore_red):
    assert isinstance(json_obj, dict)
    total = 0
    if ignore_red and (RED in json_obj.keys() or RED in json_obj.values()):
        return 0
    for key, val in json_obj.items():
        if isinstance(key, int):
            total += key
        if isinstance(val, int):
            total += val
        if isinstance(key, list):
            total += parse_list(key, ignore_red)
        if isinstance(key, dict):
            total += parse_dict(key, ignore_red)
        if isinstance(val, list):
            total += parse_list(val, ignore_red)
        if isinstance(val, dict):
            total += parse_dict(val, ignore_red)
    return total

def parse_list(json_obj, ignore_red):
    assert not isinstance(json_obj, dict)
    total = 0
    for obj in json_obj:
        if isinstance(obj, int):
            total += obj
        if isinstance(obj, (list)):
            total += parse_list(obj, ignore_red)
        if isinstance(obj, dict):
            total += parse_dict(obj, ignore_red)
    return total

def main():
    text_file = open('input.txt')
    text = text_file.readline()
    text_file.close()
    problem = read(text)
    utils.pretty_print_answer(1, parse_obj(problem))
    utils.pretty_print_answer(2, parse_obj(problem, True))

if __name__ == '__main__':
    main()
