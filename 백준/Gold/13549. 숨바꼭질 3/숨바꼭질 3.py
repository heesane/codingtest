# 백준 13549 숨바꼭질 3

from collections import deque

N,K = map(int, input().split())

MAX = 100001

visited = [0] * MAX

def bfs():
    queue = deque([N])
    while queue:
        x = queue.popleft()
        if x == K:
            print(visited[x])
            return
        for nx in (x-1, x+1, x*2):
            if 0 <= nx < MAX and not visited[nx]:
                if nx == x*2 and x != 0:
                    visited[nx] = visited[x]
                    queue.appendleft(nx)
                else:
                    visited[nx] = visited[x] + 1
                    queue.append(nx)
                    
bfs()
