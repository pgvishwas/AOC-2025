import sys
sys.setrecursionlimit(10000)
from aoc2025.utils.utils import read_input
from itertools import combinations
import math

# Disjoint set data structure
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, i):
        # Path Compression
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)

        # If they are already in the same set, do nothing.
        if s1 != s2:

            # Union by Rank: Attach the smaller tree to the root of the larger tree.
            if self.rank[s1] < self.rank[s2]:
                self.parent[s1] = s2

            elif self.rank[s1] > self.rank[s2]:
                self.parent[s2] = s1

            else:
                # If ranks are equal, attach one to the other (e.g., s2 to s1)
                # AND increment the rank of the new root (s1).
                self.parent[s2] = s1
                self.rank[s1] += 1

            # A successful union occurred, return True (optional but useful)
            return True

        # Already merged, return False
        return False


def star1() -> int:
    # --- Data Loading and Edge Creation ---
    data = read_input()
    junction_boxes = []
    num_boxes = len(data)
    for i, d in enumerate(data):
        val = d.split(",")
        x, y, z = int(val[0]), int(val[1]), int(val[2])
        junction_boxes.append([x, y, z])

    potential_ids = list(range(num_boxes))
    potential_combos = list(combinations(potential_ids, 2))
    edge_list = []
    for id1, id2 in potential_combos:
        r1 = junction_boxes[id1]
        r2 = junction_boxes[id2]
        distance = math.dist(r1, r2)
        edge_list.append([distance, id1, id2])
    edge_list.sort(key=lambda x: x[0])

    # --- Kruskal's Algorithm (DSU) ---
    dsu = DSU(num_boxes)
    pairs_processed = 0

    for distance, r1, r2 in edge_list:
        ra = dsu.find(r1)
        rb = dsu.find(r2)

        dsu.union(r1, r2)
        pairs_processed += 1

        if pairs_processed == 1000:  # <- stop after 1000 *pairs*, not unions
            break

    # --- Final Circuit Tally and Multiplication ---

    # Count the size of each circuit (group by representative/root)
    circuit_sizes = {}
    for i in range(num_boxes):
        # Use find() to ensure path compression and accurate root identification
        root = dsu.find(i)
        circuit_sizes[root] = circuit_sizes.get(root, 0) + 1

    # Extract sizes, sort in descending order
    sizes = sorted(circuit_sizes.values(), reverse=True)

    # The puzzle requires the product of the three largest circuit sizes
    if len(sizes) < 3:
        print("Error: Not enough circuits formed.")
        return 0

    return sizes[0] * sizes[1] * sizes[2]


def star2() -> int:
    # --- Data Loading and Edge Creation (same as star1) ---
    data = read_input()
    junction_boxes = []
    num_boxes = len(data)
    for d in data:
        x, y, z = map(int, d.split(","))
        junction_boxes.append([x, y, z])

    potential_ids = list(range(num_boxes))
    potential_combos = list(combinations(potential_ids, 2))
    edge_list = []
    for id1, id2 in potential_combos:
        r1 = junction_boxes[id1]
        r2 = junction_boxes[id2]
        distance = math.dist(r1, r2)
        edge_list.append([distance, id1, id2])
    edge_list.sort(key=lambda x: x[0])

    # --- Kruskal until everything is in ONE circuit ---
    dsu = DSU(num_boxes)
    components = num_boxes
    last_pair = None  # store indices of the last successful connection

    for distance, a, b in edge_list:
        # We only care about edges that actually connect two *different* circuits
        merged = dsu.union(a, b)
        if merged:
            components -= 1
            last_pair = (a, b)

            if components == 1:
                # All junction boxes now in a single circuit
                break

    if last_pair is None:
        print("Error: Could not connect all junction boxes.")
        return 0

    i, j = last_pair
    x1 = junction_boxes[i][0]
    x2 = junction_boxes[j][0]

    return x1 * x2



if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
