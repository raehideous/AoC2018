from aocd import get_data
import networkx as nx

def part_one(input):
    graph = nx.DiGraph()
    for line in input.splitlines():
        words = line.split()
        graph.add_edge(words[1], words[-3])

    print('Part One: ', ''.join(nx.lexicographical_topological_sort(graph)))
    return graph

def part_two(graph):
    ASCII_DIFF = 64
    MAX_TASKS_IN_PROGRESS = 5
    TASK_CONST_TIME = 60

    tasks_in_progress = []  # [task, task_time]
    seconds = 0
    while tasks_in_progress or graph:
        available_tasks =[t for t in graph if t not in [t for t, s in tasks_in_progress] and graph.in_degree(t) == 0]
        # if there is task to do and we have worker for that...
        if available_tasks and len(tasks_in_progress) < MAX_TASKS_IN_PROGRESS:
            task = available_tasks[0]
            tasks_in_progress.append([task, ord(task) - ASCII_DIFF + TASK_CONST_TIME])
        else:  # if not, then workers work...
            smallest_task_time = min([time for task, time in tasks_in_progress])
            completed_tasks = [task for task, time in tasks_in_progress if time == smallest_task_time]
            tasks_in_progress = [(task, time - smallest_task_time) for task, time in tasks_in_progress if task not in completed_tasks]
            seconds += smallest_task_time
            graph.remove_nodes_from(completed_tasks)
    print('Part Two:', seconds)

data = get_data(day=7)
graph = part_one(data)
part_two(graph)
