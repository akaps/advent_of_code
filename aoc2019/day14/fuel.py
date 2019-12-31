import re
from collections import defaultdict
import math
import utils

ARROW = r' => '
COMMA = r', '
SPACE = r' '

FUEL = 'FUEL'
ORE = 'ORE'

class Chemical:
    def __init__(self, count, name):
        self.count = int(count)
        self.name = name

    def __repr__(self):
        return '{n} {name}'.format(n=self.count, name=self.name)

class Recipe:
    def __init__(self, recipe_line):
        inputs, output = re.split(ARROW, recipe_line)
        out_count, out_name = re.split(SPACE, output)
        self.output = Chemical(out_count, out_name)
        self.inputs = []
        for input_str in re.split(COMMA, inputs):
            count, name = re.split(SPACE, input_str)
            self.inputs.append(Chemical(count, name))

    def __repr__(self):
        return '{inputs} to make {output}'.format(inputs=self.inputs, output=self.output)

class Recipes:
    def __init__(self, recipe_file_name):
        self.recipe_list = {}
        lines = utils.read_lines(recipe_file_name)
        for line in lines:
            recipe = Recipe(line)
            self.recipe_list[recipe.output.name] = recipe

    def scale_recipe(self, ingredient, leftover_ingredients):
        required_ingredients = []
        if leftover_ingredients[ingredient.name] > ingredient.count:
            leftover_ingredients[ingredient.name] -= ingredient.count
            return required_ingredients, leftover_ingredients
        count = ingredient.count - leftover_ingredients[ingredient.name]
        recipe = self.recipe_list[ingredient.name]
        scale = int(math.ceil(count / recipe.output.count))
        leftover_ingredients[ingredient.name] += (scale * recipe.output.count) - count
        for req_input in recipe.inputs:
            required_ingredients.append(Chemical(scale * req_input.count, req_input.name))
        return required_ingredients, leftover_ingredients


    def ore_for_fuel(self):
        num_ore = 0
        to_process = [Chemical(1, FUEL)]
        leftovers = defaultdict(lambda: 0)
        while to_process:
            print('processing items {list}'.format(list=to_process))
            next_ingredient = to_process.pop(0)
            print('handling: {next}'.format(next=next_ingredient))
            print('currently have: {processed}'.format(processed=leftovers))
            if next_ingredient.name == ORE:
                num_ore += next_ingredient.count
            else:
                ingredients, leftovers = self.scale_recipe(next_ingredient, leftovers)
                to_process.extend(ingredients)
        return num_ore

PROBLEM = Recipes('input.txt')
utils.pretty_print_answer(1, PROBLEM.ore_for_fuel())
