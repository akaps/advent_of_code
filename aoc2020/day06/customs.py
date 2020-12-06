import utils

def get_forms(file_name):
    lines = utils.read_lines(file_name)
    result = []
    current_group = []
    while lines:
        line = lines.pop(0)
        if line:
            current_group.append(set(line))
        else:
            result.append(current_group)
            current_group = []
    result.append(current_group)
    return result

def get_yes_answers(forms):
    result = []
    for family in forms:
        current_set = set()
        for individual in family:
            current_set.update(individual)
        result.append(current_set)
    return result

def get_intersection_forms(forms):
    result = []
    for family in forms:
        if len(family) == 1:
            result.append(family[0])
        else:
            current_set = set.intersection(family[0], family[1])
            for individual in family:
                current_set = set.intersection(current_set, individual)
            result.append(current_set)
    return result

def yes_total(forms):
    total = 0
    for form in forms:
        if form:
            total += len(form)
    return total

def main():
    forms = get_forms('input.txt')
    yes_answers = get_yes_answers(forms)
    utils.pretty_print_answer(1, yes_total(yes_answers))

    yes_intersect = get_intersection_forms(forms)
    utils.pretty_print_answer(2, yes_total(yes_intersect))

if __name__ == "__main__":
    main()
