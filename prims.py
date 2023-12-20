import heapq

def prim(graph):
    start_node = list(graph.keys())[0]
    visited = set([start_node])
    edges = [(weight, start_node, neighbor) for neighbor, weight in graph[start_node].items()]
    heapq.heapify(edges)
    minimumSpanningTree = []

    while edges:
        weight, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            minimumSpanningTree.append((weight, u, v))
            for neighbor, weight in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (weight, v, neighbor))
    return minimumSpanningTree


graph = {
    'A': {'B': 1, 'C': 4, 'F': 3},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1, 'F': 6},
    'D': {'B': 5, 'C': 1},
    'E': {'F': 1},
    'F': {'A': 3, 'C': 6, 'E': 1}
}

minimumSpanningTree = prim(graph)
print("Minimum Spanning Tree:", minimumSpanningTree)
