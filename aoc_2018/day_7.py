import re
import heapq

class Dependencies:
    def __init__(self, instructions):
        self.dependencies = {}
        self.parse_input(instructions)

    def parse_input(self, instructions):
        regex = 'Step | must be finished before step | can begin.'
        for instruction in instructions:
            instruction = re.split(regex, instruction.strip())
            depends_on, step = list(filter(None, instruction))
            if step not in self.dependencies:
                self.dependencies[step] = []
            if depends_on not in self.dependencies:
                self.dependencies[depends_on] = []
            self.dependencies[step].append(depends_on)
        print(self.dependencies)

    def order(self):
        res =''
        while self.dependencies:
            steps = list(self.dependencies.keys())
            steps.sort()
            print(steps)
            for step in steps:
                if len(self.dependencies[step]) == 0:
                    print(step)
                    res += step
                    self.dependencies.pop(step)
                    for step_2 in self.dependencies:
                        if step in self.dependencies[step_2]:
                            self.dependencies[step_2].remove(step)
                    break
        return res


file = open('day_7_input.txt')
instr = file.readlines()
file.close()
dep = Dependencies(instr)
print(dep.order())
