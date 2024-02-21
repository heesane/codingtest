# 백준 24479 알고리즘 수업-깊이 우선 탐색 1
import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline

N,M,R = map(int, input().split())

# 해당 노드를 몇번째로 방문했는지 확인하는 리스트
count = [0] * (N+1)
check = 1
# 방문 여부 확인 / 1번 인덱스부터 확인
visited = [False]*(N+1)

# 그래프 생성
graph = [[] for _ in range(N + 1)]

# 노드 방문 가능
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# 해당 노드의 방문 순서를 오름차순으로 정렬
for _ in range(N):
    graph[_].sort()

def dfs(graph,visited,start):
    global check
    visited[start] = True
    count[start] = check
    check += 1
    
    for i in graph[start]:
        if not visited[i]:
            dfs(graph,visited,i)

dfs(graph,visited,R)

for _ in range(1,N+1):
    print(count[_])