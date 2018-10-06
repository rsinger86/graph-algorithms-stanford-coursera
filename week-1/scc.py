from typing import List, Tuple
from collections import defaultdict
import random
import copy


def load_graph() -> Tuple[dict, int]:
    graph = defaultdict(lambda: {'explored': False, 'connected': []})
    max_node = None

    with open('data/graph.txt', 'r') as f:
        for line in f:
            from_node, to_node = line.strip().split(' ')
            from_node, to_node = int(from_node), int(to_node)
            graph[from_node]['connected'].append(to_node)

            if max_node is None or from_node > max_node:
                max_node = from_node

    return graph, max_node


def reverse_graph(graph):
    graph_r = defaultdict(lambda: {'explored': False, 'connected': []})

    for node in graph:
        for out in graph[node]:
            graph_r[out]['connected'].append(node)

    return graph_r


def dfs_first_pass(graph: dict, node: int, finishes: List[int]):
    graph[node]['explored'] = True

    for connected_node in graph[node]['connected']:
        dfs(graph, connected_node, finishes)

    finishes.append(node)


def dfs_loop_first_pass(graph, start_node: int) -> List[int]:
    finishes: List[int] = []
    current_node = start_node

    while current_node > 0:
        for connected_node in graph[current_node]['connected']:
            if graph[connected_node]['explored']:
                continue
            
            current_leader = current_node

            dfs_first_pass(graph, 
                connected_node, 
                current_finish_rank,
                finishes)

        current_node -= 1
    
    return finishes


graph, max_node = load_graph()
print('Done building graph', max_node)
graph_r = reverse_graph(graph)
print('Done reversing')
dfs_loop_first_pass(graph_r, max_node)
print('Done with dfs loop')

