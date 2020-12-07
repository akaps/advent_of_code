import re
import utils
from aoc2020.day07.bags import BagRules, RULES_REGEX

def test_matches():
    lines = utils.read_lines('sample.txt')
    for line in lines:
        assert re.match(RULES_REGEX, line)

def test_sample_nonexistent():
    rules = BagRules('sample.txt')
    assert rules.contain_count('rainbow') == 0

def test_sample_bright_white():
    rules = BagRules('sample.txt')
    assert rules.contain_count('bright white') == 2

def test_sample_muted_yellow():
    rules = BagRules('sample.txt')
    assert rules.contain_count('muted yellow') == 2

def test_sample_shiny_gold():
    rules = BagRules('sample.txt')
    assert rules.contain_count('shiny gold') == 4

def test_sample_black():
    rules = BagRules('sample.txt')
    assert rules.contain_count('dotted black') == 7

def test_sample_blue():
    rules = BagRules('sample.txt')
    assert rules.contain_count('faded blue') == 10
