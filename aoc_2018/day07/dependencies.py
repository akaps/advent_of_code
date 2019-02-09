import re

class Dependencies:
    def __init__(self, file_name):
        file = open(file_name)
        self.parse_input(file.readlines())
        file.close()

    def parse_input(self, instructions):
        self.dependencies = {}
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
        order = ''
        to_process = dict(self.dependencies)
        while to_process:
            steps = list(to_process.keys())
            steps.sort()
            for step in steps:
                if not to_process[step]:
                    order += step
                    self.satisfy_dependencies(step, to_process)
                    break
        return order

    def satisfy_dependencies(self, to_remove, dependencies):
        dependencies.pop(to_remove)
        for step in dependencies:
            if to_remove in dependencies[step]:
                dependencies[step].remove(to_remove)


    def order_in_parallel(self, time_bonus):
        processing_1 = None
        processing_2 = None
        order = ''
        to_process = dict(self.dependencies)
        time = 0
        print('Second\tWorker 1\tWorker 2\tDone')
        while to_process:
            steps = list(to_process.keys())
            steps.sort()
            if not processing_1 or not processing_2:
                for step in steps:
                    if not to_process[step]:
                        if not processing_1:
                            processing_1 = [step, time_for_step(step, time_bonus)]
                            to_process.pop(step)
                        elif not processing_2:
                            to_process.pop(step)
                            processing_2 = [step, time_for_step(step, time_bonus)]
            if processing_1: 
                processing_1[1] -= 1
            if processing_2: 
                processing_2[1] -= 1
            print('{sec}\t{t1}\t\t{t2}\t\t{done}'.format(
                sec=time,
                t1=processing_1[0] if processing_1 else '-',
                t2=processing_2[0] if processing_2 else '-',
                done=order))
            if processing_1 and processing_1[1] <= 0:
                order += processing_1[0]
                processing_1 = None
            if processing_2 and processing_2[1] <=0:
                order += processing_2[0]
                processing_2 = None
        return order, time

def time_for_step(step, time_bonus):
    return ord(step) - ord('A') + time_bonus

def solve_for(file_name, step_size):
    dep = Dependencies(file_name)
    order = dep.order()
    order_parallel, time_parallel = dep.order_in_parallel(step_size)

    return order, order_parallel, time_parallel

ORDER, ORDER_PARALLEL, TIME = solve_for('sample.txt', 0)
assert ORDER == 'CABDFE'
assert ORDER_PARALLEL == 'CABFDE'
assert TIME == 15

ORDER, ORDER_PARALLEL, TIME = solve_for('input.txt', 60)
print('single-threaded sequence is {order}'.format(order=ORDER))
print('multi-threaded time was {time}'.format(time=TIME))
