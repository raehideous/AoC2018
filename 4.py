from collections import defaultdict
import operator
from aocd import get_data

def get_minutes(time):
    return int(time[-2:])


def solve(input):
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

    strategy_one(times, guards_times)
    strategy_two(guards_times)

def strategy_one(times, guards_times):
    top_time = 0
    guard_with_top_time = None
    for key in times:
        if times[key] > top_time:
            top_time = times[key]
            guard_with_top_time = key

    guard_with_top_time_minutes = [(key, val) for key, val in guards_times.items() if guard_with_top_time in key]

    most_asleep_guard = None
    for key, val in guard_with_top_time_minutes:
        if most_asleep_guard is None or val > guards_times[most_asleep_guard]:
            most_asleep_guard = key

    print('Part Two:', most_asleep_guard[0] * most_asleep_guard[1])


def strategy_two(guards_times):
    most_freq_same_minute = None
    for key, val in guards_times.items():
        if most_freq_same_minute is None or val > guards_times[most_freq_same_minute]:
            most_freq_same_minute = key
    print('Part Two:', most_freq_same_minute[0] * most_freq_same_minute[1])



data=get_data(day=4).splitlines()
data.sort()

solve(data)
