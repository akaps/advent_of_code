import utils

class TicketRule:
    def __init__(self, rule_str):
        self.field_name, rest = rule_str.split(':')
        lower, rest = rest.split(' or ')
        upper = rest.strip()
        self.lower_range = [int(x) for x in lower.split('-')]
        self.upper_range = [int(x) for x in upper.split('-')]

    def is_match(self, value):
        return (self.lower_range[0] <= value <= self.lower_range[1] or
                self.upper_range[0] <= value <= self.upper_range[1])

def make_rules(rules_str):
    rules = []
    for rule_str in rules_str:
        rules.append(TicketRule(rule_str))
    return rules

def make_tickets(nearby_tickets):
    tickets = []
    for ticket in nearby_tickets:
        tickets.append(make_ticket(ticket))
    return tickets

def make_ticket(ticket_str):
    return (int(x) for x in ticket_str.split(','))

def error_rate(rules, tickets):
    total = 0
    valid_tickets = []
    for ticket in tickets:
        is_valid_ticket = True
        for value in ticket:
            is_valid_value = False
            for rule in rules:
                if rule.is_match(value):
                    is_valid_value = True
                    break
            if not is_valid_value:
                total += value
                is_valid_ticket = False
        if is_valid_ticket:
            valid_tickets.append(ticket)
    return total, valid_tickets

def separate_fields(file_name):
    lines = utils.read_lines(file_name, is_strip=False)
    input_break1 = lines.index('\n')
    input_break2 = lines.index('\n', input_break1 + 1)
    definitions = lines[:input_break1]
    my_ticket = lines[input_break1 + 1: input_break2][1].strip()
    nearby_tickets = lines[input_break2 + 1:][1:]
    return definitions, my_ticket, nearby_tickets

def main():
    definitions, my_ticket, nearby_tickets = separate_fields('input.txt')
    rules = make_rules(definitions)
    my_ticket = make_ticket(my_ticket[1])
    tickets = make_tickets(nearby_tickets)
    error, valid_tickets = error_rate(rules, tickets)
    utils.pretty_print_answer(1, error)
    print(len(valid_tickets))
    print(valid_tickets)

if __name__ == "__main__":
    main()
