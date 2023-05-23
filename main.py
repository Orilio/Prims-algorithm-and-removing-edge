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

    def remove_edge(self, u, v):
        self.adjList[u].edges = [e for e in self.adjList[u].edges if not e[0] == u]
        self.adjList[v].edges = [e for e in self.adjList[v].edges if not e[0] == v]

    def check_containing_edge(self, u, v):
        for edge in self.adjList[v].edges:
            if edge[0] == u:
                return True

    def __str__(self):
        g = '''graph:\n'''
        for v, n in self.adjList.items():
            g += f'{v}:\t {n.edges}\n'
        return g


def prims(g):
    active_edges = []
    mst = Graph(list(g.adjList))
    visited = {v: False for v in g.adjList}
    heappush(active_edges, [0, (None, list(g.adjList)[0])])

    while len(active_edges) != 0:
        wt, edge = heappop(active_edges)
        u = edge[1]
        prev = edge[0]

        if visited[u]:
            continue

        visited[u] = True
        if(prev):
            mst.addEdge(prev, u, wt)

        for v, w in g.adjList[u].edges:
            if not visited[v]:
                heappush(active_edges, [w, (u, v)])
    return mst


def bfs(g, node, colour):
    visited = {v: False for v in g.adjList}
    g.adjList[node].colour = colour
    visited[node] = True
    queue = [node]

    while queue:
        v = queue.pop(0)

        for edge in g.adjList[v].edges:
            u = edge[0]
            if u not in visited:
                g.adjList[u].colour = colour
                visited[u] = True
                queue.append(u)


def remove_edge_from_mst(g, mst, edge):
    if not mst.check_containing_edge(edge[0], edge[1]):
        return mst
    
    mst.remove_edge(edge[0], edge[1])
    bfs(mst, edge[0], 'blue')
    bfs(mst, edge[1], 'red')

    min_weight , min_edge = sys.maxint, None

    for v, vnode in g.adjList.items():
        for u, weight in vnode.edges:
            if vnode.colour != mst.adjList[u].colour:
                if weight < min_weight:
                    min_weight = weight
                    min_edge = (v, u, weight)

    if not min_edge:
        raise Exception('could not find a new MST')

    mst.addEdge(*min_edge)
    return mst


def main():
    v = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    g = Graph(v)

    g.addEdge('a', 'c', 23)
    g.addEdge('a', 'd', 5)
    g.addEdge('a', 'b', 12)
    g.addEdge('b', 'f', 7)
    g.addEdge('c', 'd', 18)
    g.addEdge('c', 'e', 17)
    g.addEdge('d', 'g', 9)
    g.addEdge('d', 'f', 10)
    g.addEdge('e', 'i', 16)
    g.addEdge('e', 'j', 14)
    g.addEdge('f', 'l', 20)
    g.addEdge('g', 'h', 4)
    g.addEdge('g', 'j', 3)
    g.addEdge('h', 'l', 8)
    g.addEdge('i', 'k', 7)
    g.addEdge('l', 'k', 12)

    print(f'Original - {g}')
    mst = prims(g)
    print(f'Minimal Spanning Tree - {mst}')

if __name__ == "__main__":
    main()