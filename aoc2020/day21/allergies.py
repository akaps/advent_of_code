from copy import deepcopy
import utils

SPACE = ' '
COMMA = ', '
CLOSE_APREN = ')'
CONTAINS = ' (contains '

class Food:
    def __init__(self, food_line):
        ingredients, allergens = food_line.split(CONTAINS)
        self.ingredients = ingredients.split(SPACE)
        self.allergens = allergens.split(COMMA)
        self.allergens[-1] = self.allergens[-1][:-1]

    def __repr__(self):
        return 'ingredients: {ing}, known allergens {all}'.format(
            ing=self.ingredients,
            all=self.allergens)

class Foods:
    def __init__(self, file_name):
        self.foods = []
        lines = utils.read_lines(file_name)
        for line in lines:
            self.foods.append(Food(line))
        self.allergens = self.find_allergens()

    def candidate_allergens(self):
        allergens = {}
        for food in self.foods:
            for allergen in food.allergens:
                if allergen in allergens:
                    allergens[allergen] &= set(food.ingredients)
                else:
                    allergens[allergen] = set(food.ingredients)
        return allergens

    def find_allergens(self):
        candidates = self.candidate_allergens()
        to_process = list(candidates.keys())
        allergens = {}
        while to_process:
            next_allergen = to_process.pop(0)
            if len(candidates[next_allergen]) == 1:
                ingredient = candidates[next_allergen].pop()
                allergens[next_allergen] = ingredient
                for other_allergen in candidates.values():
                    other_allergen.discard(ingredient)
            else:
                to_process.append(next_allergen)
        return allergens

    def __repr__(self):
        return '\n'.join([str(x) for x in self.foods])

    def count_allergen_free(self):
        count = 0
        for food in self.foods:
            count += len([x for x in food.ingredients if x not in self.allergens.values()])
        return count

def main():
    foods = Foods('input.txt')
    utils.pretty_print_answer(1, foods.count_allergen_free())

if __name__ == '__main__':
    main()
