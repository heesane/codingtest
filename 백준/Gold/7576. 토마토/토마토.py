## 7569 토마토
## 10:50

from collections import deque            
    
M,N = map(int,input().split()) 
graph = [list(map(int,input().split())) for _ in range(N)]
q = deque()

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append([i,j])

dx, dy = [1,-1,0,0],[0,0,1,-1]
while q:
    x,y = q.popleft()
    
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y] + 1
            q.append([nx,ny])
            
answer = 0
for line in graph:
    for t in line:
        if t == 0:
            print(-1)
            exit()
    answer = max(answer,max(line))
print(answer-1)