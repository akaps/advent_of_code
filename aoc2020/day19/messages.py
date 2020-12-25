import re
import utils

SPACE = ' '
OR = '|'
A = 'a'
B = 'b'
COLON = ': '
TERM_REGEX = r'(\d+|a|b)'

class Rules:
    def __init__(self, file_name):
        rules_text, self.messages = split_input(file_name)
        self.rules = generate_rules(rules_text)
        self.sub_answers = {}

    def count_messages_for(self, rule_id):
        self.sub_answers.clear()
        regex = self.generate_regex(rule_id)
        count = 0
        for message in self.messages:
            if re.fullmatch(regex, message):
                count += 1
        return count

    def generate_regex(self, rule_id):
        print('evaluating', rule_id)
        if rule_id in self.sub_answers:
            print('have answer!')
            return self.sub_answers[rule_id]
        if not rule_id.isdigit():
            print('base case')
            return rule_id
        sub_rules = self.rules[rule_id]
        result = ''
        if OR in sub_rules:
            clauses = []
            clause_a, clause_b = sub_rules.split(OR)
            print('handling first half', clause_a)
            for term in re.findall(TERM_REGEX, clause_a):
                print(term)
                clauses.append(self.generate_regex(term))
            clauses.append(OR)
            print('handling second half', clause_b)
            for term in re.findall(TERM_REGEX, clause_b):
                clauses.append(self.generate_regex(term))
            result = '({clauses})'.format(clauses=''.join(clauses))
        else:
            print('easier case, no OR involved')
            clauses = []
            for term in re.findall(TERM_REGEX, sub_rules):
                clauses.append(self.generate_regex(term))
            result = ''.join(clauses)
        assert result
        print('unclean result', result)
        self.sub_answers[rule_id] = result
        return result

def split_input(file_name):
    lines = utils.read_lines(file_name)
    input_break = lines.index('')
    rules_list = lines[:input_break]
    messages = lines[input_break + 1:]
    return rules_list, messages

def generate_rules(rules_list):
    result = {}
    for rule in rules_list:
        key, value = rule.split(COLON)
        value = value.replace('"', '')
        result[key] = value
    return result

def main():
    rules = Rules('input.txt')
    utils.pretty_print_answer(1, rules.count_messages_for('0'))

if __name__ == "__main__":
    main()
