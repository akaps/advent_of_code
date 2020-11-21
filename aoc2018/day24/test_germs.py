from aoc2018.day24.germs import Group, Simulation

def test_deal_damage():
    attacker = Group('3 units each with 2910 hit points with an attack that does 25 cold damage at initiative 15')
    defender = Group('10 units each with 10 hit points with an attack that does 5 cold damage at initiative 15')
    assert attacker.effective_power() == 75
    defender.deal_damage(attacker)
    assert defender.num_units == 3

def test_naive_input():
    problem = Simulation('sample.txt')
    problem.run()
    assert max(problem.count_units()) == 5216