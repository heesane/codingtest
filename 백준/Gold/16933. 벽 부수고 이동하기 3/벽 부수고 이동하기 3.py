# 백준 16933 벽 부수고 이동하기 3
from collections import deque

N,M,K = map(int,input().split())

graph = [list(map(int,input())) for _ in range(N)]

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def bfs():
    q = deque([(0,0,1,K)]) # row, col, time, wall
    visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]
    visited[0][0][K] = 0

    while q:
        r,c,t,w = q.popleft()
        daytime = t % 2
        if r == N - 1 and c == M - 1:
            return visited[r][c][w] + 1
        
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M : # 낮인 경우,
                if visited[nr][nc][w] == 0 and graph[nr][nc] == 0: # 길인 경우,
                    visited[nr][nc][w] = t
                    q.append((nr,nc,t+1,w))
                        
                elif visited[nr][nc][w-1] == 0 and graph[nr][nc] == 1 and w: # 벽인 경우,
                    if daytime: # 낮인 경우,
                        visited[nr][nc][w-1] = t
                        q.append((nr,nc,t+1,w-1))
                    else: # 밤인 경우,
                        q.append((r,c,t+1,w))
    return -1

print(bfs())