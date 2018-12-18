from aocd import get_data

def part_one(input):
    areas=input.splitlines()
    print("Part One: ", areas)

def part_two(input):
    res=''
    print("Part Two: ", res)


data = get_data(day=6)
data = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9"""
part_one(data)
part_two(data)
