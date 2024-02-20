# 백준 17071 숨바꼭질 5

from collections import deque

MAX = 500001
N, K = map(int, input().split())

visited = [[-1 for _ in range(MAX)] for _ in range(2)]

def bfs():
    q = deque([(N,0)])
    visited[0][N] = 0
    
    while q:
        pos,time = q.popleft()
        
        for nx in [pos-1,pos+1,2*pos]:
            if 0<=nx<MAX and visited[(time+1) % 2][nx] == -1:
                visited[(time+1)%2][nx] = time + 1
                q.append((nx,time+1))
                
bfs()
t = 0
flag = 0
res = -1
while K < MAX:
    if visited[flag%2][K] != -1 and visited[flag%2][K] <= t:
        res =t 
        break
    flag += 1
    t += 1
    K += t
print(res)