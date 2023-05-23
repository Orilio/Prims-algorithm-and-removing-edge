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


def bfs(visited, graph, node, colour):
    queue = []
    visited = {}
    # set colour of first node
    graph.adjList[node].colour = colour
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)

        for edge in graph.adjList[m].edges:
            if edge[0] not in visited:
                # you go over the graph and in the vertix location adding the colour
                graph.adjList[edge[0]].colour = colour
                visited.append(edge[0])
                queue.append(edge[0])


def remove_edge_create_new_minimum_spanning_tree(original_graph, prim_graph, edge):
    if not prim_graph.check_containing_edge(edge[0], edge[1]):
        return prim_graph
    prim_graph.remove_edge(edge[0], edge[1])

    # running BFS from both sides of the prim graph
    bfs([], prim_graph, edge[0], 'blue')
    bfs([], prim_graph, edge[1], 'red')

    # setting high min_weight
    min_weight , min_edge = sys.maxint, None
    # getting every edge for v and then comaparing the colour if diffrent than checking of smaller than min weight
    for v, vnode in original_graph.adjList.items():
        for u, weight in vnode.edges:
            if vnode.colour != prim_graph.adjList[u].colour:
                if weight < min_weight:
                    min_weight = weight
                    min_edge = [weight, (v, u)]

    if not min_edge:
        raise Exception('could not find a new MST')
    prim_graph.addEdge(min_edge[0], min_edge[1], min_edge[2])
    prim_graph.addEdge()

    return prim_graph