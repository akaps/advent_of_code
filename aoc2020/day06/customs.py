import utils

def get_forms(file_name):
    lines = utils.read_lines(file_name)
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

def yes_answers(forms):
    total = 0
    for form in forms:
        if form:
            total += len(form)
    return total

def main():
    forms = get_forms('input.txt')
    utils.pretty_print_answer(1, yes_answers(forms))

    forms = get_intersection_forms('input.txt')
    utils.pretty_print_answer(2, yes_answers(forms))

if __name__ == "__main__":
    main()
