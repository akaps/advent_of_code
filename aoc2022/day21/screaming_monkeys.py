import re

statement_regex = re.compile(r'(.*): (.*)')
equation_regex = re.compile(r'(.+) ([+\-\*\/]) (.*)')

class Monkey:
    def __init__(self, term_a, operator, term_b):
        self.terms = {term_a: None,
                    term_b: None}
        self.operator = operator

    def substitute(self, term, value):
        self.terms[term] = value

    def solve(self):
        lhs, rhs = self.terms.values()
        assert lhs and rhs
        if self.operator == '+':
            return lhs + rhs
        elif self.operator == '-':
            return lhs - rhs
        elif self.operator == '*':
            return lhs * rhs
        elif self.operator == '/':
            return lhs // rhs

class Monkeys:
    def __init__(self, file_name):
        file_input = open(file_name, 'r')
        lines = file_input.readlines()
        file_input.close()
        self.initialize(lines)

    def initialize(self, lines):
        self.asked = {}
        self.answered = {}
        for line in lines:
            name, statement = re.match(statement_regex, line).groups()
            if re.match(equation_regex, statement):
                term_a, operator, term_b = re.match(equation_regex, statement).groups()
                self.asked[name] = Monkey(term_a, operator, term_b)
            else:
                assert statement.isdigit()
                self.answered[name] = int(statement)

    def solve(self):
        return self.solve_for_term('root')

    def solve_for_term(self, term):
        if term in self.answered:
            return self.answered[term]
        else:
            monkey = self.asked[term]
            lhs, rhs = monkey.terms
            lhs_answer = None
            rhs_answer = None
            if lhs in self.answered:
                lhs_answer = self.answered[lhs]
            else:
                lhs_answer = self.solve_for_term(lhs)
            monkey.substitute(lhs, lhs_answer)

            if rhs in self.answered:
                rhs_answer = self.answered[rhs]
            else:
                rhs_answer = self.solve_for_term(rhs)
            monkey.substitute(rhs, rhs_answer)

            answer = monkey.solve()
            self.answered[term] = answer
            return answer

def main():
    sample = Monkeys('sample.txt')
    assert sample.solve() == 152

    problem = Monkeys('input.txt')
    print('Part 1: ', problem.solve())

if __name__ == '__main__':
    main()
