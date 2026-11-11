n = int(input("Enter number of hosts: "))
graph = []
print("Enter adjacency matrix:")
for i in range(n):
    graph.append(list(map(int, input().split())))
start = int(input("Enter starting host: "))
visited = [False] * n
queue = [start]
visited[start] = True
print("Broadcast Tree:")
while queue:
    u = queue.pop(0)
    for v in range(n):
        if graph[u][v] == 1 and not visited[v]:
            print(u, "->", v)
            visited[v] = True
            queue.append(v)
print("Broadcast completed")

