from aocd import get_data

def get_metatadatas_sum (tree):
    child_nodes = tree.pop(0)
    metas = tree.pop(0)
    return sum(get_metatadatas_sum(tree) for i in range(child_nodes)) + sum(tree.pop(0) for i in range(metas))

def get_node_value (tree):
    child_nodes = tree.pop(0)
    metas_q = tree.pop(0)
    values = [get_node_value(tree) for i in range(child_nodes)] # if it has children... get values for them
    metadatas = [tree.pop(0) for i in range(metas_q)] # this will run on node without children (is invoked recursively)

    if child_nodes == 0:
        return sum(metadatas)
    return sum(values[i-1] for i in metadatas if i - 1 in range(child_nodes))

def part_one(input):
    tree = [int(i) for i in data.split()]
    print('Part One: ', get_metatadatas_sum(tree))

def part_two(data):
    tree = [int(i) for i in data.split()]
    print("Part Two: ", get_node_value(tree))


data = get_data(day=8)
part_one(data)
part_two(data)
