from typing import List, Tuple
from collections import defaultdict


def load_data() -> dict:
    graph = defaultdict(lambda: {'explored': False, 'connected': []})
    graph_file = 'data/graph.txt'

    with open(graph_file, 'r') as f:
        for line in f:
            parts = line.split()
            node = int(parts.pop(0))
            
            for connected_to in parts:
     
                connected_node, length = connected_to.split(',')
                connected_node, length = int(connected_node), int(length)
                graph[node]['connected'].append((connected_node, length))

    return graph


def find_best_next_node(graph: dict, 
                        explored_nodes: List[int], 
                        shortest_store: dict) -> Tuple[int, int]:

    best_next: Tuple[int, int] = None

    for node in explored_nodes:
        for connected_to in graph[node]['connected']:
            if connected_to[0] in explored_nodes:
                continue

            connected_node, connected_length = connected_to
            potential_distance = shortest_store[node] + connected_length

            if best_next is None or potential_distance < best_next[1]:
                best_next = (connected_node, potential_distance)

    return best_next


def calc_shortest_paths(graph: dict, start_node: int) -> dict:
    shortest_store = {}
    explored_nodes = [start_node]
    total_nodes = len(graph)
    shortest_store[start_node] = 0

    while len(explored_nodes) < total_nodes:
        best_next = find_best_next_node(graph, explored_nodes, shortest_store)
        node, distance_to = best_next
        explored_nodes.append(node)
        shortest_store[node] = distance_to

    return shortest_store
        

graph = load_data()
shortest_distances_to = calc_shortest_paths(graph, 1)

grading_assignment_nodes = [7,37,59,82,99,115,133,165,188,197]
scores = []

for n in grading_assignment_nodes:
    scores.append(shortest_distances_to[n])

print(scores)