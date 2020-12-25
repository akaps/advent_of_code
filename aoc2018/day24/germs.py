import math
import re
import utils

UNITS_REGEX = r'(?P<amount>\d+) units '
HIT_POINTS_REGEX = r'each with (?P<hit_points>\d+) hit points '
MODIFIERS_REGEX = r'(?P<modifiers>\(.*?\) )?'
ATTACK_DAMAGE_REGEX = r'with an attack that does (?P<damage_amt>\d+) '
DAMAGE_TYPE_REGEX = r'(?P<damage_type>\w*) damage '
INITIATIVE_REGEX = r'at initiative (?P<initiative>\d+)'
DETAILS = [
    UNITS_REGEX,
    HIT_POINTS_REGEX,
    MODIFIERS_REGEX,
    ATTACK_DAMAGE_REGEX,
    DAMAGE_TYPE_REGEX,
    INITIATIVE_REGEX
]
DETAILS_REGEX = ''.join(DETAILS)

IMMUNE = 'Immune System'
INFECT = 'Infection'

COMMA = ','
SEMI_COLON = ';'
COLON = ':'
TO_SPLIT = ' to '

class Group:
    def __init__(self, details):
        match = re.match(DETAILS_REGEX, details)
        assert match, 'failed to match line {0}'.format(details)
        self.num_units = int(match.group('amount'))
        self.hit_points = int(match.group('hit_points'))
        self.attack_damage = int(match.group('damage_amt'))
        self.attack_type = match.group('damage_type')
        self.initiative = int(match.group('initiative'))
        self.immunities = []
        self.weaknesses = []
        self.set_modifiers(match.group('modifiers'))

    def set_modifiers(self, modifiers):
        if modifiers:
            modifiers = modifiers.strip()[1:-1].split(SEMI_COLON)
            for modifier in modifiers:
                modifier_type, types = modifier.split(TO_SPLIT)
                if 'immune' in modifier_type:
                    self.immunities = types.split(COMMA)
                elif 'weak' in modifier_type:
                    self.weaknesses = types.split(COMMA)

    def effective_power(self):
        return self.attack_damage * self.num_units

    def calculate_damage(self, attacker):
        modifier = 1
        if attacker.attack_type in self.weaknesses:
            modifier = 2
        elif attacker.attack_type in self.immunities:
            modifier = 0
        return attacker.effective_power() * modifier

    def deal_damage(self, attacker):
        damage = self.calculate_damage(attacker)
        total_health = self.num_units * self.hit_points - damage
        self.num_units = math.ceil(total_health / self.hit_points) if total_health > 0 else 0

    def pick_target(self, groups):
        target = None
        target_damage = 0
        target_name = None
        target_power = math.inf
        target_initiative = 0
        for name, group in groups:
            damage = group.calculate_damage(self)
            effective_power = group.effective_power()
            if damage > target_damage:
                target_damage = damage
                target_name = name
                target_power = effective_power
                target_initiative = group.initiative
            elif damage == target_damage and effective_power < target_power:
                target_damage = damage
                target_name = name
                target_power = effective_power
                target_initiative = group.initiative
            elif (damage == target_damage
                  and effective_power == target_power
                  and group.initiative > target_initiative):
                target_damage = damage
                target_name = name
                target_power = effective_power
                target_initiative = group.initiative
        return target_name

    def is_dead(self):
        return self.num_units == 0

class Simulation:
    def __init__(self, file_name):
        self.groups = {} # groupname: Group
        lines = utils.read_lines(file_name)
        current_army = None
        counter = 1
        for line in lines:
            if COLON in line:
                counter = 1
                current_army = line[:-1]
            elif not line:
                continue
            else:
                group_name = '{name} {count}'.format(name=current_army, count=counter)
                self.groups[group_name] = Group(line)
                counter += 1

    def run(self):
        while 0 not in self.count_units():
            self.run_round()
            return

    def run_round(self):
        selections = self.selection_phase() #selections = {groupname : target}
        self.attack_phase(selections)

    def selection_phase(self):
        selections = {}
        power_list = self.decreasing_power_list()
        immunes = self.get_group(IMMUNE)
        infections = self.get_group(INFECT)
        for key, val in power_list:
            next_target = None
            if IMMUNE in key:
                next_target = val.pick_target(infections)
            else:
                next_target = val.pick_target(immunes)
            if next_target:
                selections[key] = next_target
                self.remove_target(immunes, infections, next_target)
        return selections

    def remove_target(self, immunes, infections, next_target):
        target = (next_target, self.groups[next_target])
        if target in immunes:
            immunes.remove(target)
        elif target in infections:
            infections.remove(target)
        else:
            assert False, 'Did not remove {target}'.format(target=next_target)

    def decreasing_power_list(self):
        return sorted(self.groups.items(), key=lambda x: -x[1].effective_power())

    def get_group(self, group_name):
        result = []
        for key, val in self.groups.items():
            if group_name in key:
                result.append((key, val))
        assert result, 'Generated empty list for group {0}'.format(group_name)
        return result

    def attack_phase(self, selections):
        initiative_list = sorted(self.groups.items(), key=lambda x: -x[1].initiative)
        for attacker_name, _ in initiative_list:
            defender = selections[attacker_name]
            if defender:
                self.groups[defender].deal_damage(self.groups[attacker_name])
                if self.groups[defender].is_dead():
                    del self.groups[defender]

    def count_units(self):
        immune_count = 0
        infection_count = 0
        for key, val in self.groups.items():
            if IMMUNE in key:
                immune_count += val.num_units
            elif INFECT in key:
                infection_count += val.num_units
            else:
                assert False, 'Unsupported key {0}'.format(key)
        return (immune_count, infection_count)

def main():
    problem = Simulation('input.txt')
    problem.run()
    utils.pretty_print_answer(1, max(problem.count_units()))

if __name__ == "__main__":
    main()