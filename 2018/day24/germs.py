import re

class Germs:
    def __init__(self, file_name):
        self.armies = {}
        file = open(file_name, 'r')
        text = [x.strip() for x in file.readlines()]
        file.close()
        infection_group = text.index(r'Infection:')
        self.armies['Immune System'] = [Group(line) for line in text[1:infection_group - 1]]
        self.armies['Infection'] = [Group(line) for line in text[infection_group + 1:]]

    def combat(self):
        while len(self.armies) > 1:
            selections = self.select_targets()
            self.fight_targets(selections)

    def select_targets(self):
        imm_targets = []
        for group in self.armies['Immune System']:
            imm_targets.append(group.select_target(self.armies['Infection']))
        germ_targets = []
        for group in self.armies['Infection']:
            germ_targets.append(group.select_target(self.armies['Immune System']))
        return imm_targets, germ_targets

    def fight_targets(self, selections):
        pass

    def remaining_units(self, name):
        total = 0
        for group in self.armies[name]:
            total += group.num_units
        return total

class Group:
    def __init__(self, input_text):
        vals = re.findall(r'\d+', input_text)
        self.num_units, self.hit_points, self.attack_damage, self.initiative = vals
        self.attack_type = re.findall(r'\w+(?= damage)', input_text)

        defenses = re.findall(r'(?<=\().*(?=\))', input_text)
        if defenses:
            defenses = defenses[0]
            match = re.search(r'(?<=weak to )\w+(, \w+)*', defenses)
            self.weaknesses = match.group(0) if match else ''
            maatch = re.search(r'(?<=immune to )\w+(, \w)*', defenses)
            self.immunities = maatch.group(0) if maatch else ''

    def effective_power(self):
        return self.num_units * self.attack_damage

    def select_target(self, other_groups):
        return None

    def take_damage(self, amount):
        self.num_units -= amount // self.hit_points

    def element_modifier(self, damage_type):
        if damage_type in self.weaknesses:
            return 2
        if damage_type in self.immunities:
            return 0
        return 1

SAMPLE = Germs('sample.txt')
SAMPLE.combat()
assert SAMPLE.remaining_units('Immune System') == 0
assert SAMPLE.remaining_units('Infection') == 5216

INPUT = Germs('input.txt')
INPUT.combat()
print('results of Part 1')
print('Immune System: {power}'.format(power=INPUT.remaining_units('Immune System')))
print('Infection: {power}'.format(power=INPUT.remaining_units('Infection')))
