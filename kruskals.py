class UnionFind:
    def __init__(self, vertices):
        self.parent = {vertex: vertex for vertex in vertices}
        self.rank = {vertex: 0 for vertex in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)

        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                self.rank[root2] += 1

def kruskal(graph):
    edges = []
    for vertex in graph:
        for neighbor, weight in graph[vertex].items():
            edges.append((weight, vertex, neighbor))

    edges.sort()
    vertices = set()
    for edge in edges:
        vertices.add(edge[1])
        vertices.add(edge[2])
    minimumSpanningTree = []
    unionFind = UnionFind(vertices)

    for edge in edges:
        weight, vertex1, vertex2 = edge
        if unionFind.find(vertex1) != unionFind.find(vertex2):
            minimumSpanningTree.append(edge)
            unionFind.union(vertex1, vertex2)
    return minimumSpanningTree


graph = {
    'A': {'B': 1, 'C': 4, 'F': 3},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1, 'F': 6},
    'D': {'B': 5, 'C': 1},
    'E': {'F': 1},
    'F': {'A': 3, 'C': 6, 'E': 1}
}

minimumSpanningTree = kruskal(graph)
print("Minimum Spanning Tree:", minimumSpanningTree)
