# 백준 14442 벽 부수고 이동하기 2

from collections import deque

N,M,K = map(int,input().split())

graph = [list(map(int,input())) for _ in range(N)]

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def bfs():
    q = deque([(0,0,K)]) # row, column, move, 부실수 있는 벽의 수
    visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)] # 방문 여부, 벽을 부신 여부
    visited[0][0][K] = 1
    while q:
        r,c,wall = q.popleft()
        
        if r == N -1 and c == M-1:
            return visited[r][c][wall]
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if 0 <= nr < N and 0<=nc<M :
                
                if graph[nr][nc] == 0 and visited[nr][nc][wall] == 0:
                    visited[nr][nc][wall] = visited[r][c][wall] + 1
                    q.append((nr,nc,wall))

                elif graph[nr][nc] == 1 and wall > 0 and visited[nr][nc][wall-1] == 0:
                    visited[nr][nc][wall-1] = visited[r][c][wall] + 1
                    q.append((nr,nc,wall-1))
    return -1
print(bfs())
    
    