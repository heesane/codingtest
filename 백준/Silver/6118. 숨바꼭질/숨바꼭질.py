# 백준 6118 숨바꼭질

N, M = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
from collections import deque

def bfs(start):
    queue = deque([start])
    visited = [0] * (N+1)
    visited[start] = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[v] + 1
    return visited

result = bfs(1)
max_value = max(result)
max_count = result.count(max_value)
print(result.index(max_value), max_value-1, max_count)