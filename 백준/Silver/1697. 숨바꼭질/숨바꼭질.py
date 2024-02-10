# 백준 1697번 숨바꼭질

from collections import deque

def bfs():
    q = deque([n])
    while q:
        v = q.popleft()
        if v == k:
            print(visited[v])
            break
        for next_step in (v-1, v+1, v*2):
            if 0 <= next_step < MAX and not visited[next_step]:
                visited[next_step] = visited[v] + 1
                q.append(next_step)

MAX = 100001

n, k = map(int, input().split())

visited = [0] * MAX

bfs()