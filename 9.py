from aocd import get_data
from collections import deque

def play_game(players, limit):
    players_scores = [0] * players
    circle = deque([0])

    for marble in range(1, limit + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            players_scores[marble % players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)


    return players_scores

def part_one(data):
    print("Part One: ", max(play_game(int(data[0]), int(data[-2]))))

def part_two(data):
    print("Part Two: ", max(play_game(int(data[0]), int(data[-2]) * 100)))


data = get_data(day=9).split()
part_one(data)
part_two(data)
