## 2178. 미로 탐색
## 14:14

N,M = map(int,input().split())

map_list = []
for _ in range(N):
    map_list.append(list(map(int,input())))

answer = 0
def bfs(x,y):
    queue = [[x,y]]
    while queue:
        a,b = queue[0][0],queue[0][1]
        del queue[0]
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < M and map_list[nx][ny] == 1:
                global answer
                answer += 1
                queue.append([nx,ny])
                map_list[nx][ny] = map_list[a][b] + 1
bfs(0,0)
print(map_list[N-1][M-1])