import re
import utils

VALUE_REGEX = r'value (\d+) goes to (bot \d+)'
BOT_REGEX = r'(bot \d+) gives low to (bot \d+|output \d+) and high to (bot \d+|output \d+)'

class Robot:
    def __init__(self, name):
        self.name = name
        self.values = []
        self.high_dest = None
        self.low_dest = None

    def receive(self, value):
        assert len(self.values) < 2, 'cannot add more than 2 values to a robot'
        self.values.append(value)

    def send(self):
        if 5 in self.values and 2 in self.values:
            assert self.name == 'bot 2'
        if 61 in self.values and 17 in self.values:
            utils.pretty_print_answer(1, self.name)
        assert self.high_dest and self.low_dest, (
            '{bot} high {high} and low {low} destinations not set'.format(
                bot=self.name, high=self.high_dest, low=self.low_dest))
        result = {}
        result[self.low_dest] = min(self.values)
        result[self.high_dest] = max(self.values)
        self.values.clear()
        return result

    def is_full(self):
        return len(self.values) == 2

    def __repr__(self):
        return 'holding: {vals}, high to {high}, low to {low}'.format(vals=self.values, high=self.high_dest, low=self.low_dest)

class Factory:
    def __init__(self, file_name):
        self.output = {}
        self.robots = {}
        lines = utils.read_lines(file_name)
        self.handoffs = []
        self.load_rules(lines)

    def load_rules(self, lines):
        for line in lines:
            if re.match(BOT_REGEX, line):
                robot, low, high = re.match(BOT_REGEX, line).groups()
                self.set_robot_rules(robot, low, high)
            elif re.match(VALUE_REGEX, line):
                self.handoffs.append(line)
            else:
                assert False, 'parse error for line {line}'.format(line=line)

    def run_simulation(self):
        for line in self.handoffs:
            if re.match(VALUE_REGEX, line):
                value, robot = re.match(VALUE_REGEX, line).groups()
                value = int(value)
                self.give_value(value, robot)
            else:
                assert False, 'parse error for line {line}'.format(line=line)

    def give_value(self, value, to_robot):
        self.validate_entry(to_robot)
        self.robots[to_robot].receive(value)
        if self.robots[to_robot].is_full():
            to_process = self.robots[to_robot].send()
            for destination, value2 in to_process.items():
                if 'output' in destination:
                    self.output[destination] = value2
                elif 'bot' in destination:
                    self.give_value(value2, destination)
                else:
                    assert False, 'definitely did something wrong processing {0}'.format(to_process)

    def set_robot_rules(self, robot, low_dest, high_dest):
        self.validate_entries(robot, low_dest, high_dest)
        self.robots[robot].low_dest = low_dest
        self.robots[robot].high_dest = high_dest

    def validate_entries(self, robot, low_dest, high_dest):
        if robot not in self.robots:
            self.robots[robot] = Robot(robot)
        self.validate_entry(low_dest)
        self.validate_entry(high_dest)

    def validate_entry(self, entry):
        if 'bot' in entry and entry not in self.robots:
            self.robots[entry] = Robot(entry)

    def __repr__(self):
        result = []
        for key, val in self.output.items():
            result.append('{key}: {val}'.format(key=key, val=val))
        for key, val in self.robots.items():
            result.append('{key}: {val}'.format(key=key, val=val))
        return '\n'.join(result)

def main():
    sample = Factory('test.txt')
    sample.run_simulation()
    assert sample.output['output 1'] == 2
    assert sample.output['output 2'] == 3
    assert sample.output['output 0'] == 5
    problem = Factory('input.txt')
    problem.run_simulation()
    vals = problem.output
    utils.pretty_print_answer(2, vals['output 0'] * vals['output 1'] * vals['output 2'])

if __name__ == '__main__':
    main()