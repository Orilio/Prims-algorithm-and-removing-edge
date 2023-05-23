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

    def remove_edge(self, u, v):
            

        self.adjList[u].edges = [edge for edge in self.adjList[u].edges if not edge[0] == u]
        self.adjList[v]

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
    new_graph = Graph(list(g.adjList))
    mst = {i: False for i in g.adjList}
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


def bfs(visited_vertices, graph, node, colour):  # function for BFS
    queue = []  # Initialize a queue
    # set colour of first node to colour
    graph.adjList[node].colour = colour

    visited_vertices.append(node)
    queue.append(node)

    # we need to add the part where we add the colour to the node
    while queue:  # Creating loop to visit each node
        m = queue.pop(0)
        print(m, end=" ")

        # finding the edge neighbor vertic for the node
        for edge in graph.adjList[m].edges:
            if edge[0] not in visited_vertices:
                # you go over the graph and in the vertix location adding the colour
                graph.adjList[edge[0]].colour = colour
                visited_vertices.append(edge[0])
                queue.append(edge[0])


def remove_edge_create_new_minimum_spanning_tree(original_graph, prim_graph, edge):
    if not prim_graph.check_containing_edge(edge[0], edge[1]):
        return prim_graph
    prim_graph.remove_edge(edge[0], edge[1], edge[2])

    # running BFS from both sides of the prim graph
    bfs([], prim_graph, edge[0], "blue")  # function calling
    bfs([], prim_graph, edge[1], "red")  # function calling

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