import re
from collections import defaultdict
import math
import utils

ARROW = r' => '
COMMA = r', '
SPACE = r' '

FUEL = 'FUEL'
ORE = 'ORE'

class Formula:
    def __init__(self, formula):
        self.count, self.name = re.split(SPACE, formula)
        self.count = int(self.count)

    def __repr__(self):
        return '{count} {name}'.format(count=self.count, name=self.name)

class Equation:
    def __init__(self, reactants, product):
        self.product = product
        self.reactants = []
        for reactant in re.split(COMMA, reactants):
            self.reactants.append(Formula(reactant))

    def __repr__(self):
        reactants = COMMA.join([str(reactant) for reactant in self.reactants])
        return '{reactants} makes {product}'.format(reactants=reactants, product=str(self.product))

class Equations:
    def __init__(self, input_file):
        self.populate_equations(input_file)

    def populate_equations(self, input_file):
        self.equations = {}
        lines = utils.read_lines(input_file)
        for line in lines:
            reactants, prod_formula = re.split(ARROW, line)
            product = Formula(prod_formula)
            self.equations[product.name] = Equation(reactants, product)
        return self.equations

    def produce(self, prod_name, prod_count, chemicals):
        missing_reactants = {}
        if chemicals[prod_name] > prod_count:
            chemicals[prod_name] -= prod_count
            return missing_reactants, chemicals
        needed_product = prod_count - chemicals[prod_name]
        formula = self.equations[prod_name]
        multiple = int(math.ceil(needed_product / formula.product.count))
        chemicals[prod_name] += (formula.product.count * multiple) - needed_product
        for reactant in formula.reactants:
            missing_reactants[reactant.name] = reactant.count * multiple
        return missing_reactants, chemicals

    def minimum_ore(self):
        min_ore = 0
        to_produce = {FUEL: 1}
        products = defaultdict(lambda: 0)
        while to_produce:
            print(min_ore, to_produce)
            next_product = list(to_produce.keys())[0]
            next_count = to_produce.pop(next_product)
            if next_product == ORE:
                min_ore += next_count
            else:
                reactants, products = self.produce(next_product, next_count, products)
                for name, count in reactants.items():
                    if name not in to_produce:
                        to_produce[name] = 0
                    to_produce[name] += count
        return min_ore

def main():
    equations = Equations('input.txt')
    min_ore = equations.minimum_ore()
    utils.pretty_print_answer(1, min_ore)

if __name__ == '__main__':
    main()
