from copy import deepcopy

ADULT_SPAWN = 7
CHILD_SPAWN = 9

class Lanternfish:
    def __init__(self, file_name):
        self.adults = [0] * ADULT_SPAWN
        with open(file_name, 'r') as file:
            for val in [int(val) for val in file.readline().split(',')]:
                self.adults[val] += 1

    def fish_after_time(self, time) -> int:
        children = [0] * CHILD_SPAWN
        adults = deepcopy(self.adults)
        for current_time in range(time):
            #children who spawn become adults, spawn children
            child_index = current_time % CHILD_SPAWN
            children_spawning = children[child_index]
            children[(current_time + CHILD_SPAWN) % CHILD_SPAWN] += children_spawning
            adults[(current_time + ADULT_SPAWN) % ADULT_SPAWN] += children_spawning
            children[child_index] = 0

            #adults who spawn remain adults, spawn children
            adult_index = current_time % ADULT_SPAWN
            children_spawning = adults[adult_index]
            children[(current_time + CHILD_SPAWN) % CHILD_SPAWN] += children_spawning
        return self.fish_count(adults, children)

    def fish_count(self, adults, children) -> int:
        return sum(adults) + sum(children)

def main():
    sample = Lanternfish('aoc2021/day06/sample.txt')
    assert sample.fish_after_time(0) == 5
    assert sample.fish_after_time(1) == 5
    assert sample.fish_after_time(2) == 6
    assert sample.fish_after_time(3) == 7
    assert sample.fish_after_time(4) == 9
    assert sample.fish_after_time(5) == 10
    assert sample.fish_after_time(6) == 10
    assert sample.fish_after_time(7) == 10
    assert sample.fish_after_time(8) == 10
    assert sample.fish_after_time(9) == 11
    assert sample.fish_after_time(10) == 12
    assert sample.fish_after_time(11) == 15
    assert sample.fish_after_time(12) == 17
    assert sample.fish_after_time(13) == 19
    assert sample.fish_after_time(14) == 20
    assert sample.fish_after_time(15) == 20
    assert sample.fish_after_time(16) == 21
    assert sample.fish_after_time(17) == 22
    assert sample.fish_after_time(18) == 26
    assert sample.fish_after_time(80) == 5934

    problem = Lanternfish('aoc2021/day06/input.txt')
    print('Part 1:', problem.fish_after_time(80))

    assert sample.fish_after_time(256) == 26984457539
    print('Part 2:', problem.fish_after_time(256))

if __name__ == '__main__':
    main()
