
n = int(input("Enter number of vertices: "))

graph = []

print("Enter adjacency matrix:")
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

start = int(input("Enter starting vertex: "))

dist = [999] * n
visited = [False] * n

dist[start] = 0

for i in range(n):
    min_dist = 999
    u = -1

    for j in range(n):
        if not visited[j] and dist[j] < min_dist:
            min_dist = dist[j]
            u = j

    if u == -1:
        break

    visited[u] = True

    for v in range(n):
        if graph[u][v] > 0 and not visited[v]:
            new_dist = dist[u] + graph[u][v]

            if new_dist < dist[v]:
                dist[v] = new_dist

print("Shortest distances from vertex", start)

for i in range(n):
    print("To vertex", i, "=", dist[i])
