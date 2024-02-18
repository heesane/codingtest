from collections import deque

def solution(maps):
    def bfs(start, end):
        visited = [[0 for _ in range(max_r)] for _ in range(max_c)]

        queue = deque()
        queue.append(start)

        while queue:
            c, r = queue.popleft()

            for i in range(4):
                nc, nr = c + dc[i] , r + dr[i]

                if 0 <= nc < max_c and 0 <= nr < max_r and not visited[nc][nr] and maps[nc][nr] != "X":
                    visited[nc][nr] = visited[c][r] + 1
                    queue.append((nc, nr))

        return visited[end[0]][end[1]]
    
    dr = [0,0,1,-1]
    dc = [-1,1,0,0]
    
    max_r, max_c = len(maps[0]), len(maps)
    
    for i in range(max_c):
        for j in range(max_r):
            if maps[i][j] == 'S':
                pos_start = (i,j)
            elif maps[i][j] == 'L':
                pos_lever = (i,j)
            elif maps[i][j] == 'E':
                pos_end = (i,j)
                
    d1 = bfs(pos_start,pos_lever)
    d2 = bfs(pos_lever,pos_end)
    
    return d1 + d2 if d1 and d2 else -1