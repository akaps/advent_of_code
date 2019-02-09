import re
import copy

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
        to_process = copy.deepcopy(self.dependencies)
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


    def order_in_parallel(self, num_processors, time_bonus):
        processing = {}
        order = ''
        to_process = copy.deepcopy(self.dependencies)
        time = 0
        pretty_print_header(num_processors)
        while to_process or processing:
            steps = list(to_process.keys())
            steps.sort()
            populate_processors(processing, num_processors, steps, to_process, time_bonus)
            pretty_print_line(time, processing, num_processors, order)
            time += update_time(processing)
            order = complete_processors(processing, to_process, order)
        return order, time

def complete_processors(processing, to_process, order):
    for key in list(processing):
        if processing[key] <= 0:
            processing.pop(key)
            order += key
            for step in to_process:
                if key in to_process[step]:
                    to_process[step].remove(key)
    return order

def update_time(processing):
    smallest = min(processing, key=processing.get)
    time = processing[smallest]
    print('smallest time {t} for {item}'.format(t=time, item=smallest))
    time_update = processing[min(processing, key=processing.get)]
    for item in processing.items():
        processing.update({item[0]: item[1] - time_update})
    return time_update

def populate_processors(processing, num_processors, steps, to_process, time_bonus):
    if len(processing) < num_processors:
        for step in steps:
            if not to_process[step]:
                processing[step] = time_for_step(step, time_bonus)
                to_process.pop(step)

def pretty_print_header(num_processors):
    result = ['Second']
    for i in range(num_processors):
        result.append('Worker {i}'.format(i=i))
    result.append('Done')
    print('\t'.join(result))

def pretty_print_line(time, processing, num_processors, order):
    result = [str(time)]
    keys = list(processing)
    for i in range(num_processors):
        if i < len(keys):
            result.append(keys[i])
        else:
            result.append('-')
    result.append(order)
    print('\t\t'.join(result))

def time_for_step(step, time_bonus):
    return ord(step) - ord('A') + 1 + time_bonus

def solve_for(file_name, processors, step_size):
    dep = Dependencies(file_name)
    order = dep.order()
    order_parallel, time_parallel = dep.order_in_parallel(processors, step_size)

    return order, order_parallel, time_parallel

assert time_for_step('A', 0) == 1
assert time_for_step('B', 0) == 2
assert time_for_step('C', 0) == 3
assert time_for_step('D', 0) == 4
assert time_for_step('E', 0) == 5
assert time_for_step('F', 0) == 6
ORDER, ORDER_PARALLEL, TIME = solve_for('sample.txt', 2, 0)
assert ORDER == 'CABDFE'
assert TIME == 15
assert ORDER_PARALLEL == 'CABFDE'

ORDER, ORDER_PARALLEL, TIME = solve_for('input.txt', 5, 60)
print('single-threaded sequence is {order}'.format(order=ORDER))
print('multi-threaded time was {time}'.format(time=TIME))
