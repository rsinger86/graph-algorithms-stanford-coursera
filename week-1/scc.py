from typing import List, Tuple
from collections import defaultdict
import sys, resource, time

# Increase recursion limit and stack size
sys.setrecursionlimit(2 ** 20)
hardlimit = resource.getrlimit(resource.RLIMIT_STACK)[1]
resource.setrlimit(resource.RLIMIT_STACK,(hardlimit,hardlimit))


def load_data() -> Tuple[dict, dict, int]:
    graph = defaultdict(lambda: {'explored': False, 'connected': []})
    graph_r = defaultdict(lambda: {'explored': False, 'connected': []})
    max_node = -1
    graph_file = 'data/graph.txt'

    with open(graph_file, 'r') as f:
        for line in f:
            from_node, to_node = line.strip().split(' ')
            from_node, to_node = int(from_node), int(to_node)
            graph[from_node]['connected'].append(to_node)
            graph_r[to_node]['connected'].append(from_node)

            if from_node > max_node:
                max_node = from_node

    return graph, graph_r, max_node


def collect_nodes_of_leader(graph: dict, leader: int) -> List[int]:
    graph[leader]['explored'] = True
    found = []
    q = [leader]

    while len(q) > 0:
        current_node = q.pop()
        found.append(current_node)

        for n in graph[current_node]['connected']:
            if graph[n]['explored'] is False:
                graph[n]['explored'] = True
                q.append(n)

    return found


def second_pass_loop(graph: dict, ranked_nodes: List[int]) -> dict:
    sccs = {}

    while len(ranked_nodes) > 0:
        leader = ranked_nodes.pop()

        if not graph[leader]['explored']:
            sccs[leader] = collect_nodes_of_leader(graph, leader)

    return sccs


def dfs_finish_times(graph: dict, node: int, ranked_finishes: List[int]):
    graph[node]['explored'] = True

    for n in graph[node]['connected']:
        if not graph[n]['explored']:
            dfs_finish_times(graph, n, ranked_finishes)

    ranked_finishes.append(node)


def first_pass_loop(graph, start_node: int) -> List[int]:
    ranked_finishes: List[int] = []
    current_node = start_node

    while current_node > 0:
        if not graph[current_node]['explored']:
            dfs_finish_times(graph, current_node, ranked_finishes)
        current_node -= 1

    return ranked_finishes


graph, graph_r, max_node = load_data()
finish_ranks = first_pass_loop(graph_r, max_node)
sccs = second_pass_loop(graph, finish_ranks)

five_largest_sizes = []

for leader in sccs:
    size = len(sccs[leader])

    if len(five_largest_sizes) < 5:
        five_largest_sizes.append(size)
        five_largest_sizes = sorted(five_largest_sizes, reverse=True)
    elif size > five_largest_sizes[4]:
        five_largest_sizes[4] = size
        five_largest_sizes = sorted(five_largest_sizes, reverse=True)

# [434821, 968, 459, 313, 211]
print(five_largest_sizes)