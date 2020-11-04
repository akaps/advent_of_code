from aoc2015.day16.aunt_sue import Sue

def test_parse():
    sue = Sue('Sue 145: pomeranians: 2, samoyeds: 7, children: 7')
    assert sue.id == 145
    assert sue.compounds['pomeranians'] == 2
    assert sue.compounds['samoyeds'] == 7
    assert sue.compounds['children'] == 7
