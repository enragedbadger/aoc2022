# Advent of Code 2022 - day 12

from math import inf
from time import perf_counter


def data():
    with open("./inputs/day12", "r") as f:
        data = f.read().splitlines()
    return [list(row) for row in data]


def test_data():
    data = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""".splitlines()
    return [list(row) for row in data]


class Node:
    LOOKUP = {"S": "a", "E": "z"}

    def __init__(self, xy, value):
        self.xy = xy
        self.value = value
        self.visited = False
        self.distance = inf
        self.parent = None
        self.adjacent = []

    def __repr__(self):
        return (
            f"Node: xy={self.xy}, elevation={self.elevation}, value={self.value}, visited={self.visited}, "
            f"distance={self.distance}, parent={self.parent}, #adjacent={len(self.adjacent)}"
        )

    @property
    def elevation(self):
        return ord(self.LOOKUP.get(self.value, self.value))


class Graph:
    MOVES = {(-1, 0): "^", (1, 0): "v", (0, -1): "<", (0, 1): ">"}

    def __init__(self, data):
        self._data = data
        self.nodes = {(x, y): Node((x, y), col) for x, row in enumerate(self._data) for y, col in enumerate(row)}
        self._find_edges()

    def __repr__(self):
        return f"Graph: #nodes={len(self.nodes)}, start={self.start}, end={self.end}"

    @property
    def end(self):
        return [node.xy for node in self.nodes.values() if node.value == "E"][0]

    @property
    def start(self):
        return [node.xy for node in self.nodes.values() if node.value == "S"][0]

    def _find_edges(self):
        for node in self.nodes.values():
            for m in self.MOVES.keys():
                adjacent_xy = (node.xy[0] + m[0], node.xy[1] + m[1])
                if adjacent_xy in self.nodes:
                    delta_elevation = self.nodes[adjacent_xy].elevation - node.elevation
                    if delta_elevation <= 1:
                        node.adjacent.append(adjacent_xy)

    def reset(self):
        for node in self.nodes.values():
            node.visited = False
            node.distance = inf
            node.parent = None

    def solve(self, start):  # based on Dijkstra's algorithm
        self.nodes[start].distance = 0
        while True:
            distances = {v.distance: k for k, v in self.nodes.items() if not v.visited and not v.distance == inf}
            if len(distances):
                current_xy = distances[min(distances.keys())]
                for adjacent_xy in self.nodes[current_xy].adjacent:
                    if self.nodes[adjacent_xy].visited:
                        pass
                    else:
                        self.nodes[adjacent_xy].distance = self.nodes[current_xy].distance + 1
                        self.nodes[adjacent_xy].parent = current_xy
                self.nodes[current_xy].visited = True
            else:
                break

    def path(self):
        path = [self.end]
        while self.nodes[path[-1]].parent:
            path.append(self.nodes[path[-1]].parent)
        return path

    def plot(self, arrows=False):
        points = [["." for __ in row] for row in self._data]
        path = self.path()
        for ix, p in enumerate(path):
            if ix == 0 or not arrows:
                points[p[0]][p[1]] = "#"
            else:
                direction = (path[ix - 1][0] - path[ix][0], path[ix - 1][1] - path[ix][1])
                points[p[0]][p[1]] = self.MOVES[direction]
        for row in points:
            print("".join(map(str, row)))


def run(data):
    g = Graph(data)
    g.solve(g.start)
    g.plot(True)
    part1 = g.nodes[g.end].distance

    part2 = {n.xy: inf for n in g.nodes.values() if n.xy[1] == 0}
    for xy in part2.keys():
        g.reset()
        g.solve(xy)
        part2[xy] = g.nodes[g.end].distance

    return part1, min(part2.values())


if __name__ == "__main__":
    now = perf_counter()
    print(run(data()))
    print(f"total time {perf_counter() - now}")
