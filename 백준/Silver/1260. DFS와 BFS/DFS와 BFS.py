## DFS와 BFS
## 13:04
from collections import deque

N,M,V = map(int,input().split())
dfs_list = [ False for _ in range(N+1)]
bfs_list = [False for _ in range(N+1)]

check_list = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    check_list[a].append(b)
    check_list[b].append(a)
    
## DFS
def dfs(start):
    dfs_list[start] = True
    print(start,end=" ")
    check_list[start].sort()
    for i in range(len(check_list[start])):
        if dfs_list[check_list[start][i]]== False:
            dfs(check_list[start][i])
            
def bfs(start):
    bfs_list[start] = True
    q = deque()
    q.append(start)
    while len(q)!=0:
        t = q.popleft()
        print(t,end=" ")
        check_list[t].sort()
        for i in range(len(check_list[t])):
            if bfs_list[check_list[t][i]] == False:
                q.append(check_list[t][i])
                bfs_list[check_list[t][i]] = True
dfs(V)
print()
bfs(V)
