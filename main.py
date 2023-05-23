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

    min_weight , min_edge = sys.maxsize, None

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
    # v = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    # g = Graph(v)

    # g.addEdge('a', 'c', 23)
    # g.addEdge('a', 'd', 5)
    # g.addEdge('a', 'b', 12)
    # g.addEdge('b', 'f', 7)
    # g.addEdge('c', 'd', 18)
    # g.addEdge('c', 'e', 17)
    # g.addEdge('d', 'g', 9)
    # g.addEdge('d', 'f', 10)
    # g.addEdge('e', 'i', 16)
    # g.addEdge('e', 'j', 14)
    # g.addEdge('f', 'l', 20)
    # g.addEdge('g', 'h', 4)
    # g.addEdge('g', 'j', 3)
    # g.addEdge('h', 'l', 8)
    # g.addEdge('i', 'k', 7)
    # g.addEdge('l', 'k', 12)


    v =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
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
    print('##################################################################')

    mst = prims(g)
    print(f'Minimal Spanning Tree - {mst}')
    print('##################################################################')


    print("Removing an edge that doesn't affect the minimal spanning tree:")
    print('Edge: (a,h)')
    mst = remove_edge_from_mst(g,mst,('a', 'h'))
    print(f'Minimal Spanning Tree after removal - {mst}')
    print('##################################################################')


    print('Removing an edge that does affect the minimal spanning tree')
    print('Edge: (r,t)')
    mst = remove_edge_from_mst(g,mst,('r', 't'))
    print(f'Minimal Spanning Tree after removal - {mst}')


if __name__ == "__main__":
    main()






































# def creating_list_of_edges(num_vertices):
#     return list(string.ascii_lowercase)[0:num_vertices]


# def creating_initial_graph(g, vertices):
#     vertices_remove = vertices.copy()

#     counter_of_edges = 0
#     num_vertices = len(vertices)
#     # looping over the list except for the last vertex, otherwise we will create an empry list
#     for vertex in vertices[0:num_vertices - 1]:
#         # removing the vertex so we wont create an edge to the same vertex
#         vertices_remove.remove(vertex)
#         # contains all the edges created for the vertex were on
#         created_edges = []
#         # creating a random number of edges, the number of edges might be lower if dulicates were created
#         for i in [i + 1 for i in range(random.randint(0, 8))]:
#             edge = tuple((vertex, random.choice(vertices_remove)))

#             # checking if  the edge that was created wasn't created before
#             if edge not in created_edges:
#                 created_edges.append(edge)
#                 counter_of_edges += 1
#                 # print("g.addEdge('" + edge[0] + "', '" + edge[1] + "', " + str(random.randint(0, 30)) + ")")
#                 g.addEdge(edge[0], edge[1], random.randint(0, 30))

#     print("num of edges created " + str(counter_of_edges))


# num_vertices = 20
# list_of_vertices = creating_list_of_edges(num_vertices)
# g = Graph(list_of_vertices)

# creating_initial_graph(g, list_of_vertices)
# print(g)