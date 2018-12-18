from aocd import get_data
import re

def get_text_moment(vectors):
    min_x_diff = float("inf")
    min_y_diff = float("inf")
    m_x_i = 0
    m_y_i = 0
    test_limit = 20000
    for i in range(test_limit):
        minx = min(x + i * dx for (x, y, dx, dy) in vectors)
        maxx = max(x + i * dx for (x, y, dx, dy) in vectors)
        miny = min(y + i * dy for (x, y, dx, dy) in vectors)
        maxy = max(y + i * dy for (x, y, dx, dy) in vectors)
        cmxd = maxx - minx
        cmyd = maxy - miny
        if cmxd < min_x_diff:
            min_x_diff = cmxd
            m_x_i = i
        if cmyd < min_y_diff:
            min_y_diff = cmyd
            m_y_i = i

    print(m_x_i, m_y_i, min_x_diff, min_y_diff)
    if m_x_i == m_y_i:
        return m_x_i
    return None

def solve(input):
    vectors = [[int(n) for n in re.findall(r'-?\d+', line)] for line in input]
    after_seconds = get_text_moment(vectors)
    matrix = [[' '] * 200 for i in range(200)]
    for (x, y, dx,dy) in vectors:
        matrix[y + after_seconds * dy][x + after_seconds * dx] = 'X'

    print('Part One: ')
    for row in matrix:
        print(''.join(row))
    print('Part Two: ', after_seconds)


data = get_data(day=10).splitlines()
solve(data)
