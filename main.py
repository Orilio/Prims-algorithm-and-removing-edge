from heapq import heappush, heappop
import sys


class Node:
    def __init__(self):
        self.colour = None
        self.edges = []


class Graph:
    def __init__(self, vertices):
        self.v = len(vertices)
        self.adjList = {vertex: Node() for vertex in vertices}

    def addEdge(self, u, v, w):
        self.adjList[u].edges.append((v, w))
        self.adjList[v].edges.append((u, w))

    def remove_edge(self, u, v):
        self.adjList[u].edges = [
            e for e in self.adjList[u].edges if not e[0] == v]
        self.adjList[v].edges = [
            e for e in self.adjList[v].edges if not e[0] == u]

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
            if not visited[u]:
                g.adjList[u].colour = colour
                visited[u] = True
                queue.append(u)


def remove_edge_from_mst(g, mst, edge):
    if not mst.check_containing_edge(edge[0], edge[1]):
        return mst

    mst.remove_edge(edge[0], edge[1])
    bfs(mst, edge[0], 'blue')
    bfs(mst, edge[1], 'red')

    min_weight, min_edge = sys.maxsize, None

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
    v = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
         'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
    g = Graph(v)

    g.addEdge('a', 'h', 21)
    g.addEdge('a', 'o', 25)
    g.addEdge('a', 'e', 5)
    g.addEdge('a', 'c', 1)
    g.addEdge('a', 'd', 21)
    g.addEdge('b', 't', 20)
    g.addEdge('b', 'e', 23)
    g.addEdge('b', 'q', 14)
    g.addEdge('c', 'j', 29)
    g.addEdge('d', 'n', 14)
    g.addEdge('d', 'o', 10)
    g.addEdge('d', 'i', 22)
    g.addEdge('e', 's', 9)
    g.addEdge('e', 'l', 17)
    g.addEdge('e', 'm', 18)
    g.addEdge('f', 'r', 25)
    g.addEdge('f', 'o', 13)
    g.addEdge('f', 'g', 25)
    g.addEdge('f', 's', 2)
    g.addEdge('g', 'p', 26)
    g.addEdge('g', 't', 2)
    g.addEdge('g', 'q', 13)
    g.addEdge('g', 'l', 7)
    g.addEdge('h', 's', 24)
    g.addEdge('h', 'o', 2)
    g.addEdge('i', 'o', 18)
    g.addEdge('i', 'n', 24)
    g.addEdge('j', 'p', 11)
    g.addEdge('j', 's', 25)
    g.addEdge('k', 'r', 19)
    g.addEdge('k', 'o', 16)
    g.addEdge('k', 'q', 23)
    g.addEdge('k', 'l', 11)
    g.addEdge('k', 'p', 9)
    g.addEdge('k', 'm', 2)
    g.addEdge('l', 'q', 13)
    g.addEdge('l', 'm', 3)
    g.addEdge('m', 's', 2)
    g.addEdge('m', 'r', 29)
    g.addEdge('m', 't', 27)
    g.addEdge('n', 'o', 30)
    g.addEdge('n', 'q', 11)
    g.addEdge('n', 't', 2)
    g.addEdge('o', 't', 15)
    g.addEdge('o', 'p', 27)
    g.addEdge('o', 'r', 30)
    g.addEdge('o', 's', 16)
    g.addEdge('p', 'r', 1)
    g.addEdge('p', 'q', 14)
    g.addEdge('q', 't', 28)
    g.addEdge('q', 's', 7)
    g.addEdge('q', 'r', 21)
    g.addEdge('r', 't', 6)
    g.addEdge('r', 's', 21)
    g.addEdge('s', 't', 29)

    print(f'Original - {g}')
    print('##################################################################\n')

    mst = prims(g)
    print(f'Minimal Spanning Tree - {mst}')
    print('##################################################################\n')

    print("Removing an edge that doesn't affect the minimal spanning tree:")
    print('Edge: (a,h)')
    mst = remove_edge_from_mst(g, mst, ('a', 'h'))
    print(f'Minimal Spanning Tree after removal - {mst}')
    print('##################################################################\n')

    print('Removing an edge that does affect the minimal spanning tree')
    print('Edge: (r,t)')
    mst = remove_edge_from_mst(g, mst, ('r', 't'))
    print(f'Minimal Spanning Tree after removal - {mst}')


if __name__ == "__main__":
    main()
