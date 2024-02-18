# 백준 16940번 BFS 스페셜 저지

from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]

# 그래프 만들기
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 입력받은 순서
b = list(map(int, input().split()))
# 입력받은 순서의 인덱스
order = [0] * (n+1)

# 입력받은 순서의 인덱스를 저장
for i in range(n):
    order[b[i]] = i
    
for i in range(1, n+1):
    graph[i].sort(key=lambda x: order[x])

def bfs(start):
    visited = [False] * (n+1)
    q = deque()
    q.append(start)
    visited[start] = True
    index = 0

    while q:
        now = q.popleft()
        if now != b[index]:
            return 0
        index += 1

        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

    return 1

print(bfs(1))
