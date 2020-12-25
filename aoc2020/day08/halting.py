from collections import defaultdict
import copy
import utils
import aoc2020.virtual_machine as vm

def run_til_repeat(virtual_machine):
    vm_state = vm.VmState()
    ips = defaultdict(lambda: False)
    infinite = False
    while vm_state.instruction_pointer < len(virtual_machine.instructions) and not ips[vm_state.instruction_pointer]:
        ips[vm_state.instruction_pointer] = True
        instruction = virtual_machine.instructions[vm_state.instruction_pointer]
        vm_state = vm.execute(instruction, vm_state)
        if vm_state.instruction_pointer in ips:
            infinite = True
    return vm_state.accumulator, infinite

def find_non_accs(instructions):
    result = []
    for index, instruction in enumerate(instructions):
        if instruction[vm.OPCODE] != vm.ACC:
            result.append((index, instruction))
    return result

def part_2(virtual_machine):
    old_instructions = copy.deepcopy(virtual_machine.instructions)
    non_accs = find_non_accs(virtual_machine.instructions)
    non_accs.reverse()
    for index, instruction in non_accs:
        modified_instructions = copy.deepcopy(virtual_machine.instructions)
        if vm.JUMP in instruction[vm.OPCODE]:
            modified_instructions[index][vm.OPCODE] = vm.NOP
        elif vm.NOP in instruction[vm.OPCODE]:
            modified_instructions[index][vm.OPCODE] = vm.JUMP
        else:
            assert False, 'Unexpected opcode {op}'.format(op=instruction)
        virtual_machine.instructions = modified_instructions
        answer, infinite = run_til_repeat(virtual_machine)
        if not infinite:
            print('found solution inverting', index, instruction)
            return answer
        virtual_machine.instructions = old_instructions
    assert False, 'Did not find answer to part 2'
    return -1

def main():
    virtual_machine = vm.VirtualMachine('aoc2020/day08/input.txt')
    utils.pretty_print_answer(1, run_til_repeat(virtual_machine)[0])
    utils.pretty_print_answer(2, part_2(virtual_machine))

if __name__ == "__main__":
    main()
