import re
import utils
CID = 'cid'

def validate_byr(val):
    val = int(val)
    return 2002 >= val >= 1920

def validate_iyr(val):
    val = int(val)
    return 2020 >= val >= 2010

def validate_eyr(val):
    val = int(val)
    return 2030 >= val >= 2020

def validate_hgt(val):
    if 'cm' not in val and 'in' not in val:
        return False
    number = int(val[:-2])
    unit = val[-2:]
    assert len(unit) == 2
    if unit == 'cm':
        return 193 >= number >= 150
    if unit == 'in':
        return 76 >= number >= 59
    return False

def validate_hcl(val):
    color_regex = r'#[0-9a-f]{6}'
    return re.match(color_regex, val)

def validate_ecl(val):
    return val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def validate_pid(val):
    pid_regex = r'^[0-9]{9}$'
    return re.match(pid_regex, val)

KEYS = {
    'byr' : validate_byr,
    'iyr' : validate_iyr,
    'eyr' : validate_eyr,
    'hgt' : validate_hgt,
    'hcl' : validate_hcl,
    'ecl' : validate_ecl,
    'pid' : validate_pid
}

class Passport:
    def __init__(self):
        self.fields = {}

    def add_field(self, field_key, field_val):
        self.fields[field_key] = field_val
        assert len(self.fields) <= 8

    def is_valid(self):
        if len(self.fields) == 8:
            return True
        return len(self.fields) == 7 and CID not in self.fields

    def validate_keys(self):
        for key, val in self.fields.items():
            if key != CID and not KEYS[key](val):
                return False
        return True

def read_passports(file_name):
    passports = []
    lines = utils.read_lines(file_name)
    next_passport = Passport()
    while lines:
        next_line = lines.pop(0)
        if next_line:
            pairs = next_line.split(' ')
            for pair in pairs:
                key, val = pair.split(':')
                next_passport.add_field(key, val)
        else:
            passports.append(next_passport)
            next_passport = Passport()
    passports.append(next_passport)
    return passports

def passports_with_fields(passports):
    result = []
    for passport in passports:
        if passport.is_valid():
            result.append(passport)
    return result

def validate_passports(passports):
    result = []
    for passport in passports:
        if passport.validate_keys():
            result.append(result)
    return result

def main():
    passports = read_passports('input.txt')
    assert passports[0].is_valid()
    assert not passports[1].is_valid()
    passports = passports_with_fields(passports)
    utils.pretty_print_answer(1, len(passports))

    passports = validate_passports(passports)
    utils.pretty_print_answer(2, len(passports))

if __name__ == "__main__":
    main()
