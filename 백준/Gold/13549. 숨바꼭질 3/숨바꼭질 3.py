from collections import deque

def bfs(start,end):
    q = deque([start])
    visited = [0] * MAX
    while q:
        x = q.popleft()
        if x == end:
            return visited[x]

        for nx in (x-1,x+1,2*x):
            if 0 <= nx < MAX and not visited[nx]:
                if nx == 2*x and x!=0:
                    visited[nx] = visited[x]
                    q.appendleft(nx)
                else:
                    visited[nx] = visited[x] + 1
                    q.append(nx)

MAX = 100001

N,K = map(int,input().split())

print(bfs(N,K))