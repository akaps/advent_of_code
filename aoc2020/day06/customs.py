import utils

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
            current_set = set.intersection(set(family[0]), set(family[1]))
            for individual in family:
                current_set = set.intersection(current_set, set(individual))
            result.append(current_set)
    return result

def yes_total(forms):
    total = 0
    for form in forms:
        if form:
            total += len(form)
    return total

def main():
    forms = utils.read_groups('input.txt')
    yes_answers = get_yes_answers(forms)
    utils.pretty_print_answer(1, yes_total(yes_answers))

    yes_intersect = get_intersection_forms(forms)
    utils.pretty_print_answer(2, yes_total(yes_intersect))

if __name__ == "__main__":
    main()
