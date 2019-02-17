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
        pass

    def take_damaage(self, amount):
        self.num_units -= amount // self.hit_points

    def element_modifier(self, damage_type):
        if damage_type in self.weaknesses:
            return 2
        if damage_type in self.immunities:
            return 0
        return 1

SAMPLE = Germs('sample.txt')
INPUT = Germs('input.txt')
