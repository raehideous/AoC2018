from aocd import get_data


def are_equal(a, b):
    res=(a.lower() == b.lower() and
            ((a.isupper() and b.islower()) or
             (a.islower() and b.isupper())))
    return res


def part_one(input):
    buffer = []
    for c in input:
        if buffer and are_equal(c, buffer[-1]):
            buffer.pop()
        else:
            buffer.append(c)

    return len(buffer)


def part_two(polymer):
    letters = set([c.lower() for c in polymer])
    minimal_count = min([part_one(polymer.replace(l, '').replace(l.upper(), '')) for l in letters])
    return minimal_count


data = get_data(day=5)
print('Part One: ', part_one(data))
print('Part Two: ', part_two(data))
