# 백준 12851 숨바꼭질 2

from collections import deque

N,K = map(int, input().split())

MAX = 100001

visited = [0] * MAX

def bfs():
    cnt = 0
    q = deque()
    q.append(N)
    
    while q:
        x = q.popleft()
        if x == K:
            cnt += 1
            continue
        for nx in (x-1,x+1,x*2):
            if 0<=nx<MAX:
                if visited[nx] == 0 or visited[nx] == visited[x] + 1:
                    visited[nx] = visited[x] + 1
                    q.append(nx)
    return visited[K],cnt
print(*bfs(),sep='\n')