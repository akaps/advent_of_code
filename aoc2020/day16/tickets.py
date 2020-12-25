import utils

class Ticket:
    def __init__(self, values, rules):
        self.values = [int(x) for x in values.split(',')]
        self.potential_fields = {}
        for value in self.values:
            self.potential_fields[value] = []
            for rule in rules:
                if rule.is_match(value):
                    self.potential_fields[value].append(rule.field_name)

    def __repr__(self):
        return '\n'.join([str(self.values), str(self.potential_fields)])

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

def make_tickets(nearby_tickets, rules):
    tickets = []
    for ticket in nearby_tickets:
        tickets.append(Ticket(ticket, rules))
    return tickets

def error_rate(tickets):
    total = 0
    valid_tickets = []
    for ticket in tickets:
        is_valid = True
        for value in ticket.values:
            if not ticket.potential_fields[value]:
                total += value
                is_valid = False
        if is_valid:
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

def part_2(rules, valid_tickets, my_ticket):
    possible_fields = {}
    for index in range(20):
        possible_fields[index] = []
        for rule in rules:
            possible = True
            for ticket in valid_tickets:
                if not rule.is_match(ticket.values[index]):
                    possible = False
            if possible:
                possible_fields[index].append(rule.field_name)
    #print(possible_fields)

def main():
    definitions, my_ticket, nearby_tickets = separate_fields('input.txt')
    rules = make_rules(definitions)
    my_ticket = Ticket(my_ticket, rules)
    tickets = make_tickets(nearby_tickets, rules)
    error, valid_tickets = error_rate(tickets)
    utils.pretty_print_answer(1, error)
    part_2(rules, valid_tickets, my_ticket)
    departure_platform = my_ticket.values[5]
    departure_date = my_ticket.values[6]
    departure_station = my_ticket.values[10]
    departure_track = my_ticket.values[11]
    departure_time = my_ticket.values[16]
    departure_location = my_ticket.values[19]
    total = (departure_platform *
             departure_date *
            departure_station *
            departure_track *
            departure_time *
            departure_location)
    utils.pretty_print_answer(2, total)

if __name__ == "__main__":
    main()
