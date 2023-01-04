import math
import statistics

class Crabs:
    def __init__(self, file_name):
        file_input = open(file_name, 'r')
        self.inputs = [int(x.strip()) for x in file_input.readline().split(',')]
        file_input.close()

    def smallest_fuel(self):
        total = 0
        median = statistics.median(self.inputs)
        for val in self.inputs:
            total += abs(val - median)
        return total

    def geometric_fuel(self):
        total = 0
        mean = math.ceil(statistics.mean(self.inputs))
        assert isinstance(mean, int)
        for val in self.inputs:
            #sum of a sequence of arithmetic terms
            diff = abs(val - mean)
            distance = (diff // 2) * (abs(diff) + 1)
            print('distance for {val} to {mean} = {distance}'.format(
                    val=val,
                    mean=mean,
                    distance=distance))
            total += distance
        print(total)
        return total

def main():
    sample = Crabs('aoc2021/day07/sample.txt')
    assert sample.smallest_fuel() == 37
    assert sample.geometric_fuel() == 168

    problem = Crabs('aoc2021/day07/input.txt')
    print('Part 1', problem.smallest_fuel())
    print('Part 2', problem.geometric_fuel())

if __name__ == '__main__':
    main()
