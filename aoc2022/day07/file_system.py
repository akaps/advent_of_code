import re

cd_regex = re.compile(r'\$ cd (.+)')
ls_regex = re.compile(r'\$ ls')
dir_regex = re.compile(r'dir (.+)')
file_regex = re.compile(r'(\d+) (.+)')

class File:
    def __init__(self, size: int, name: str):
        self.name = name
        self.size = int(size)

    def __str__(self):
        return '{name} size={size}'.format(path=self.name, size=self.size)

class Directory:
    def __init__(self, name: str, parent):
        self.parent = parent
        self.name = name
        self.files = []
        self.directories = {}

    def add_file(self, size: int, name: str):
        self.files.append(File(size, name))

    def add_directory(self, name: str):
        self.directories[name] = Directory(name, self)

    def path(self):
        current_dir = self
        result = []
        while current_dir:
            result.insert(0, current_dir.name)
            current_dir = current_dir.parent
        return '/'.join(result)[1:]

    def __str__(self):
        if not self.parent:
            return self.name
        else:
            return str(self.parent) + '/' + self.name

class FileSystem:
    def __init__(self, file_name: str):
        self.root = Directory('/', None)
        self.current_directory = self.root
        file_input = open(file_name, 'r')
        lines = [s.strip() for s in file_input.readlines()]
        file_input.close()
        lines.pop(0)
        self.parse_input(lines)

    def cd(self, input: str):
        input = re.match(cd_regex, input).groups()[0]
        if input == '..':
            self.current_directory = self.current_directory.parent
        else:
            self.current_directory = self.current_directory.directories[input]

    def pwd(self):
        return self.current_directory.path()

    def ls(self):
        return self.current_directory.directories

    def parse_input(self, lines):
        while lines:
            command = lines.pop(0)
            assert is_command(command)
            if is_cd_command(command):
                self.cd(command)
            elif is_ls_command(command):
                lines = self.process_ls(lines)
            else:
                assert False, 'unsupported command {cmd}'.format(cmd=command)

    def process_ls(self, lines):
        current_line = lines.pop(0)
        while not is_command(current_line):
            if re.match(dir_regex, current_line):
                name = re.match(dir_regex, current_line).groups()[0]
                self.current_directory.add_directory(name)
            elif re.match(file_regex, current_line):
                size, name = re.match(file_regex, current_line).groups()
                self.current_directory.add_file(size, name)
            else:
                assert False, 'unexpected line {line}'.format(line=current_line)
            if lines:
                current_line = lines.pop(0)
            else:
                assert not lines
                return lines
        lines.insert(0, current_line)
        return lines

    def inventory_sizes(self):
        self.sizes = {}
        self.inventory_sizes_inner(self.root)

    def inventory_sizes_inner(self, current_directory):
        size = sum([file.size for file in current_directory.files])
        for child in current_directory.directories.values():
            size += self.inventory_sizes_inner(child)
        self.sizes[current_directory.path()] = size
        return size

def is_command(line):
    return '$' in line

def is_cd_command(line: str):
    return re.match(cd_regex, line)

def is_ls_command(line: str):
    return re.match(ls_regex, line)

def sizes_under_100kb(sizes):
    result = 0
    for size in sizes.values():
        if size < 100000:
            result += size
    return result

def find_smallest_freeup(sizes):
    available_free = 70000000 - sizes['']
    to_free = 30000000 - available_free
    free_candidates = []
    for size in sizes.values():
        if size >= to_free:
            free_candidates.append(size)
    return min(free_candidates)

def main():
    system = FileSystem('aoc2022/day07/sample.txt')
    small = sizes_under_100kb(system.sizes)
    assert small == 95437

    system = FileSystem('aoc2022/day07/input.txt')
    sizes = system.inventory_sizes()
    print('Part 1: ', sizes_under_100kb(system.sizes))
    print('Part 2:', find_smallest_freeup(system.sizes))

if __name__ == '__main__':
    main()
