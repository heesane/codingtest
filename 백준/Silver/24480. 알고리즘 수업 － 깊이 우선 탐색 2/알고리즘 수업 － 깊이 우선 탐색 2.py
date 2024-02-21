# 백준 24480 알고리즘 수업-깊이 우선 탐색 2
import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline

def dfs(start):
    global check 
    visited[start] = True
    count[start] = check
    graph[start].sort(reverse=True)

    for i in graph[start]:
        if not visited[i]:
            check += 1
            dfs(i)


N,M,R = map(int, input().split())

# 해당 노드를 몇번째로 방문했는지 확인하는 리스트
count = [0] * (N+1)
check = 1
# 방문 여부 확인 / 1번 인덱스부터 확인
visited = [False]*(N+1)

# 그래프 생성
graph = [[] for _ in range(N + 1)]

# 그래프 입력
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(R)

for i in count[1:]:
    print(i)