from aocd import get_data
import re
import numpy as np

def part_one(claims):
    fabric=np.zeros((1000, 1000))
    for claim, start_x, start_y, width, height in claims:
        fabric[start_x:start_x + width, start_y:start_y + height] += 1

    print(np.sum(fabric > 1))
    return fabric



def part_two(claims, fabric):
    for claim, start_x, start_y, width, height in claims:
        if np.all(fabric[start_x:start_x + width, start_y:start_y + height]==1):
            print("Part Two: ", claim)
            return claim


data = get_data(day=3)
claims=[[*map(int, re.findall(r'\d+', l))] for l in data.splitlines() if l]
fabric=part_one(claims)
part_two(claims, fabric)
