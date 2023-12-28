from collections import deque
def solution(maps):
    answer = 0
    width = len(maps[0])
    height = len(maps)
    d = deque()
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    start = (0,0)
    d.append(start)
    while d:
        x,y = d.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x <=height-1 and 0 <= new_y <= width-1:
                if maps[new_x][new_y] == 1:
                    maps[new_x][new_y] = maps[x][y] + 1
                    d.append((new_x,new_y))
                    
    if maps[height-1][width-1] == 1:
        return -1
    return maps[height-1][width-1]