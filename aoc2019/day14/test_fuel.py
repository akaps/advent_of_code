from aoc2019.day14.fuel import Recipes

def test_sample1():
    recipes = Recipes('sample1.txt')
    assert recipes.ore_for_fuel() == 31

def test_sample2():
    recipes = Recipes('sample2.txt')
    assert recipes.ore_for_fuel() == 165

def test_sample3():
    recipes = Recipes('sample3.txt')
    assert recipes.ore_for_fuel() == 13312

def test_sample4():
    recipes = Recipes('sample4.txt')
    assert recipes.ore_for_fuel() == 180697

def test_sample5():
    recipes = Recipes('sample5.txt')
    assert recipes.ore_for_fuel() == 2210736

def test_hint1():
    recipes = Recipes('hint1.txt')
    assert recipes.ore_for_fuel() == 1

def test_hint2():
    recipes = Recipes('hint2.txt')
    assert recipes.ore_for_fuel() == 20
