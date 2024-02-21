# 백준 24444 알고리즘 수업 - 너비 우선 탐색 1

from collections import deque

N, M, R = map(int,input().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
check = 1
visited[R] =check 

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for _ in range(N+1):
    graph[_].sort()


def bfs():
    global check
    q = deque([R])
    while q:
        x = q.popleft()
        
        for nx in graph[x]:
            if not visited[nx]:
                visited[nx] = check + 1
                q.append(nx)
                check += 1
    
bfs()

print(*visited[1:],sep='\n')