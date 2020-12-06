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

def get_intersection_forms(file_name):
    lines = utils.read_lines(file_name)
    forms = []
    groups = '\n'.join(lines).split('\n\n')
    for group in groups:
        group = group.split('\n')
        print('processing', group)
        if len(group) == 1:
            forms.append(set(group[0]))
            print('easy, one item')
        else:
            current_set = set.intersection(set(group[0]), set(group[1]))
            print(current_set)
            for i in range(2, len(group)):
                current_set = set.intersection(current_set, set(group[i]))
                print(current_set)
            print('ended with', current_set)
            forms.append(current_set)
    print(forms)
    return forms

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

    forms = get_intersection_forms('input.txt')
    utils.pretty_print_answer(2, yes_total(forms))

if __name__ == "__main__":
    main()
