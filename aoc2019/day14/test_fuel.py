from aoc2019.day14.fuel import Recipes

def test_sample1():
    recipes = Recipes('day14/sample1.txt')
    assert recipes.ore_for_fuel() == 31

def test_sample2():
    recipes = Recipes('day14/sample2.txt')
    assert recipes.ore_for_fuel() == 165

def test_sample3():
    recipes = Recipes('day14/sample3.txt')
    assert recipes.ore_for_fuel() == 13312

def test_sample4():
    recipes = Recipes('day14/sample4.txt')
    assert recipes.ore_for_fuel() == 180697

def test_sample5():
    recipes = Recipes('day14/sample5.txt')
    assert recipes.ore_for_fuel() == 2210736

def test_hint1():
    recipes = Recipes('day14/hint1.txt')
    assert recipes.ore_for_fuel() == 1

def test_hint2():
    recipes = Recipes('day14/hint2.txt')
    assert recipes.ore_for_fuel() == 20
