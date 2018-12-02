from aocd import get_data
from collections import Counter

def part_one(input):
    counts=[0, 0] #array of occurences two and three times

    for word in input.split():
        occurences_count=[j for i, j in Counter(word).most_common()]
        if 3 in occurences_count:
            counts[0]+=1
        if 2 in occurences_count:
            counts[1]+=1

    print('Part One: ', counts[0]*counts[1])


def part_two(input):
    words=input.split()
    for word in words:
        for wordCmp in words:
            diffs = 0
            for idx, char in enumerate(word):
                if char != wordCmp[idx]:
                    diffs+=1
            if diffs==1:
                difference=[ch for idx, ch in enumerate(word) if ch == wordCmp[idx]]
                print('Part Two: ', ''.join(difference))
                return


data = get_data(day=2)
part_one(data)
part_two(data)
