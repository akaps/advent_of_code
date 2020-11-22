from aoc2018.day24.germs import Group, Simulation

def test_deal_damage():
    attacker = Group('3 units each with 2910 hit points with an attack that does 25 cold damage at initiative 15')
    defender = Group('10 units each with 10 hit points with an attack that does 5 cold damage at initiative 15')
    assert attacker.effective_power() == 75
    defender.deal_damage(attacker)
    assert defender.num_units == 3

def test_run_sample():
    problem = Simulation('sample.txt')
    problem.run()
    assert max(problem.count_units()) == 5216

def test_selection_round_1():
    problem = Simulation('sample.txt')
    selections = problem.selection_phase()
    assert len(selections) == 4
    assert selections['Infection 2'] == 'Immune System 2'
    assert selections['Immune System 2'] == 'Infection 1'
    assert selections['ImmuneSystem 1'] == 'Infection 2'
    assert selections['Infection 1'] == 'Immune System 2'

def test_infection_2_selection():
    problem = Simulation('sample.txt')
    immunes = problem.get_group('Immune System')
    assert len(immunes) == 2
    selector = problem.groups['Infection 2']
    assert selector.pick_target(immunes) == 'Immune System 2'

def test_immune_2_selection():
    problem = Simulation('sample.txt')
    infections = problem.get_group('Infection')
    infections.pop(1)
    selector = problem.groups['Immune System 2']
    assert selector.pick_target(infections) == 'Infection 1'

def test_decreasing_power_list():
    problem = Simulation('sample.txt')
    sort_list = problem.decreasing_power_list()
    assert len(sort_list) == 4
    assert sort_list[1][1].effective_power() < sort_list[0][1].effective_power()
    assert sort_list[0][0] == 'Infection 1'
    assert sort_list[1][0] == 'Immune System 1'
    assert sort_list[2][0] == 'Infection 2'
    assert sort_list[3][0] == 'Immune System 2'
