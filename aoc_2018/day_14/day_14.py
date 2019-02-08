import copy

class Recipes:

    def __init__(self):
        self.recipe = [3, 7]
        self.current = 0
        self.next = 1

    def run(self, total):
        i = 0
        while i < total + 10:
            score = self.recipe[self.current] + self.recipe[self.next]
            score = [int(d) for d in str(score)]
            self.recipe.extend(score)
            self.current = (self.current + (self.recipe[self.current] + 1)) % len(self.recipe)
            self.next = (self.next + (self.recipe[self.next] + 1)) % len(self.recipe)
            i += len(score)

    def __repr__(self):
        pretty = copy.deepcopy(self.recipe)
        for i in range(len(pretty)):
            if i == self.current:
                pretty[i] = '({num})'.format(num=pretty[i])
            elif i == self.next:
                pretty[i] = '[{num}]'.format(num=pretty[i])
        return ' '.join(map(str, pretty))

    def next_ten(self, num):
        return ''.join(map(str, self.recipe[num:num+10]))

#easy sample
recipes = Recipes()
#print(recipes)
recipes.run(9)
assert recipes.next_ten(9) == '5158916779'
assert recipes.next_ten(5) == '0124515891'
#big sample
recipes.run(2018)
assert recipes.next_ten(18) == '9251071085'
assert recipes.next_ten(2018) == '5941429882'
#input
print('part 1')
recipes.run(409551)
print(recipes.next_ten(409551))
