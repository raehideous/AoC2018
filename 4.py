from collections import defaultdict
from aocd import get_data
from datetime import datetime

def get_minutes(time):
    return int(time[-2:])


def part_one(input):
    guards_times = defaultdict(int)
    times = defaultdict(int)
    guard = None
    asleep = None

    for line in input:
        time, action = line.split('] ')
        time = get_minutes(time)
        if 'Guard' in action:
            guard = int(action.split()[1][1:])
            asleep = None
        elif 'falls asleep' in action:
            asleep = time
        elif 'wakes up' in action:
            # guardsTimes[guard] =
            times[guard] += (time - asleep)
            for t in range(asleep, time):
                guards_times[(guard, t)] += 1

    top_time = 0
    top_guard = 0
    for key in times:
        if times[key] > top_time:
            top_time = times[key]
            top_guard = key

    top = None
    for key, val in guards_times.items():
        guard, time = key
        if top is None or val > guards_times[top]Z:
            top = key

    print(top_guard, top_time, top, top[0] * top[1])

def part_two(input):
    res=''
    print("Part Two: ", res)


data=get_data(day=4).splitlines()
data.sort()
part_one(data)
part_two(data)
