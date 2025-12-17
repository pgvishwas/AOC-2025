import math

from aoc2015.utils.utils import read_input
from itertools import permutations

def star1() -> int:
    data = read_input()
    distance_log = {}
    distance = {}
    places_combo = set()
    for s in data:
        left, dist = s.split(" = ")
        src, dst = left.split(" to ")
        distance_log[src,dst] = int(dist)
        distance_log[dst,src] = int(dist)
        places_combo.add(src)
        places_combo.add(dst)
    places = tuple(places_combo)
    for (s,d),dist in distance_log.items():
        distance[(s,d)] = dist
    shortest = float("inf")
    def find_distance(route):
        total_distance = 0
        for i in range(len(route)-1):
            edge = (route[i],route[i+1])
            if edge not in distance:
                return math.inf
            total_distance+= distance[edge]
        return total_distance

    for routes in permutations(places):
        d = find_distance(routes)
        if d != math.inf:
            if d < shortest:
                shortest = d


    return shortest


def star2() -> int:
    data = read_input()
    distance_log = {}
    distance = {}
    places_combo = set()
    for s in data:
        left, dist = s.split(" = ")
        src, dst = left.split(" to ")
        distance_log[src, dst] = int(dist)
        distance_log[dst, src] = int(dist)
        places_combo.add(src)
        places_combo.add(dst)
    places = tuple(places_combo)
    for (s, d), dist in distance_log.items():
        distance[(s, d)] = dist
    longest = 0

    def find_distance(route):
        total_distance = 0
        for i in range(len(route) - 1):
            edge = (route[i], route[i + 1])
            if edge not in distance:
                return math.inf
            total_distance += distance[edge]
        return total_distance

    for routes in permutations(places):
        d = find_distance(routes)
        if d != math.inf:
            if d > longest:
                longest = d

    return longest


if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
