import utils

def get_forms(lines):
    forms = []
    current_set = set()
    while lines:
        line = lines.pop(0)
        if line:
            current_set.update(set(line))
        else:
            forms.append(current_set)
            current_set = set()
    forms.append(current_set)
    return forms

def get_intersection_forms(lines):
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
            if current_set:
                forms.append(current_set)
    print(forms)
    return forms

def yes_answers(forms):
    total = 0
    for form in forms:
        total += len(form)
    return total

def main():
    lines = utils.read_lines('sample.txt')
    forms = get_forms(lines)
    assert len(forms) == 5
    assert yes_answers(forms) == 11

    lines = utils.read_lines('input.txt')
    forms = get_forms(lines)
    utils.pretty_print_answer(1, yes_answers(forms))

    lines = utils.read_lines('sample.txt')
    forms = get_intersection_forms(lines)
    print(forms)
    assert yes_answers(forms) == 6

    lines = utils.read_lines('input.txt')
    forms = get_intersection_forms(lines)
    utils.pretty_print_answer(2, yes_answers(forms))

if __name__ == "__main__":
    main()
