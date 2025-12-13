from aoc2025.utils.utils import read_input
def find_all_paths(graph, start_node, end_val="out"):
    all_paths = []

    def dfs(current_node, current_path):
        # If we reach the target value 'out'
        if current_node == end_val:
            all_paths.append(list(current_path))
            return

        # If the node isn't in our rack, we can't go further
        if current_node not in graph:
            return

        # Explore every neighbor of the current node
        for neighbor in graph[current_node]:
            current_path.append(neighbor)
            dfs(neighbor, current_path)
            current_path.pop() # Backtrack to explore the next neighbor

    # Start the recursion from 'you'
    dfs(start_node, [start_node])
    return all_paths
from functools import lru_cache
import sys
sys.setrecursionlimit(10**7)

def parse_graph(text):
    graph = {}
    for line in text.strip().splitlines():
        node, rest = line.split(":")
        graph[node.strip()] = rest.strip().split()
    return graph


def count_valid_paths(graph):
    visiting = set()  # recursion stack (not cached!)

    @lru_cache(None)
    def dfs(node, seen_dac, seen_fft):
        if node in visiting:
            return 0

        seen_dac |= (node == "dac")
        seen_fft |= (node == "fft")

        if node == "out":
            return 1 if seen_dac and seen_fft else 0

        visiting.add(node)
        total = 0
        for nxt in graph.get(node, []):
            total += dfs(nxt, seen_dac, seen_fft)
        visiting.remove(node)

        return total

    return dfs("svr", False, False)

def star1() -> int:
    data = read_input()
    data_value = []
    server_rack = {}
    for val in data:
        values = val.split(":")
        data_value.append(values)
    server_rack = {item[0]: item[1].split() for item in data_value}
    server_route = ['you']
    for servers in server_rack:
        if servers == 'you':
            server_path = server_rack[servers]
            break
    you_to_out_paths = find_all_paths(server_rack, "you")
    return len(you_to_out_paths)





    return 0

def star2() -> int:
    data = read_input()
    data_value = []
    server_rack = {}
    for val in data:
        values = val.split(":")
        data_value.append(values)
    server_rack = {item[0]: item[1].split() for item in data_value}
    results =count_valid_paths(server_rack)
    return results






if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
