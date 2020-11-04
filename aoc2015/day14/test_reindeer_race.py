from aoc2015.day14.reindeer_race import Reindeer, parse_line, winning_deer

def test_parser():
    name, rate, duration, rest = parse_line(
        'Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.')
    assert name == 'Comet'
    assert rate == 14
    assert duration == 10
    assert rest == 127

def test_race():
    reindeer = []
    reindeer.append(Reindeer(
        'Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.'))
    reindeer.append(Reindeer(
        'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.'))
    assert winning_deer(reindeer, 1000) == 'Comet', 1120
