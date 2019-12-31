import itertools

ITEMS = ['food ration', 'weather machine', 'antenna', 'jam', 'semiconductor', 'planetoid', 'monolith']

FILE = open('combinations.txt', 'w')
for r in range(1, len(ITEMS)):
    for combination in itertools.combinations(ITEMS, r):
        for item in combination:
            FILE.write('take {item}\n'.format(item=item))
        FILE.write('east\n')
        for item in combination:
            FILE.write('drop {item}\n'.format(item=item))
FILE.close()
