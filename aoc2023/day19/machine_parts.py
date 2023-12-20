import re

ACCEPTED = 'A'
REJECTED = 'R'

EXPR_REGEX = r'(.*)\{(.*)\}'
PART_REGEX = r'\d+'
RULES_DELIMITER = ','
CONDITION_DELIMITER = ':'

class MachinePart:
    def __init__(self, values):
        x, m, a, s = re.findall(PART_REGEX, values)
        self.extreme = int(x)
        self.musical = int(m)
        self.aerodynamic = int(a)
        self.shiny = int(s)

    def score(self):
        return self.extreme + self.musical + self.aerodynamic + self.shiny

class Rule:
    def __init__(self, rule):
        if CONDITION_DELIMITER in rule:
            self.condition, self.output = rule.split(CONDITION_DELIMITER)
            self.condition = self.condition
        else:
            self.condition = None
            self.output = rule

    def evaluate(self, part:MachinePart)-> bool:
        if self.condition:
            return eval(self.condition, { \
                'x': part.extreme, \
                'm': part.musical, \
                'a': part.aerodynamic,\
                's': part.shiny})
        return True

class Workflow:
    def __init__(self, rules):
        self.rules = []
        for rule in rules.split(RULES_DELIMITER):
            self.rules.append(Rule(rule))

    def evaluate(self, part: MachinePart) -> str:
        for rule in self.rules:
            if rule.evaluate(part):
                return rule.output
        assert False, 'workflows cannot have undefined outputs'

class Workflows:
    def __init__(self, file_name):
        input_file = open(file_name, encoding='utf-8')
        self.instructions = {} #label, checks
        next_line = input_file.readline().strip()
        while next_line:
            label, workflow = re.match(EXPR_REGEX, next_line).groups()
            self.instructions[label] = Workflow(workflow)
            next_line = input_file.readline().strip()
        self.parts = []

        next_line = input_file.readline().strip()
        while next_line:
            self.parts.append(MachinePart(next_line))
            next_line = input_file.readline().strip()

    def evaluate(self, part:MachinePart) -> str:
        current_label = 'in'
        while current_label != ACCEPTED and current_label != REJECTED:
            current_rule = self.instructions[current_label]
            current_label = current_rule.evaluate(part)
        return current_label

    def sum_accepted(self):
        total = 0
        for part in self.parts:
            result = self.evaluate(part)
            if result == ACCEPTED:
                total += part.score()
        return total

def main():
    sample = Workflows('aoc2023/day19/sample.txt')
    assert sample.sum_accepted() == 19114

    problem = Workflows('aoc2023/day19/input.txt')
    print('Answer to Part 1:', problem.sum_accepted())
    print('Answer to Part 2:', -1)

if __name__ == '__main__':
    main()
