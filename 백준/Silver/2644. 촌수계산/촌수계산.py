# 백준 2644 촌수계산

from collections import deque

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[v] + 1

n = int(input())
x, y = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
bfs(x)
if visited[y] == 0:
    print(-1)
else:
    print(visited[y]-1)