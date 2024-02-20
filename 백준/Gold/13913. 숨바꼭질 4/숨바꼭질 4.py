# 백준 13913 숨바꼭질 4

from collections import deque

def bfs(start,end):
    global visited_list
    q = deque([(start)])
    visited = [0] * MAX
    visited[start] = 1
    
    prev_node = [-1] * MAX
    
    while q:
        x = q.popleft()
        
        if x == end:
            print(visited[x] - 1)
            path = []
            while x != -1:
                path.append(x)
                x = prev_node[x]
            print(*reversed(path))
            return 
        
        for nx in (x-1,x+1,2*x):
            if 0<= nx < MAX and not visited[nx]: 
                visited[nx] = visited[x] + 1
                prev_node[nx] = x
                q.append(nx)
                
        
        
N,K = map(int,input().split())
MAX = 100001
visited_list = [N]

bfs(N,K)