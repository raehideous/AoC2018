from aocd import get_data
from itertools import cycle

def part_one(input):
    data = [int(n) for n in input.split()]
    print("Part One: ", sum(data))

def part_two(input):
    freq = 0
    seen={0}
    data = [int(n) for n in input.split()]

    for n in cycle(data):
        freq+=n
        if freq in seen:
            print('Part Two: ', freq)
            break
        seen.add(freq)


data = get_data(day=1)
part_one(data)
part_two(data)
