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

    def find_allergens(self):
        allergens = {}
        to_process = deepcopy(self.foods)
        processed = []
        # processing = True
        while to_process:
            print('-----')
            print(len(to_process))
            food = to_process.pop(0)
            if not food.allergens:
                print('fully processed food, can eliminate')
                processed.append(food)
            elif len(food.allergens) != 1:
                print('cannot process {allergens} yet'.format(allergens=food.allergens))
                to_process.append(food) #inefficient, but will become more effective as time goes on
            else:
                assert food.allergens
                allergen = food.allergens[0]
                print('found single known allergen', allergen)
                candidates = set(food.ingredients)
                for next_food in [x for x in to_process if allergen in x.allergens]:
                    candidates.intersection_update(next_food.ingredients)
                    next_food.allergens.remove(allergen)
                print('before checking processed: {length}'.format(length=len(candidates)))
                # for next_food in processed:
                #     candidates.intersection_update(next_food.ingredients)
                # print('after checking processed: {length}'.format(length=len(candidates)))
                if len(candidates) == 1:
                    answer = candidates.pop()
                    print('{allergen} maps to {ingredient}'.format(allergen=allergen, ingredient=answer))
                    allergens[allergen] = answer
                    for next_food in [x for x in to_process if answer in x.ingredients]:
                        next_food.ingredients.remove(answer)
                    assert food not in processed
                    processed.append(food) #is food in
                else:
                    print('found {candidates} but cannot select'.format(candidates=candidates))
                    to_process.append(food)
        return allergens

    def __repr__(self):
        return '\n'.join([str(x) for x in self.foods])

    def count_allergen_free(self):
        print('allergens:', self.allergens)
        count = 0
        for food in self.foods:
            count += len([x for x in food.ingredients if x not in self.allergens.values()])
        return count

def main():
    foods = Foods('input.txt')
    utils.pretty_print_answer(1, foods.count_allergen_free())

if __name__ == '__main__':
    main()
