# 백준 1931 회의실 배정

N = int(input())

convention = [list(map(int,input().split())) for _ in range(N)]

convention.sort(key = lambda x : (x[1],x[0]))

end = 0
cnt = 0

for i in range(N):
    if convention[i][0] >= end:
        end = convention[i][1]
        cnt += 1

print(cnt)