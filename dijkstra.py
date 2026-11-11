n = int(input("Enter number of vertices: "))
graph = []
print("Enter adjacency matrix:")
for i in range(n):
    graph.append(list(map(int, input().split())))
start = int(input("Enter starting vertex: "))
dist = [999] * n
visited = [False] * n
dist[start] = 0
for i in range(n):
    u = -1
    for j in range(n):
        if not visited[j] and (u == -1 or dist[j] < dist[u]):
            u = j
    visited[u] = True

    for v in range(n):
        if graph[u][v] > 0 and not visited[v]:
            new = dist[u] + graph[u][v]

            if new < dist[v]:
                dist[v] = new

print("Shortest distances from source:")
print(dist)
