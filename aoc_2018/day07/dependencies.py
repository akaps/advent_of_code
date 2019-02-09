import re

class Dependencies:
    def __init__(self):
        self.dependencies = {}

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

    def order(self):
        res =''
        while self.dependencies:
            steps = list(self.dependencies.keys())
            steps.sort()

            for step in steps:
                if not self.dependencies[step]:
                    res += step
                    self.satisfy_dependencies(step)
                    break
        return res

    def satisfy_dependencies(self, step):
        self.dependencies.pop(step)
        for step_2 in self.dependencies:
            if step in self.dependencies[step_2]:
                self.dependencies[step_2].remove(step)


    def order_in_parallel(self, max_workers, time_bonus):
        total_time = 0
        processing = {}
        order = ''
        while self.dependencies:
            steps = list(self.dependencies.keys())
            steps.sort()
            #fill pipelines
            for step in steps:
                if not self.dependencies[step] and len(processing) < max_workers:
                    print(step)
                    processing[step] = time_for_step(step, time_bonus)
                    print(self.dependencies)
            print(processing)
            #decrease time in pipelines & increase time in total
            to_remove = min(processing, key=processing.get)
            order += to_remove
            time_left = processing.pop(to_remove, None)
            processing = {k: v - time_left for k, v in processing.items()}
            self.satisfy_dependencies(to_remove)
            total_time += time_left
            print(total_time)
            print(order)
        return total_time

def time_for_step(step, time_bonus):
    return ord(step)-ord('A')+time_bonus

file = open('input.txt')
instr = file.readlines()
file.close()
dep = Dependencies()

#part 1
dep.parse_input(instr)
order = dep.order()
print('single-threaded sequence is {order}'.format(order=order))

#part 2
dep.parse_input(instr)
time = dep.order_in_parallel(2, 0)
print('multi-threaded time was {time}'.format(time=time))
