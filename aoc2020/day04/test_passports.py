import passports

def test_sample():
    passport_list = passports.read_passports('sample.txt')
    assert passport_list[0].is_valid()
    assert not passport_list[1].is_valid()
    assert passport_list[2].is_valid()
    assert not passport_list[3].is_valid()
    assert len(passports.passports_with_fields(passport_list)) == 2

def test_byr_valid():
    assert passports.validate_byr('2002')

def test_byr_invalid():
    assert not passports.validate_byr('2003')

def test_hgt_valid():
    assert passports.validate_hgt('60in')
    assert passports.validate_hgt('190cm')

def test_hgt_invalid():
    assert not passports.validate_hgt('190in')
    assert not passports.validate_hgt('190')

def test_hcl_valid():
    assert passports.validate_hcl('#123abc')

def test_hcl_invalid():
    assert not passports.validate_hcl('#123abz')
    assert not passports.validate_hcl('123abc')

def test_ecl_valid():
    assert passports.validate_ecl('brn')

def test_ecl_invalid():
    assert not passports.validate_ecl('wat')

def test_pid_valid():
    assert passports.validate_pid('000000001')

def test_pid_invalid():
    assert not passports.validate_pid('0123456789')
