# 백준 24482 알고리즘 수업 - 깊이 우선 탐색 4
from collections import deque
N, M, R = map(int,input().split())

graph = [[] for _ in range(N+1)]
depths = [-1 for _ in range(N+1)]
visited = [False for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for _ in range(N+1):
    graph[_].sort()

q = deque([(R,0)])

while q:
    node,depth = q.pop()
    if visited[node]: continue
    
    visited[node] = True
    depths[node] = depth
    for nn in graph[node]:
        if not visited[nn]:
            q.append((nn,depth+1))
            
print(*depths[1:],sep='\n')