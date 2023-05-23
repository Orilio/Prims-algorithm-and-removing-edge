from heapq import heappush, heappop
import sys


class Node:
    def __init__(self):
        self.color = None
        self.edges = []


class Graph:
    def __init__(self, vertices):
        self.v = len(vertices)
        self.adjList = {vertex: Node() for vertex in vertices}

    def addEdge(self, u, v, w):
        self.adjList[u].edges.append((v, w))
        self.adjList[v].edges.append((u, w))

    def remove_edge(self, u, v, w):
        self.adjList[u].edges.remove((v, w))
        self.adjList[v].edges.remove((u, w))

    def check_containing_edge(self, u, v):
        for edge in self.adjList[v].edges:
            if edge[0] == u:
                return True

    def check_removing_edge_creates_not_tree(self, u, v):
        # checking if one of the vertex isn't connected to other vertex
        if len(self.adjList[u].edges) == 0 or len(self.adjList[v].edges) == 0:
            return True

    def __str__(self):
        g = '''graph?\n'''
        for v, n in self.adjList.items():
            g += f'{v}:\t {n.edges}\n'
        return g


def prims(g):
    active_edges = []
    new_graph = Graph(list(g.adjList))
    mst = {i: False for i in g.adjList}
    # cost = 0
    heappush(active_edges, [0, (None, list(g.adjList)[0])])

    while len(active_edges) != 0:
        wt, edge = heappop(active_edges)
        u = edge[1]
        prev = edge[0]

        if mst[u]:
            continue

        mst[u] = True
        if(prev):
            new_graph.addEdge(prev, u, wt)

        for v, w in g.adjList[u].edges:
            if not mst[v]:
                heappush(active_edges, [w, (u, v)])
    return new_graph

