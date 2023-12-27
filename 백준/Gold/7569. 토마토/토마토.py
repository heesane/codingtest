## 7569 토마토
## 10:50

from collections import deque            
    
m,n,h = map(int,input().split())
box = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
q = deque()
dx = [0,0,1,-1,0,0]
dy = [1,-1,0,0,0,0]
dz = [0,0,0,0,1,-1]

for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                q.append((i,j,k))
                
while q:
    x,y,z = q.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0<=nx<h and 0<=ny<n and 0<=nz<m and box[nx][ny][nz] == 0:
            box[nx][ny][nz] = box[x][y][z] + 1
            q.append((nx,ny,nz))

ans = 0
for i in box:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit()
        ans = max(ans,max(j))

print(ans-1)