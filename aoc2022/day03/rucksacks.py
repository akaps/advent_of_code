def collisions(lines):
    total = 0
    for line in lines:
        total += collision(line)
    return total

def collision(line):
    assert len(line) % 2 == 0
    half = len(line) // 2
    ruck1, ruck2 = line[:half], line[half:]
    assert len(ruck1) == len(ruck2)
    duplicate_char = list(set(ruck1).intersection(ruck2))[0]
    return priority(duplicate_char)

def priority(character):
    if character.isupper():
        return ord(character) - ord('A') + 27
    return ord(character) - ord('a') + 1

def badge_group(group1, group2, group3):
    badge = list(set(group1).intersection(group2).intersection(group3))[0]
    return badge

def badge_priorities(lines):
    assert len(lines) % 3 == 0
    priorities = 0
    for index in range(0, len(lines), 3):
        badge = badge_group(lines[index], lines[index + 1], lines[index +2])
        priorities += priority(badge)
    return priorities

def main():
    input_file = open('input.txt', 'r')
    lines = [s.strip() for s in input_file.readlines()]
    input_file.close()
    sum_priorities = collisions(lines)
    print('Part 1: ',  sum_priorities)

    sum_badges = badge_priorities(lines)
    print('Part 2:', sum_badges)

if __name__ == '__main__':
    assert priority('p') == 16
    assert priority('L') == 38
    assert priority('P') == 42
    assert priority('v') == 22
    assert priority('t') == 20
    assert priority('s') == 19

    assert badge_group('vJrwpWtwJgWrhcsFMMfFFhFp',
                        'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
                        'PmmdzqPrVvPwwTWBwg') == 'r'
    assert badge_group('wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
                        'ttgJtRGJQctTZtZT',
                        'CrZsJsPPZsGzwwsLwLmpwMDw') == 'Z'

    main()
