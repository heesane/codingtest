# 백준 14502 연구소
from collections import deque
import copy
import sys

input = sys.stdin.readline
N, M = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(N)]

# 2 : 바이러스 , 1 : 벽 , 0 : 빈칸

dr = [-1,1,0,0]
dc = [0,0,-1,1]

count = 0

def bfs():
    graph_copy = copy.deepcopy(graph)
    q = deque([(i,j) for i in range(N) for j in range(M) if graph_copy[i][j] == 2])
    
    while q:
        r,c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and graph_copy[nr][nc] == 0:
                graph_copy[nr][nc] = 2
                q.append((nr,nc))
    count_safe(graph_copy)
    

# 안전영역 크기 구하기
def count_safe(graph_copy):
    global count
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph_copy[i][j] == 0:
                cnt += 1
    count = max(count,cnt)

def make_wall(count):
    if count == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(count+1)
                graph[i][j] = 0
make_wall(0)
print(count)