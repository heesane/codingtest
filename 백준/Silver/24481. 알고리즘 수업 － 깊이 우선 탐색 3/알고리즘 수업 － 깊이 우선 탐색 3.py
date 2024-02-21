import sys
from collections import deque
input = sys.stdin.readline
n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
depth = [-1 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()
    
q = deque([(r,0)]) # (node,depth)

while q:
    node, node_depth = q.popleft()
    if visited[node]: continue
    visited[node] = True
    depth[node] = node_depth

    for nn in reversed(graph[node]):
        if not visited[nn]:
            q.appendleft((nn, node_depth+1))

print(*depth[1:],sep='\n')