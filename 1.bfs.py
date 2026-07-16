from collections import deque

graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [],
    6: []
}

visited = []
queue = deque([1])

while queue:
    node = queue.popleft()
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        queue.extend(graph[node])
