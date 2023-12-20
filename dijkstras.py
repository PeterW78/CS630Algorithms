import heapq

def dijkstra(g, start):
    distances = {node: float('infinity') for node in g}
    distances[start] = 0
    priorityQueue = [(0, start)]

    while priorityQueue:
        cur, u = heapq.heappop(priorityQueue)
        if cur > distances[u]:
            continue
        for neighbor, weight in g[u].items():
            distance = cur + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priorityQueue, (distance, neighbor))

    return distances

graph = {
    'A': {'B': 1, 'C': 4, 'F': 3},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1, 'F': 6},
    'D': {'B': 5, 'C': 1},
    'E': {'F': 1},
    'F': {'A': 3, 'C': 6, 'E': 1}
}

start = 'A'
result = dijkstra(graph, start)
print("Shortest distances from", start, ":", result)
