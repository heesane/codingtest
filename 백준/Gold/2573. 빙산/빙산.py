# 백준 2573번 빙산

# BFS

from collections import deque

N, M = map(int,input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(x,y,visited):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    
    while q:
        cx,cy = q.popleft()
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            if not visited[nx][ny] and graph[nx][ny] != 0:
                q.append((nx,ny))
                visited[nx][ny] = True

def count_ice():
    visited = [[False] * M for _ in range(N)]
    cnt = 0 
    
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and graph[i][j] != 0 :
                bfs(i,j,visited)
                cnt += 1
    return cnt

def melt_ice():
    new_graph = [[0] * M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0:
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx < 0 or nx >= N or ny < 0 or ny >= M:
                        continue
                    if graph[nx][ny] == 0:
                        cnt += 1
                new_graph[i][j] = max(0, graph[i][j] - cnt)
    return new_graph

def check_ice():
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0:
                return False
    return True

def solve():
    global graph
    years = 0
    while True:
        iceberg = count_ice()
        
        if iceberg == 0:
            return 0
        
        if iceberg >= 2:
            return years
        
        graph = melt_ice()
        years += 1
        
        if check_ice():
            return 0

print(solve())