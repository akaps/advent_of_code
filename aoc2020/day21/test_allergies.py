from aoc2020.day21.allergies import Foods

def test_sample():
    foods = Foods('sample.txt')
    assert len(foods.allergens) == 3
    assert foods.allergens['dairy'] == 'mxmxvkd'
    assert foods.allergens['fish'] == 'sqjhc'
    assert foods.allergens['soy'] == 'fvjkl'
    assert foods.count_allergen_free() == 5
