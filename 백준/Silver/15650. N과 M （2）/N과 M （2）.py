# 백준 15650 N과 M (2)

N, M = map(int,input().split())

visited = [False] * (N+1)

ans = []

def dfs():
    if len(ans) == M:
        print(' '.join(map(str,ans)))
    
    for i in range(1,N+1):
        if not visited[i]:
            if len(ans) == 0:
                ans.append(i)
                visited[i] = True
                dfs()
                ans.pop()
                visited[i] = False
            
            else:
                if i > ans[-1]:
                    ans.append(i)
                    visited[i] =True
                    dfs()
                    ans.pop()
                    visited[i] = False
    
dfs()
